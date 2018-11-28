#include <stdio.h>
#include <string.h>
#include <stdlib.h>

class sss
{
public:
	char s[11];
	char looks[11];
	int hash[27];
	int len;
	int cost;
	int ori_order;
};

char order[27];
sss dic[10002];

void get_look(int left,int right, char reveal)
{
	int i,j;
	for(i=left;i<right;i++)
	{
		for(j=0;j<dic[i].len;j++)
		{
			if(dic[i].s[j] == reveal)
				dic[i].looks[j] = reveal;
		}
	}
}

int cmp(const void *a, const void *b)
{
	sss* c = (sss *)a;
	sss* d = (sss *)b;
	return strcmp( c->looks, d->looks );
}

void ssort(int left,int right)
{
	qsort(dic + left, right - left, sizeof(dic[0]), cmp);
}


void guess(int left,int right,int last,int total_cost)
{
	int i,yes;
	int guessed = 0;
	if(right - 1 == left)
	{
		dic[left].cost = total_cost; return;
	}
	while(last<26)
	{
		yes = 0;
		for(i = left; i < right; i++)
		{
			if(dic[i].hash[ order[last] - 'a'])
			{
				yes = 1;
				break;
			}
		}
		if(yes)
			break;
		last++;
	}
	get_look(left,right,order[last]);
	ssort(left,right);
	int lll = left;
	while(lll < right)
	{
		for(i = lll+1; i<right; i++)
		{
			if( strcmp(dic[i-1].looks, dic[i].looks) != 0 )
				break;
		}
		if( dic[i-1].hash[ order[last] - 'a'] == 0)
			guessed = 1;
		else
			guessed = 0;
		guess(lll,i,last+1,total_cost+guessed);

		lll = i;
	}
}

int main()
{
	int i,j,cas,asd,k,dsa;
	int n,m;

	freopen("22.in","r",stdin);
	freopen("22.out","w",stdout);

	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d %d",&n,&m);

		for(i=0;i<n;i++)
		{
			scanf("%s",dic[i].s);
			for(j=0;j<26;j++)
				dic[i].hash[j] = 0;
			dic[i].ori_order = i;
		}
		printf("Case #%d:",asd+1);
		for(dsa=0;dsa<m;dsa++)
		{
			scanf("%s",order);
			for(j=0;j<n;j++)
			{
				dic[j].len = strlen(dic[j].s);
				for(k=0;k<dic[j].len;k++)
				{
					dic[j].looks[k] = '-';
					dic[j].hash[ dic[j].s[k] - 'a' ] = 1;
				}
				dic[j].looks[dic[j].len] = 0;
			}
			
			ssort(0,n);

			int lll = 0;
			while(lll < n)
			{
				for(i = lll+1; i<n; i++)
				{
					if( dic[i-1].len!=dic[i].len)
						break;
				}
				guess(lll,i,0,0);

				lll = i;
			}


			int max = -1;
			int maxp = -1;
			int min2;
			for(i=0;i<n;i++)
			{
				if(dic[i].cost > max)
				{
					max = dic[i].cost;
					min2 = dic[i].ori_order;
					maxp = i;
				}
				else if(dic[i].cost == max && dic[i].ori_order < min2)
				{
					min2 = dic[i].ori_order;
					maxp = i;					
				}
			}
			printf(" %s",dic[maxp].s);
		}
		printf("\n");

	}
	return 0;
}