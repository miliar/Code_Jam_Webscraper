#pragma warning( disable : 4786 )
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <queue>
#include <cstring>
using namespace std;

typedef long long i64; 
typedef unsigned long long u64;
#define I64 "%lld"
#define U64 "%llu"

#define mabs(x) ((x)<0?(-(x)):(x))
#define mmin(a,b) ((a)>(b)?(b):(a))
#define mmax(a,b) ((a)<(b)?(b):(a))
#define sq(x) ((x)*(x))

#define EPS 1e-7

#define eq(a,b) (a - b < EPS && b - a < EPS) 
#define les(a, b) (b - a > EPS) 

typedef vector<int> VI; 

#define rep(i,n) for((i)=0;(i)<(n);++(i))

#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),c) != (c).end()) 

#define FOR(v, it) for(it = v.begin(); it!=v.end(); ++it)
#define foreach(vtype, v, it) for(vtype::iterator it = v.begin(); it!=v.end(); ++it)

// tostring
string itos (int i){ stringstream s; s << i; return s.str(); }
string i64tos (i64 i){ char s[51];sprintf(s,I64,i);string ss=s;return ss; }

template <class T>
void SWAP(T &x, T &y){T z=x; x=y; y=z;}

#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << endl;

#define CLR(c, v) memset(c, v, sizeof(c))

int getInt(void){
	int d;
	scanf("%d",&d);
	return d;
}
#define INT getInt()

char InputFileNames[4][20] = {"A-sample.in", "A-small.in", "A-large.in", "A-test.in"};
char OutputFileNames[4][20] = {"A-sample.out", "A-small.out", "A-large.out", "A-test.out"};

enum{SAMPLE=0, SMALL, LARGE, TEST};


char buff[1000];
#define SIZE 2000
bool vis[SIZE];
int t;

int calc(int val, int base){
    int res = 0;
    while(val){
        res += sq(val%base);
        val/=base;
    }
    return res;
}

bool isHappy(int val, int base){
    assert(val<SIZE);
    if(vis[val]==true)return false;
    else vis[val]=true;

    if(val==1)return true;

    int nval = calc(val, base);
    return isHappy(nval, base);
}

int main (void){
	int CUR = SMALL;
	freopen(InputFileNames[CUR], "r", stdin);
	freopen(OutputFileNames[CUR], "w", stdout);

    gets(buff);
	int T = atoi(buff);
    
	for(t=1; t<=T; ++t){
        int res = -1;
        gets(buff);
        string s(buff);
        stringstream sin(s);
        
        vector<int> v;
        v.clear();

        int a;
        while(sin>>a){
            v.push_back(a);
        }
        
        for(int i=2; ;++i){
            int j;
            
            for(j=0; j<v.size(); ++j){

            int val = i;
            while(val>=SIZE){
                val = calc(val, v[j]);
            }
                
                
                memset(vis, 0, sizeof(vis));
                if(isHappy(val, v[j])==false)break;
            }

            if(j==v.size()){
                res = i;
                break;
            }
        }

		printf("Case #%d: %d\n",t,res);
	}

	return 0;
}
