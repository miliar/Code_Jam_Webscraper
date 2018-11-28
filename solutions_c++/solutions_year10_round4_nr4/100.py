#pragma comment(linker,"/STACK:256000000")
//#pragma comment(linker,"/STACK:536870912")
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <cstring>
#include <ctime>
#include <memory.h>
using namespace std;

#define lng long long
#define PB push_back
#define pii pair<int,int>
#define MPII make_pair<int,int>
#define PLL pair<lng,lng>
#define MPLL make_pair<lng,lng>
#define PI 3.1415926535897932384626433832795
#define DEG2RAD (PI/180.0)
#define RAD2DEG (1.0/DEG2RAD)
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define forn(i,n) for(int i=0;i<n;++i)
#define fornr(i,n) for(int i=n-1;i>=0;--i)
#define forn1(i,n) for(i=0;i<n;++i)
#define forv(i,v) for(int i=0;i<v.size();++i)
#define forvr(i,v) for(int i=v.size()-1;i>=0;--i)
#define fors(i,s) for(int i=0;i<s.length();++i)
#define EPS 1e-12
#define eps EPS
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)
#define iinf 1000000000
#define linf 100000000000000000LL
#define maxll ((1LL<<62)-1+(1LL<<62))
#define dinf 10000000000000000000000.0
#define SQ(a) ((a)*(a))
#define SWAP(t,a,b) {t ____tmpasdasdasd=(a);(a)=(b);(b)=____tmpasdasdasd;}
#define left _left
#define y1 asdy1
#define y2 asdy2
#define y0 asdy0
#define abs(a) ((a)<0?-(a):(a))
#define mat _mat
#define ALL(a) (a).begin(),(a).end()
#ifdef __TRATATA__
//#include "my.h"
#endif



int main(){
#ifdef __TRATATA__
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	forn(q,tc){
		int n,m;
		cin>>n>>m;
		if(n!=2)
			continue;
		cout<<"Case #"<<q+1<<":";
		double x0,y0,x1,y1;
		cin>>x0>>y0>>x1>>y1;
		forn(i,m){
			double xx,yy;
			cin>>xx>>yy;
			double r0=sqrt(SQ(x0-xx)+SQ(y0-yy));
			double r1=sqrt(SQ(x1-xx)+SQ(y1-yy));
			double a0,a1;
			double c=sqrt(SQ(x1-x0)+SQ(y1-y0));
			a0=2*acos((SQ(r0)+SQ(c)-SQ(r1))/(2*r0*c));
			a1=2*acos((SQ(r1)+SQ(c)-SQ(r0))/(2*r1*c));
			double s=a0*SQ(r0)/2-SQ(r0)*sin(a0)/2+a1*SQ(r1)/2-SQ(r1)*sin(a1)/2;
			printf(" %.10lf",s);
		}
		cout<<endl;
	}

    return 0;
}