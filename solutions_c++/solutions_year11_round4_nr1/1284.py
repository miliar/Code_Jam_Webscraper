/*	SURENDRA KUMAR MEENA	*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <queue>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long int LL;
#define ALL(s) (s).begin(),(s).end()
#define R(i,m,n)	for(int i=m;i>=n;i--)
#define FF(i,m,n)	for(int i=m;i<n;i++)
#define F(i,n)	FF(i,0,n)
#define VI vector<int>
#define PB push_back
#define CLR(s,v) memset(s,v,sizeof(s))
string to_str(LL x){ ostringstream o;o<<x;return o.str();}
LL to_int(string s){ istringstream st(s); LL i;	st>>i;return i;}
#define FR(it,t) for(typeof(t.begin()) it=t.begin(); it!=t.end(); ++it)
typedef pair<double,double> PI;
typedef pair<PI,double> PII;
#define f first
#define s second
#define VP vector<PI>
#define S(t)	scanf("%d",&t)

const double eps = 1e-8;

bool cmp1(PII a, PII b){
	return a.s<b.s;
}

int main(){
	int tst;
	cin>>tst;
	FF(kase,1,tst+1){
		cout<<"Case #"<<kase<<": ";
		double x,s,r,t;
		int n;
		cin>>x>>s>>r>>t>>n;
		vector< PII > v(n);
		F(i,n)
			cin>>v[i].f.f>>v[i].f.s>>v[i].s;
		sort(ALL(v));
		if(v[0].f.f > eps)
			v.insert(v.begin(), PII(PI(0,v[0].f.f),0));
		for(int i=1;i<v.size();){
			if(v[i].f.f > v[i-1].f.s + eps){
				v.insert(v.begin()+i, PII(PI(v[i-1].f.s,v[i].f.f),0));
			}
			else
				i++;
		}
		int sz = v.size();
		if(v[sz-1].f.s + eps < x){
			v.PB(PII(PI(v[sz-1].f.s,x),0));
			sz++;
		}
		sort(ALL(v),cmp1);
		double tm=(double)t;
		int i=0;
		while(tm>0.0 && i<sz){
			double dist = v[i].f.s - v[i].f.f;
			double sp = v[i].s + r;
			if(dist > sp*tm + eps){
				v.insert(v.begin()+i, PII(PI(v[i].f.f, v[i].f.f+sp*tm),sp));
				v[i+1].f.f = v[i].f.f+sp*tm;
				sz++;
				i++;
				break;
			}
			else{
				tm -= dist/sp;
				v[i].s+=r;
			}
			i++;
		}
		double ans=0.0;
//		F(j,sz){
//			cout<<v[j].f.f<<" "<<v[j].f.s<<" : "<<v[j].s<<endl;
//		}
		F(j,i)
			ans += (v[j].f.s-v[j].f.f)/(v[j].s);
		FF(j,i,sz)
			ans += (v[j].f.s-v[j].f.f)/(v[j].s+s);
		
		printf("%.7lf\n",ans);
	}
	return 0;
}
