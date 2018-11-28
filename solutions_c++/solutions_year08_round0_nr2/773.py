#include<iostream>
using namespace std;
struct train {
	int op,t,s;
} s[1000];
int n;
inline bool cmp(const train& a,const train& b)
{
	return a.t<b.t || (a.t==b.t && a.op<b.op);
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,c;
	scanf("%d",&T);
	for (c=1;c<=T;++c) {
		int i,t,a,b;
		n=0;
		scanf("%d",&t);
		scanf("%d%d",&a,&b);
		for (i=0;i<a;++i) {
			int t1,t2,h1,m1,h2,m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			t1=h1*60+m1;t2=h2*60+m2+t;
			s[n].op=0;s[n].t=t2;s[n++].s=1;
			s[n].op=1;s[n].t=t1;s[n++].s=0;
		}
		for (i=0;i<b;++i) {
			int t1,t2,h1,m1,h2,m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			t1=h1*60+m1;t2=h2*60+m2+t;
			s[n].op=0;s[n].t=t2;s[n++].s=0;
			s[n].op=1;s[n].t=t1;s[n++].s=1;
		}
		sort(s,s+n,cmp);
		int cur[2]={0},need[2]={0};
		for (i=0;i<n;++i) {
			if (s[i].op==0) {
				cur[s[i].s]++;
			} else {
				if (cur[s[i].s]==0) {
					++cur[s[i].s];
					++need[s[i].s];
				}
				--cur[s[i].s];
			}
		}
		printf("Case #%d: %d %d\n",c,need[0],need[1]);
	}
}
