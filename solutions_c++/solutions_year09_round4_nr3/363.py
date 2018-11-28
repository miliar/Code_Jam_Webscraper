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


#define dbg(x) if(DEBUG) cerr << __LINE__ << ": " << #x << " -> " << (x) << "\t";
#define dbge(x) if(DEBUG) cerr << __LINE__ << ": "<<#x << " -> " << (x) << endl;

#define CLR(c, v) memset(c, v, sizeof(c))

vector<string> Tokenize(string s, string ch) {
  vector<string> ret;
  for (int p = 0, p2; p < s.size(); p = p2+1) {
    p2 = s.find_first_of(ch, p);
    if (p2 == -1) p2 = s.size();
    if (p2-p > 0) ret.push_back(s.substr(p, p2-p));
  }
  return ret;
}

vector<int> TokenizeInt(string s, string ch) {
  vector<int> ret;
  vector<string> p = Tokenize(s, ch);
  for( int i = 0; i < p.size(); i++ )
    ret.push_back(atoi(p[i].c_str()));
  return ret;
}

vector<vector<int> > TokenizeMatrix(vector<string> s, string ch) {
  vector<vector<int> > ret;
  for( int i = 0; i < s.size(); i++ )
    ret.push_back( TokenizeInt(s[i], ch) );
  return ret;
}

int getInt(void){
	int d;
	scanf("%d",&d);
	return d;
}
#define INT getInt()

double getDouble(void){
    double d;
    scanf("%lf", &d);
    return d;
}
#define DOUB getDouble()

char InputFileNames[4][30] = {"A-sample.in", "A-small-attempt0.in", "A-large.in", "A-test.in"};
char OutputFileNames[4][30] = {"A-sample.out", "A-small-attempt0.out", "A-large.out", "A-test.out"};

enum{SAMPLE=0, SMALL, LARGE, TEST};

void openFile(char c, int f, int a, bool console){
    if (f==SMALL){
        int len = strlen(InputFileNames[f]);
        InputFileNames[f][len-4] = '0' + a;
        OutputFileNames[f][len-4] = '0' + a;
    }

    InputFileNames[f][0] = c;
    OutputFileNames[f][0] = c;

    freopen(InputFileNames[f], "r", stdin);
    if(console == false) freopen(OutputFileNames[f], "w", stdout);
}

bool DEBUG = false;
bool CLC = true;

#define SIZE 101

int N, K;
int adj[SIZE][SIZE];

int chart[SIZE][30];
int cind[SIZE];

void comp(int u, int v){
    int i;

    bool valid = true;
    rep(i, K){
        if(chart[u][i] <= chart[v][i]) valid = false;

        //if(u==1 && v==2)cout<<"-- "<<chart[u][i] << " "<<chart[v][i]<<endl;
    }

    if(valid == true){
        adj[u][v] = 1;
        return;
    }

    valid = true;
    rep(i, K){
        if(chart[u][i] >= chart[v][i]) valid = false;
    }

    if(valid == true){
        adj[u][v] = -1;
        return;
    }

    adj[u][v] = 0;
    return;
}


int memo[1<<16];
bool vstate[1<<16];

void checkValid(int state){
    vector<int> v;
    v.clear();

    int i, j;
    
    vstate[state] = false;

    rep(i, N) if(state &(1<<i) ){
        rep(j, N) if(state & (1<<j) ){
            if(i==j)continue;
        
            if( adj[i][j] == 0) return;
        }
    }

    vstate[state] = true;
}

int go(int state){
    int &ret = memo[state];
    if(-1!=ret)return ret;

    if (state == 0)return ret = 0;

    int a=state;
    ret = N + 1;

    while(a){
        //doSomethingWith(a);
        if (vstate[a] == true){
            int temp = 1 + go(state - a);
            ret = min(temp, ret);
        }
        --a;
        a&=state;
    }

    return ret;
}


int main (void){
    openFile('C', SMALL, 0, false);

	int totalCase = INT;
    int i, j, k;

    double start = clock();
    double last = start;
    double end;

	for(int nCase = 1; nCase <= totalCase; ++nCase){
       // solution
        N = INT;
        K = INT;
        rep(i, N){
            rep(j, K) chart[i][j] = INT;
        }

        rep(i, N)rep(j, N)comp(i, j);

        //rep(i, N){
        //    rep(j, N)cout<<adj[i][j]<<"\t";
        //    cout<<endl;
        //}

        /*
        rep(i, N) cind[i] = i;

        rep(i, N + 1){
            rep(j, N-1){
                if(adj[ind[j]][ind[j+1]] > 0){
                    std::swap(ind[j], ind[j+1]);
                }
            }
        }
        */
        
        for(i=0; i < (1<<N); ++i){
            checkValid(i);
            dbg(i); dbge(vstate[i]);
        }

        

        memset(memo, -1, sizeof(memo));
       // end of solution


        // print result
		printf("Case #%d: ",nCase);
        cout<<go( (1<<N) - 1);
        printf("\n");

        //time
        end = clock();
        if (CLC) {
            fprintf(stderr, "[--- Case #%4d: %5.2lf ---]\n", nCase, (end-last)/CLOCKS_PER_SEC);
        }
        last = end;
	}

    end = clock();
    fprintf(stderr, "Total time: %lf\n", (end-start)/CLOCKS_PER_SEC);

	return 0;
}
