#include <cstdio>

int t,r,k,n;
int arr[10];

void init()
{
	int i;
	scanf("%d%d%d",&r,&k,&n);
	for (i=0;i<n;i++)
		scanf("%d",&arr[i]);
}

void solve()
{
	int earn=0,i,times,gcnt,pcnt;
	i=0;
	for (times=0;times<r;times++)
	{
		gcnt=0;
		pcnt=0;
		while(gcnt<n)
		{
			pcnt+=arr[i];
			if (pcnt>k)
			{
				pcnt-=arr[i];
				break;
			}
			i=(i+1)%n;
			gcnt++;
		}
		earn+=pcnt;
	}
	printf("%d\n",earn);
}

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		init();
		printf("Case #%d: ",i);
		solve();
	}
}
