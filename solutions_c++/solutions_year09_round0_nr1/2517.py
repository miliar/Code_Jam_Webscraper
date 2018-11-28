#include<stdio.h>
#include<string.h>
#include<set>
#include<string>

using namespace std;

#define MAXL 18
#define MAXD 5010

char dic[MAXD][MAXL];
char q[MAXD * MAXL];
int len, L, D, ans;
set<string> mdic[MAXL];

void get(int k,int ind, char str[])
{
	string tstr;

	if(ind == len)
	{
		if(k == L)
		{	
			tstr = str;
			int v=strlen(str);

			if(mdic[k].count(tstr))				
			{
				ans ++;				
			}	
		}
		return;
	}

	if(q[ind] == '(')
	{
		int i, lastind;

		for(i = ind + 1; ; i ++)
		{
			if(q[i] == ')')
			{
				lastind = i;
				break;
			}
		}

		for(i = ind + 1; i < lastind; i ++)
		{
			str[k] = q[i];
			str[k + 1] = 0;			
			tstr = str;
			if(mdic[k + 1].count(tstr))				
			{
				get(k + 1, lastind + 1, str);
			}
		}
	}
	else
	{
		str[k] = q[ind]; 
		str[k + 1] = 0;
		get(k + 1, ind + 1, str);
	}

	return ;
}

int main()
{
	int i, j, n, kase = 1;	
	char str[MAXL], temp[MAXL];
	string tstr;

	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);

	while(3 == scanf("%d %d %d ",&L, &D, &n))
	{
		for(i=0;i<MAXL;i++)	
		{
			mdic[i].clear();
		}
		
		for(i=0;i<D;i++)
		{
			scanf("%s", dic[i]);
		}

		for(i=0;i<D;i++)
		{
			for(j = 1; j <= L; j ++)
			{
				memset(temp, 0, sizeof(temp));
				strncpy(temp, dic[i], j);
				string tstr = temp;
				mdic[j].insert(tstr);		
			}			
		}

		for(i = 0; i < n; i ++)
		{
			scanf("%s", q);	
			ans = 0;
			len = strlen(q);
			memset(str, 0, sizeof(str));
			get(0, 0, str);
			printf("Case #%d: %d\n",kase ++, ans);
		}
	}

	return 0;
}

