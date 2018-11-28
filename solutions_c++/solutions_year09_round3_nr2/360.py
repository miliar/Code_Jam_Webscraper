// 3.cpp : Defines the entry point for the console application.
//
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define sz(a) int((a).size()) 
#define pb push_back 
typedef long long LL;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 


int main()
{
	int r;
	cin>>r;
	REP(i,r)
	{
		vector<double> x(1000);vector<double> y(1000);vector<double> z(1000);
		vector<double> vx(1000);vector<double> vy(1000);vector<double> vz(1000);

		int N;
		cin>>N;
		double sumx=0;double sumy=0;double sumz=0;
		double sumvx=0;double sumvy=0;double sumvz=0;
		REP(j,N)
		{
			cin>>x[j]>>y[j]>>z[j]>>vx[j]>>vy[j]>>vz[j];
		}
		double sum1 =0;
		double sum2=0;
		REP(j,N)
		{
			sumx+=x[j];
			sumy+=y[j];
			sumz+=z[j];
			sumvx+=vx[j];sumvy+=vy[j];sumvz+=vz[j];	
		}
		double t;
		if((sumvx*sumvx+sumvy*sumvy+sumvz*sumvz)==0)
			t=0;
		else
			 t= -(sumx*sumvx+sumy*sumvy+sumz*sumvz)/(sumvx*sumvx+sumvy*sumvy+sumvz*sumvz);

		if(t<=0) t =0;
		sumx=sumy=sumz=0;
		REP(j,N)
		{
			sumx +=x[j]+vx[j]*t;
			sumy = sumy+y[j]+vy[j]*t;
			sumz= sumz+z[j]+vz[j]*t;
		}
		double d = sqrt(sumx*sumx+sumy*sumy+sumz*sumz)/N;
		//cout<<"Case #"<<i+1<<": ";
		//cout<<d<<" "<<t<<"\n";
		printf("Case #%d: %.9lf %.9lf\n",i+1,d,t);
	}	

	return 0;
}

