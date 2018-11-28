#include <set>
#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)

int N,T,A,B;
struct tr
{
	int a,b,s;
	void get()
	{
		int h,m;
		scanf("%d:%d",&h,&m);
		a=60*h+m;
		scanf("%d:%d",&h,&m);
		b=60*h+m;
	}
	bool operator<(const tr& c)const
	{
		return a<c.a||a==c.a&&b<c.b;
	}
}t[200];
multiset<int> qA,qB;

int main()
{
	freopen("B.in","r",stdin);freopen("B.out","w",stdout);
	scanf("%d",&N);
	REP(i,N)
	{
		scanf("%d%d%d",&T,&A,&B);
		REP(j,A){t[j].get();t[j].s=0;}
		REP(j,B){t[j+A].get();t[j+A].s=1;}
		sort(t,t+A+B);
		int needA=0,needB=0;
		qA.clear(),qB.clear();
		REP(j,A+B)
			if(!t[j].s)
			{
				if(qA.empty()||*qA.begin()>t[j].a)needA++;
				else qA.erase(qA.begin());
				qB.insert(t[j].b+T);
			}
			else
			{
				if(qB.empty()||*qB.begin()>t[j].a)needB++;
				else qB.erase(qB.begin());
				qA.insert(t[j].b+T);
			}
		printf("Case #%d: %d %d\n",i+1,needA,needB);
	}
	return 0;
}
