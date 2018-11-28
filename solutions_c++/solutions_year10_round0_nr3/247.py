#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <bitset>
#include <cmath>
#include <sstream>
#include <complex>
#include <cassert>
using namespace std;

#define pb push_back
#define mp make_pair

#define fo(i,n) for(int i=0; i < (n) ; ++i)
#define FO(i,a,b) for(int i=a;i<=(b);++i)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define UNIQ(v) (v).erase(unique(ALL(v)),(v).end())

#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define VDebug(x)  {fo(i,(x).size()) cout<<(x)[i]<<" ";cout<<endl;}
#define VVDebug(x) {fo(j,(x).size()) VDebug(x[j])}
				     
typedef istringstream iss;
typedef ostringstream oss;
typedef long long int lint;
typedef complex<double> point;
				     
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<VS> VVS;
typedef pair<int,int> pii;

const char eof = -123;

void printBits(unsigned int x,int end = 32,int start = 0){for(int i = end-1;i>=start;i--) if(x & (1<<i)) cout<<1<<" "; else cout<<0<<" ";}
int readInt(){	int x;if(scanf("%d",&x) != 1) return eof;return x;}
char readChar() { char c; if(scanf("%c",&c) != 1) return eof; return c;}
lint readLL(){lint x; if(cin>>x) return x; return eof;}
double readDouble(){double f;if(scanf("%lf",&f) == 1)return f;return eof;}

void init(){
}

lint v[1001];
lint sum[1001];
int seen[1000];

void solve(int testCase){
	int r = readInt();
	lint capacity = readInt();
	int n = readInt();
	fo(i,n) v[i] = readInt();
	lint tSum  = 0; fo(i,n) tSum += v[i];
	if(capacity > tSum) capacity = tSum;
	memset(seen,-1,sizeof(seen));
	
	lint ret = 0;
	int pos = 0;
	for(int ride=0;ride<r;++ride){
		if(seen[pos] != -1){
			lint cycleLength = ride - seen[pos];
			lint cycleSum = sum[ride] - sum[seen[pos]];
			ret += (r - ride)/cycleLength * cycleSum;
			lint remaining = (r-ride)%cycleLength;
			ret += sum[seen[pos]+remaining] - sum[seen[pos]];
			break;
		}

		seen[pos] = ride;
		lint cSum = 0;
		while(cSum + v[pos] <= capacity){
			cSum += v[pos];
			pos = (pos+1)%n;
		}
		sum[ride+1] = sum[ride] + cSum;
		ret += cSum;
	}
	assert(ret >= 0);
	cout<<ret<<endl;
}

main()
{
	init();
	int cases = readInt();
	int tc = 0;
	while(cases--){
		tc++;
		printf("Case #%d: ",tc);
		solve(tc);
	}
}

