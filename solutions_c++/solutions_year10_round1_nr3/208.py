#include <iostream>
using namespace std;

int tot,a1,a2,b1,b2;
long long cnt;

bool win(int x,int y)
{
	if (x<y)
	{	int c=x;x=y;y=c;}
	if (x==y) return false;
	if (x%y==0) return true;
	if (x>2*y) return true;
	return !win(y,x-y);
}

void work()
{
	for (int i=a1;i<=a2;++i)
		for (int j=b1;j<=b2;++j)
			if (win(i,j)) ++cnt;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&tot);
	for (int tc=1;tc<=tot;++tc)
	{
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		cnt=0;
		work();
		printf("Case #%d: %I64d\n",tc,cnt);
	}
	return 0;
}
