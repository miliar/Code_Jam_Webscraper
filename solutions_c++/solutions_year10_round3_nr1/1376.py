#include<iostream>
#include<algorithm>
using namespace std;
typedef long long llong;
llong c[100003];
struct PH
{
	int x,y;
	bool operator<(const PH &h)const
	{return x>h.x;}
}ph[1003];
int lowbit(int x)
{
	return x&-x;
}
const int N=100001;
void update(int pos,int val)
{
	int i;
	for(i=pos;i<=N;i+=lowbit(i))
	{
		c[i]+=val;
	}
}
llong query(int pos)
{
	llong sum=0;
	int i;
	for(i=pos;i>0;i-=lowbit(i))
	{
		sum+=c[i];
	}
	return sum;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,j,oo=1;
	int n;
	llong ans;
	scanf("%d",&t);
	while(t--)
	{
		ans=0;
		scanf("%d",&n);
		memset(c,0,sizeof(c));
		for(i=0;i<n;i++)
			scanf("%d %d",&ph[i].x,&ph[i].y);
		sort(ph,ph+n);
		for(i=0;i<n;i++)
		{
			ans+=query(ph[i].y);
			update(ph[i].y,1);
		}
		printf("Case #%d: ",oo++);
		cout<<ans<<endl;
	}
	return 0;
}