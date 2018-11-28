#include<stdio.h>
#include<memory.h>

int ans[10][1<<10];
bool can[10][10];
int ccan[10];

int R,C;

int N;

char str[100];
int one[1<<10];

void init()
{
	int i,j;
	scanf("%d%d",&R,&C);
	memset(can,true,sizeof(can));
	for(i=0;i<R;i++)
	{
		scanf("%s",str);
		for(j=0;j<C;j++)
		{
			if(str[j]=='x')
				can[i][j]=false;
		}
	}
	memset(ccan,0,sizeof(ccan));
	for(i=0;i<R;i++)
		for(j=0;j<C;j++)
		{
			if(!can[i][j])
				ccan[i]|=1<<j;
		}
}

bool judge(int m,int n)
{
	if(n&ccan[m])
		return false;
	if(n&(n>>1))
		return false;
	if(n&(n<<1))
		return false;
	return true;
}

bool jjudge(int n,int m)
{
	if(n&(m>>1))
		return false;
	if(n&(m<<1))
		return false;
	return true;
}

void solve()
{
	int i,j,k;
	memset(ans,0,sizeof(ans));
	for(i=0;i<(1<<C);i++)
	{
		if(judge(0,i))
			ans[0][i]=one[i];
	}
	for(i=1;i<R;i++)
		for(j=0;j<(1<<C);j++)
		{
			if(judge(i,j))
			{
				for(k=0;k<(1<<C);k++)
				{
					if(jjudge(j,k))
					{
						if(ans[i-1][k]+one[j]>ans[i][j])
							ans[i][j]=ans[i-1][k]+one[j];
					}
				}
			}
		}
	int ret=0;
	for(i=0;i<R;i++)
		for(j=0;j<(1<<C);j++)
		{
			if(ans[i][j]>ret)
				ret=ans[i][j];
		}
	printf("%d\n",ret);
}

int main()
{
	int i;
	//freopen("C.in","r",stdin);
	//freopen("C.txt","w",stdout);
	memset(one,0,sizeof(one));
	for(i=1;i<1024;i++)
		one[i]=one[i>>1]+(i&1);
	scanf("%d",&N);
	for(i=1;i<=N;i++)
	{
		init();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}


	