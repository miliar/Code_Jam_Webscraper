#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <deque>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <valarray>
#include <iterator>
using namespace std;

typedef long long int lli;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef unsigned long long ull;

#define REP(i,x) for(int i=0;i<(int)(x);i++)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();i++)
#define RREP(i,x) for(int i=(x);i>=0;i--)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();i++)

int dx[4]={-1,0,1,0},dy[4]={0,-1,0,1}; //ç∂ è„ âE â∫

const int INF=0x20000000;
const double EPS=1e-8;

int N;
int d[11111];
int D;
int l[11111];

int m[11111];
void solve(){
	memset(m,0,sizeof(m));
	// Ç∆ÇËÇ†Ç¶Ç∏ç≈èâ
	m[0]=d[0];
	d[N]=D;
	for(int i=0;i<N;i++){
		if(m[i]+d[i]>=D){
			cout<<"YES"<<endl;
			return;
		}
		int movement=upper_bound(d,d+N,m[i]+d[i])-d;
		for(int j=i+1;j<movement;j++){
			m[j]=max(m[j],min(l[j],d[j]-d[i]));
		}
	}
	cout<<"NO"<<endl;
}
int main(){
	int TestCaseCount;
	cin>>TestCaseCount;
	for(int tc=1;tc<=TestCaseCount;tc++){
		cin>>N;
		for(int i=0;i<N;i++){
			cin>>d[i]>>l[i];
		}
		cin>>D;

		cout<<"Case "<<"#"<<tc<<": ";
		solve();
	}
}
