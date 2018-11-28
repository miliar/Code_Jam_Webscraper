#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T gcd(T a,T b){return a==0?b:gcd(b%a,a);}
template<class T> inline int countbit(T n){return n==0?0:(1+countbit(n&(n-1)));}
template<class T> inline void pout(T A[],int n){cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<", ";cout<<"}\n";}
template<class T> inline void pout(vector<T> A,int n=-1){if (n==-1) n=A.size();cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<", ";cout<<"}\n";}

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,cs,h) for(i=(cs);i<=(h);++i)
#define FORD(i,h,cs) for(i=(h);i>=(cs);--i)
#define FORIT(a,aa) for(a=aa.begin();a!=aa.end();++a)
#define split(str) {vs.clear();istringstream sss(str);while(sss>>(str))vs.push_back(str);}
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))

typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VLL;
typedef vector<LD> VLD;

//#define DEBUG

int lastLen[10000];
int l[10000], D, N;
VI d(10000);

bool bReach;

void swing(int v, int p){
	if(bReach) return;

	int len = abs(d[v] - p);

	if(len <= lastLen[v]) return;
	lastLen[v] = len;

	int range = d[v] + len;
	if(D <= range){
		bReach = true;
		return;
	}

	int vS;

	for(vS = 0; vS < N && d[vS] <= range; vS++){
		if(d[vS] < p) continue;
		int dif = d[vS] - d[v];
		int newP;
		if(dif > 0){
			newP = d[vS] - l[vS];
			checkmax(newP, d[v]);
		}
		else{
			newP = d[vS] + l[vS];
			checkmin(newP, d[v]);
		}
		
		len = abs(d[vS] - newP);
		if(len <= lastLen[vS]) continue;
		swing(vS, newP);
	}
}

int main(){
	freopen("in.in", "r", stdin);
#ifndef DEBUG
	freopen("out.txt", "w", stdout);
#endif

	int t, T;
	int i, j, ii, jj;
	cin>>T;
	REP(t, T){
		cout<<"Case #"<<t+1<<": ";

		Fill(lastLen, 0);

		cin>>N;
		REP(i, N){
			cin>>d[i]>>l[i];
		}
		cin>>D;

		bReach = false;
		swing(0, 0);
		cout<<(bReach ? "YES" : "NO")<<endl;
	}
	return 0;
}
