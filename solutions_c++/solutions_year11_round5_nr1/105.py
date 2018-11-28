#include <vector>
#include <cstring>
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
#include <sstream>
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <stdlib.h>
#include <ctime>
#include <string>
#include <complex>
#ifdef __ASD__
#include <windows.h>
#endif
using namespace std;
#define all(a) a.begin(),a.end()
#define forn(i,n) for(int i=0;i<(n);++i)
#define fornn(i,n) for(i=0;i<(n);++i)
#define lng long long
#define SQ(a) ((a)*(a))
#define forv(i,v) for(int i=0;i<(int)v.size();++i)
#define mp make_pair
#define pb push_back
#define ABS(a) ((a)<0?-(a):(a))
#define iinf 1000000000
#define left asdleft
#define prev asdprev
#define eps 1e-10
#define y1 asdy1
#define y2 asdy2
#define EQ(a,b) abs((a)-(b))<eps
void mytimer(string task){
#ifdef __ASD__
	static LARGE_INTEGER prev;	LARGE_INTEGER cur,freq;	QueryPerformanceCounter(&cur);	QueryPerformanceFrequency(&freq);	if(task!="")		cout<<task<<" took "<<(cur.QuadPart-prev.QuadPart)*1.0/freq.QuadPart<<endl;	prev=cur;
#endif
}

vector<pair<int,int> > pts0[2];
vector<pair<int,double> > pts;

void solve(){
	pts0[0].clear();
	pts0[1].clear();
	pts.clear();
	int W,n1,n2,G;
	cin>>W>>n1>>n2>>G;
	forn(i,n1){
		int x,y;
		cin>>x>>y;
		pts0[0].pb(mp(x,y));
	}
	forn(i,n2){
		int x,y;
		cin>>x>>y;
		pts0[1].pb(mp(x,y));
	}

	forn(s,2){
		forv(i,pts0[s]){
			int x,y;
			x=pts0[s][i].first;
			y=pts0[s][i].second;
			int x1,x2,y1,y2;
			int p=lower_bound(all(pts0[1-s]),mp(x,-iinf))-pts0[1-s].begin();
			x2=pts0[1-s][p].first;
			y2=pts0[1-s][p].second;
			double ty;
			if(x2==x)
				ty=y2;
			else{
				x1=pts0[1-s][p-1].first;
				y1=pts0[1-s][p-1].second;

				ty=1.*(y1*(x2-x)+y2*(x-x1))/(x2-x1);
			}

			pts.pb(mp(x,abs(ty-y)));
		}
	}

	sort(all(pts));

	double area=0;
	int n=pts.size();
	forn(i,n-1){
		area+=(pts[i+1].first-pts[i].first)*(pts[i].second+pts[i+1].second);
	}
	area/=G;

	vector<double> res;

	double cur=0;
	forn(i,n-1){
		double y1=pts[i].second;
		double y2=pts[i+1].second;
		double x1=pts[i].first;
		double x2=pts[i+1].first;
		double t=(x2-x1)*(y1+y2);
		while(cur+t>=area){
			double k=(y2-y1)/(x2-x1);
			double a,b,c;
			a=k;
			b=2*y1;
			c=-area+cur;
			double x;
			if(EQ(a,0))
				x=-c/b;
			else{
				double d=b*b-4*a*c;
				if(d<0)
					exit(312);
				d=sqrt(d);
				x=(-b+d)/(2*a);
			}
			if(x<0||x>x2-x1+eps)
				exit(232);
			
			y1=y1+k*x;
			x1+=x;
			res.pb(x1);
			cur=0;
			t=(x2-x1)*(y1+y2);
		}
		cur+=t;
	}

	if(res.size()==G)
		res.pop_back();

	if(res.size()!=G-1)
		exit(444);

	cout<<endl;
	forv(i,res)
		printf("%.12lf\n",res[i]);
}

int main(){
#ifdef __ASD__
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	forn(qqq,tc){
		cout<<"Case #"<<qqq+1<<": ";
		solve();
	}

    return 0;
}
