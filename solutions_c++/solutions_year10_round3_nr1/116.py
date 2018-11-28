#include<iostream>
#include<string>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#include<deque>
using namespace std;

struct DD
{
	int A,B;
}dd[1005];

inline bool cmp(const DD &a,const DD &b)
{
	return a.A < b.A;
}

int sum[10005];

inline int lowbit(int t)
{
	return t&(-t);
}
void update(int t)
{
	while( t<=10000 )
	{
		sum[t]++;
		t+=lowbit(t);
	}
}

int getsum(int t)
{
	int ret=0;
	while( t>=1 )
	{
		ret+=sum[t];
		t-=lowbit(t);
	}
	return ret;
}


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int CAS,Te=1;
	cin>>CAS;
	while(CAS--)
	{
		int N;
		cin>>N;
		for(int i=0;i<N;i++) cin>>dd[i].A>>dd[i].B;
		sort(dd,dd+N,cmp);

		memset(sum,0,sizeof(sum));

		int ans=0,num=0;
		for(int i=0;i<N;i++)
		{
			int s=getsum(dd[i].B);
			update(dd[i].B);
			ans+=num-s;
			num++;
		}
		printf("Case #%d: %d\n",Te++,ans);
	}
}