#include <iostream>
using namespace std;
int mm[105];
bool judge(int x,int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(!(x%mm[i]==0||mm[i]%x==0))return 0;
	}
	return 1;
}
int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	int i,n,l,h;
	int cnt=0;
	scanf("%d",&T);
	while(T--)
	{

		cnt++;
		printf("Case #%d: ",cnt);
		scanf("%d%d%d",&n,&l,&h);
		for(i=0;i<n;i++)scanf("%d",&mm[i]);
		for(i=l;i<=h;i++)
		{
			if(judge(i,n))
			{
				break;
			}
		}
		if(i<=h)printf("%d\n",i);
		else printf("NO\n");
	}
}