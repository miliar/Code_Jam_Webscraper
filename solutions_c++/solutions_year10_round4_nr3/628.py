#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll long long int
#define uli unsigned long long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("C-small-attempt0.in");
//A-small-attempt0.in
#define cin fin
ofstream fout ("C-small.out");
#define cout fout
bool ok(int a[101][101]) {
 REP(i,100)REP(j,100) if(a[i][j]==1) return false;
 return true;
}
bool north(int i,int j,int a[101][101]) {
	if(i<=0) return false;
	return a[i-1][j];
}
bool west(int i,int j,int a[101][101]) {
	if(j<=0) return false;
	return a[i][j-1];
}
int main() {
	int t=0;
	cin>>t;
	REP(T,t) {
		int R;
		cin>>R;
		int a[101][101],b[101][101];
		REP(i,100)REP(j,100) a[i][j]=0;
		REP(i,R) {
			int x1,x2,y2,y1;
			cin>>x1>>y1>>x2>>y2;
			FOR(x,x1,x2+1)
			FOR(y,y1,y2+1) a[x-1][y-1]=1;
		}
		int cnt=0;
		while(1) {
			if(ok(a)) break;
			cnt++;
			REP(i,100)
				REP(j,100)
					if(north(i,j,a) && west(i,j,a)) b[i][j]=1;
					else if(north(i,j,a) || west(i,j,a)) b[i][j]=a[i][j];
					else b[i][j]=0;
			REP(i,100)
				REP(j,100) a[i][j]=b[i][j];
		}
		cout<<"Case #"<<T+1<<": "<<cnt<<endl;
	}
	return 0;
}
