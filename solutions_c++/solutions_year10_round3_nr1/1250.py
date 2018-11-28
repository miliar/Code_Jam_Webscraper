#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;
struct PAIR{
	int h1,h2;
};
PAIR p[1010];
int n;
bool cmp(const PAIR &x,const PAIR &y)
{
	return x.h1<y.h1;
}
void input()
{
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		scanf("%d%d",&p[i].h1,&p[i].h2);
	}
	sort(p,p+n,cmp);
}
int cal()
{
	int cnt=0;
	for(int i=0;i<n;++i)
	{
		for(int j=i+1;j<n;++j)
			if(p[j].h2<p[i].h2) cnt++;
	}
	return cnt;
}
int main()
{
	freopen("rope.in","r",stdin);
	freopen("rope.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	for(int t=1;t<=cs;++t)
	{
		printf("Case #%d: ",t);
		input();
		printf("%d\n",cal());
	}
	return 0;
}
