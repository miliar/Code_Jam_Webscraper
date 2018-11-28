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

void globalInit();
void tcInit();
void tcEnd();

//////////// START HERE ///////////

const int MAXH = 100, MAXW = 100;

int m, n;
int h[MAXH][MAXW];
int p[MAXH * MAXW];
int sink[MAXH*MAXW];
char label[MAXH*MAXW];

void globalInit(){
}

void tcInit(){
	m = readInt();
	n = readInt();
	fo(i,m)fo(j,n) h[i][j] = readInt();
	fo(i,m)fo(j,n) p[i*n + j] = i*n + j;
	memset(sink,0,sizeof(sink));
	memset(label,-1,sizeof(label));
}

/////////// INIT BLOCKS END ///////
int findset(int x){
	return (x==p[x]) ? x: findset(p[x]);
}
void unite(int x,int y){
	int a = findset(x);
	int b = findset(y);
	if(sink[a]) p[b] = a;
	else p[a] = b;
}

void assignLabels(){
	char next = 'a';
	fo(i,(m*n)){
		int j = findset(i);
		if(label[j] == -1){
			label[j] = next++;
		}
		label[i] = label[j];
	}
}
void printLabels(){
	fo(i,m){
		fo(j,n){
			if(j) printf(" ");
			printf("%c",label[i*n+j]);
		}
		printf("\n");
	}
}
void solve(){
	int dx [] = {-1,0,0,1};
	int dy [] = {0,-1,1,0};
	fo(rnd,2){
		fo(i,m)fo(j,n){
			int least = 10000000;
			int cand = -1;
			fo(k,4){
				int I = i + dx[k], J = j + dy[k];
				if(I < 0 || I >= m || J < 0 || J >=n) continue;
				if(h[I][J] < least){
					least = h[I][J];
					cand = k;
				}
			}
			if(least >= h[i][j]) sink[i*n+j] = 1;
			else if(rnd ==1) unite( (i + dx[cand])*n + (j + dy[cand]), i*n+j);
		}
	}
	assignLabels();
	printLabels();
}


main()
{
	globalInit();
	int cases = readInt();
	int tc = 0;
	while(cases--){
		tc++;
		printf("Case #%d:\n",tc);
		tcInit();
		solve();
		tcEnd();
	}
}

void tcEnd(){
}


