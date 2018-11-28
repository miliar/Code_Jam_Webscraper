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

int a[1111],b[1111];

bool v[1111];
double m[1111];

double getM(int n){
	if(v[n]) return m[n];
	double val = 0;

	return v[n]=1,m[n]=val;
}

bool F[1111];
double f[1111];
double getF(int n){
	if(n<=1) return 1.;
	if(F[n]) return f[n];
	double v = n * getF(n-1);
	return F[n]=true,f[n]=v;
}

bool u[1111];
double r[1111];

double solve(int n){
	if(n<2) return 0.;
	if(u[n]) return r[n];
	double v = 1;
	double tmp = 0;
	double f = 1;
	FOR(i,2,n){
		f /= i;
		tmp += (i%2 ? -1 : 1) * f;
		v += tmp * solve(i) / getF(n-i);
		 //(1/2 - 1/3! + 1/4! - ...) * solve(i) / (n-i)! 

	}
	v /= (1 - (tmp + (n%2 ? -1 : 1) * f / n) ); 
	return u[n]=1,r[n]=v;
}

int main(){ 
#ifdef LocalHost
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int tc;
	cin>>tc;
	REP(TC,tc){
		int n;
		cin>>n;
		REP(i,n) cin>>a[i],b[i]=a[i];
		sort(b,b+n);
		int num = 0;
		REP(i,n)if(a[i]!=b[i]) num++;
		printf("Case #%d: %.6lf\n",TC+1,(double)num);
	}
	return 0;
}