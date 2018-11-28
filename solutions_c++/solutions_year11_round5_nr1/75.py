#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

int w,l,u,g;

int x[1111],y[1111];
int X[1111],Y[1111];

int xx[2111],yy[2111];

const double eps = 1e-9;

double getSQ(double r){
	double s = 0;
	double Y1 = 0;
	double Y2 = -1e100;
	REP(i,l+u){
		if(xx[i] <= r + eps && xx[i+1]<=r + eps){
			s += xx[i+1]*yy[i] - yy[i+1]*xx[i];
			if(i+1<l) Y1 = yy[i+1];
			if(i>=l && Y2 < -1e50) Y2 = yy[i];
		}else if(xx[i] <= r + eps){
			double nx = r;
			double ny = yy[i] + (yy[i+1]-yy[i])/(0.+xx[i+1]-xx[i])*(nx - xx[i]);
			s += nx * yy[i] - ny * xx[i];
			if(i+1<l) Y1 = ny;
		}else if(xx[i+1] <= r + eps){
			double nx = r;

			double ny = yy[i] + (yy[i+1]-yy[i])/(0.+xx[i+1]-xx[i])*(nx - xx[i]);
			s += xx[i+1]*ny - yy[i+1] * nx;
			if(i>=l) Y2 = ny;
		}
	}
	s += r * (Y1 - Y2);
	if(s<0) s = -s;
	return s;
}

int main(){ 
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int tc;
	cin>>tc;
	REP(TC,tc){
		cin>>w>>l>>u>>g;
		g--;
		REP(i,l) cin>>x[i]>>y[i],xx[i]=x[i],yy[i]=y[i];
		REP(i,u) cin>>X[i]>>Y[i],xx[l+u-1-i]=X[i],yy[l+u-1-i]=Y[i];
		xx[l+u]=xx[0];
		yy[l+u]=yy[0];

		ll sq = 0;
		REP(i,l+u) sq += xx[i+1]*yy[i] - yy[i+1]*xx[i];
		if(sq<0) sq = -sq;
		//cout<<getSQ(5)<<endl;
		printf("Case #%d:\n",TC+1);
		REP(i,g){
			double a = 0;
			double b = w;
			double need = sq / double(g + 1) * (i+1);
			REP(j,100){
				double s = (a+b)/2;
				double ss = getSQ(s);
				if(ss > need) b = s;
				else a = s;
			}
			printf("%.10lf\n",a);
		}
		//puts("");
	}
#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif
	return 0;
}