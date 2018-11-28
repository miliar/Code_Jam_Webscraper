#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char s[500005];
char s2[500005];
int best[65536][16];
int used[20];
int k,t,p;

void dfs(int value,int last,int depth)
{
	int i,j;
	int tmp,count;
	if(depth==1)
	{
		if(value!=0)
			abort();
		count = t;
		for(j=0;j<t;j++)
		{
			if(s[j*k+p] != s[j*k+last] )
				count++;
		}
		best[value][last] = count;
		return;
	}
	if(best[value][last]!=-1)
		return;
	for(i=0;i<k;i++)
	{
		if(!used[i])
		{
			tmp  = value & (~(1<<i));
			used[i] =1;
			dfs(tmp, i, depth-1);

			used[i]=0;

			count = best[tmp][i];

			for(j=0;j<t;j++)
			{
				s2[j*k+depth-1] = s[j*k+i];
				if(s[j*k+last] != s[j*k+i] )
					count++;

			}
			if(best[value][last]==-1 || count < best[value][last])
				best[value][last] = count;
		}
	}
	
}

int main()
{
	int value;
	int i,j,q,l;
	int cas,asd;
	int count,min;
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d",&k);
		scanf("%s",s);
		l=strlen(s);
		t = l / k;
		for(i=0;i<k;i++)
			used[i] = 0;
		min = 1000000000;
		for(p=0;p<k;p++) /* p is the first one */
		{
			used[p] = 1; /* need initialize */
			for(i=0;i<(1<<k);i++)
			{
				for(j=0;j<k;j++)
					best[i][j] = -1;
			}
			
			for(q=0;q<k;q++)
			{
				if(p==q)
					continue;
				/* fill first p */
				for(i=0;i<t;i++)
					s2[i*k] = s[i*k+p]; 

				for(i=0;i<t;i++)
					s2[i*k+k-1] = s[i*k+q]; 

				used[q] = 1;
				
				value = (1<<k) - 1;
				value = value & (~(1<<p));

				value = value & (~(1<<q));
				dfs(value,q,k-1);
				count = best[value][q];

/*				for(j=0;j<t;j++)
				{
					if(s2[j*k+k-1] != s2[j*k+k-2] )
						count++;
				}*/

				used[q] = 0;
	
				for(i=1;i<t;i++)
				{
					if(s[(i-1)*k + q] == s[i*k + p])
						count--;
				}
				if(count < min)
					min = count;

			}
			used[p] = 0;
		}
		printf("Case #%d: %d\n",asd+1,min);
	}
	return 0;
}