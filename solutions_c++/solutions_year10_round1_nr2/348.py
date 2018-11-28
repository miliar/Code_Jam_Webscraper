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
#include <ctime>
using namespace std;

typedef __int64 i64; 
typedef unsigned __int64 u64;
#define I64 "%I64d"
#define U64 "%U64d"

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

int parseInts(char buff[], int a[]){
	int n = 0;
    char *p = strtok(buff," ");
    while(p!=NULL){
        sscanf(p,"%d",&a[n++]);
        p = strtok(NULL," ");
    }
	return n;
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

// char c = problem name
// int f = SAMPLE, SMALL, LARGE or TEST?
// int a = attempt, 0, 1, 2 and ..
// console or file output?
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

bool DEBUG = true;
bool CLC = false;

////////////////////////////////////////////////////////////////////////////////////////////////////////////
// END OF PREWRITTEN CODES 
////////////////////////////////////////////////////////////////////////////////////////////////////////////

#define HIGH 255
int memo[300][110][2];
int a[110];
int D, I, M, N;

int go(int cur, int nextInd, int start){
	int &ret = memo[cur][nextInd][start];
	if (-1!=ret) return ret;


	if (nextInd == N) return ret = 0;

	ret = D * N;

	int t;

	// skip
	if (start == 0 || abs(a[nextInd] - cur) <= M) {
		t = go(a[nextInd], nextInd + 1, 1);
		if (t < ret) {
			ret = t;
		}
	}

	// delete
	t = D + go(cur, nextInd + 1, start);
	if (t < ret) ret = t;

	// change
	int i;
	rep(i, HIGH + 1){
		int c = abs(i - a[nextInd]);
		if (c == 0) continue;
		t = c + go(i, nextInd + 1, 1);

		if (start == 0 || abs(cur - i) <= M);
		else continue;

		if (t < ret) {
			ret = t;
		}
	}


	// insert before
	rep(i, HIGH + 1){
		if (start == 0) continue;
		if (abs(cur - i) <= M){
			t = I + go(i, nextInd, 1);
			if (t < ret) ret = t;
		}
	}

	return ret;
}

int main (void){
    int attempt = 0;
    bool console = false;

    openFile('B', SMALL, attempt, console);

	int totalCase = INT;
    int i, j, k;

    double start = clock();
    double last = start;
    double end;

	for(int nCase = 1; nCase <= totalCase; ++nCase){
       // solution
		D = INT;
		I = INT;
		M = INT;
		N = INT;
		rep(i, N) a[i] = INT;
		memset(memo, -1, sizeof(memo));

		int res = go(0, 0, 0);
       // end of solution


        // print result
		printf("Case #%d: ",nCase);
		printf("%d", res);
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
