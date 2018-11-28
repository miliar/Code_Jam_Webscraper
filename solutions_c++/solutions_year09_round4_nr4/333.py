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
bool CLC = false;

#define SIZE 50

int X[SIZE];
int Y[SIZE];
int R[SIZE];

double dist(int x1, int y1, int x2, int y2){
    return sqrt(sq(x1-x2) + sq(y1-y2));
}

int main (void){
    openFile('D', SMALL, 0, false);

	int totalCase = INT;
    int i, j, k;

    double start = clock();
    double last = start;
    double end;

	for(int nCase = 1; nCase <= totalCase; ++nCase){
       // solution

        int N = INT;

       // end of solution
        rep(i, N){
            X[i] = INT;
            Y[i] = INT;
            R[i] = INT;
        }
        
        double res;

        if (N==1){
            res = R[0];
        }
        else if(N==2){
            res = max(R[0], R[1]);
        }
        else{
            int u = 0;
            int v = 1;
            int w = 2;

            double r1 = dist(X[u], Y[u], X[v], Y[v]) + R[u] + R[v];
            r1/=2;

            double r2 = R[w];

            double r = max(r1, r2);

            res = r;


            u = 0;
            v = 2;
            w = 1;

            r1 = dist(X[u], Y[u], X[v], Y[v]) + R[u] + R[v];
            r1/=2;

            r2 = R[w];

            r = max(r1, r2);

            res = min(r, res);

            u = 1;
            v = 2;
            w = 0;

            r1 = dist(X[u], Y[u], X[v], Y[v]) + R[u] + R[v];
            r1/=2;

            r2 = R[w];

            r = max(r1, r2);

            res = min(r, res);
        }

        // print result
		printf("Case #%d: ",nCase);
        printf("%.10lf",res);
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
