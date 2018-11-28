#include<cstdio>
#include<cstring>

using namespace std;

int r,k,n;
int g[13000];
void input()
{
	scanf("%d%d%d",&r,&k,&n);
	for(int i=0;i<n;++i)	
		scanf("%d",g+i);	
}
void solve()
{
	int earn=0;
	int tail=0,head=n-1;	
	while(r--)
	{	
		int cap=0,head2=head;		
		for(;tail<=head && cap+g[tail]<=k ;++tail)
		{
			cap+=g[tail];
			earn+=g[tail];
			head2++;
			g[head2]=g[tail];
		}
		head=head2;
	}
	printf("%d\n",earn);
}
int main()
{
	//freopen("theme.in","r",stdin);
	//freopen("theme.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	for(int t=1;t<=cs;++t)
	{
		input();
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
