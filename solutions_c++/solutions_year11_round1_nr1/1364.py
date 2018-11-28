#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
bool sol(int n,int d,int g)
{
	int i;
	if(d ==0 && g == 0 ) return true;
	if(d && !g ) return false;
	if(g == 100 ) return d==100;
	for(i=(d?1:0);i<=n;i++)
		if((d*i)%100==0)
			break;
	if(i>n) return false;
	for(i=(i==0?1:i);i<1001;i++)
		if((g*i)%100==0)
			break;
	if( i==1001) return false;
	return true;
}
int main()
{
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int TC,i,n,d,g;
	scanf("%d",&TC);
	for(int tc=1;tc<=TC;tc++)
	{
		scanf("%d %d %d",&n,&d,&g);
		printf("Case #%d: ",tc);
		if(sol(n,d,g))
			printf("Possible\n");
		else printf("Broken\n");
	}
	return 0;
}