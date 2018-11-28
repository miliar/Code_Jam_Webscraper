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
#include <sstream>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

struct cor
{
	double B, E, w;
};

double result;
double X, S, R, t;
int N;
vector <cor> corr;

bool ss(cor a, cor b)
{
	return a.w<b.w;
}

void cal(double ll, double w)
{
	if (t*(w+R) < ll)
	{
		result+=t;
		ll -= t*(w+R);
		result+=ll/(w+S);	
		t=0;	
	} else
	{
		result+=ll/(w+R);
		t-=ll/(w+R);
	}
//	cout<<ll<<" "<<result<<" "<<t<<	endl;//" "<<w<<" "<<S<<" "<<result<<endl;
}

int main()
{
	int ntest;
	cin>>ntest;
	FOR(kk, 1, ntest)
	{
		cin>>X>>S>>R>>t>>N;	
		corr.clear();
		REP(i, N)
		{
		 	cor tmp;
		 	cin>>tmp.B>>tmp.E>>tmp.w;
		 	corr.push_back(tmp);
		}
		sort(corr.begin(), corr.end(), ss);
		long khongthang=X;
		result=0;
		REP(i, corr.size()) khongthang-=(corr[i].E-corr[i].B);
		cal(khongthang, 0);
		REP(i, corr.size()) cal(corr[i].E-corr[i].B, corr[i].w);
		cout<<"Case #"<<kk<<": ";
		printf("%.8f\n", result);

	}	
	return 0;
}





















