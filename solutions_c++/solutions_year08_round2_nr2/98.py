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
using namespace std;

#define pb push_back
#define mp make_pair
#define pii pair<int,int>

#define fo(i,n) for(int i=0; i < (n) ; ++i)
#define FO(i,a,b) for(int i=a;i<=(b);++i)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define UNIQ(v) (v).erase(unique(ALL(v)),(v).end())

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
				     
const char eof = -123;

void printBits(unsigned int x,int end = 32,int start = 0){for(int i = end-1;i>=start;i--) if(x & (1<<i)) cout<<1<<" "; else cout<<0<<" ";}
int readInt(){	int x;if(scanf("%d",&x) != 1) return eof;return x;}
char readChar() { char c; if(scanf("%c",&c) != 1) return eof; return c;}
lint readLL(){lint x; if(cin>>x) return x; return eof;}
double readDouble(){double f;if(scanf("%lf",&f) == 1)return f;return eof;}

const int MAX = 1000000;
bool comp[MAX+10];
VI primes;

VI v[MAX+10];

void init()
{
	for(int i=2;i<=MAX;i++) if(!comp[i]){
		primes.pb(i);
		for(lint j = (lint)i*i;j <= MAX; j+=i)
			comp[j] = 1;
	}
/*
	for(int i=2;i<=MAX;i++){
		int k = i;
		for(int j=2;j*j<=i;j++) if(!comp[j]){
			if(k%j) continue;
			v[i].pb(j);
			while(k%j == 0) k /= j;
		}
		if(k > 1) v[i].pb(k);
	}
*/
}

int parent[MAX+10];

int findset(int x)
{
	if(x == parent[x]) return x;
	return parent[x] = findset(parent[x]);
}

void unite(int x, int y)
{
	int a = findset(x);
	int b = findset(y);
	if(a != b) {
		parent[b] = a;
	}
}
main()
{
	init();
	int cases = readInt();
	int tc = 0;
	lint A, B, P;
	while(cases--){
		++tc;
		printf("Case #%d: ",tc);
		cin>>A>>B>>P;
		for(lint i=A;i<=B;i++) parent[i-A] = i-A;
		if(P > primes.back()){
			cout<<B-A+1<<endl;
			continue;
		}
		int x = lower_bound(primes.begin(),primes.end(), P) - primes.begin();
		for(int i=x;i<primes.size();i++){
			lint p = primes[i];
			lint start = A + (p - A%p)%p;
			if(p > B - A) break;
			while(start <= B){
				if(start + p <= B) unite(start-A, start+p-A);
				start += p;
			}
		}
		int ret = 0;
		for(lint i=A;i<=B;i++) if(parent[i-A] == i-A) ret++;
		cout<<ret<<endl;
	}
}

