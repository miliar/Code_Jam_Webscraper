#include <stdio.h>
#include <string.h>

bool can[5];
int pth[5];
int N,len,ans;

char in[1100];
char to[1100];


int press()
{
	int i,cnt=1;
	for (i=1;i<len;++i)
	{
		if (to[i]!=to[i-1]) cnt++;
	}
	return cnt;
}

void Do()
{
	int i,j;
	for (i=0;i<len;i+=N)
	{
		for (j=0;j<N;++j)
		{
			to[i+j] = in[i+pth[j]];
		}
	}
	int temp=press();
	if (temp<ans) ans=temp;
	
}


int DFS(int dep)
{
	if (dep==N)
	{
		Do();
	}
	else
	{
		int i;
		for (i=0;i<N;++i)
		{
			if (can[i])
			{
				can[i]=false;
				pth[dep]=i;
				DFS(dep+1);
				can[i]=true;
			}
		}
	}
	return 0;
}
int main()
{
	freopen("D_small.txt","w",stdout);
	
	int t,st;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d",&N);
		scanf("%s",in);
		len=strlen(in);
		ans=0x7fffffff;
		memset(can,1,sizeof(can));
		DFS(0);
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}

