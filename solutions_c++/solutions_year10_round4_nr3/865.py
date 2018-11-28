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

#define min(a,b) ((a)>(b)?(b):(a))
#define max(a,b) ((a)<(b)?(b):(a))
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


set< pair<int, int> > s;
set< pair<int, int> > temp;

bool b[200][200];
bool c[200][200];
int main (void){
    int attempt = 0;
    bool console = false;

    openFile('C', SMALL, attempt, console);

	int totalCase = INT;
    int i, j, k;

    double start = clock();
    double last = start;
    double end;

	for(int nCase = 1; nCase <= totalCase; ++nCase){
       // solution
		int R = INT;

		memset(b, 0, sizeof(b));
		rep(i, R){
			int x1 = INT;
			int y1 = INT;
			int x2 = INT;
			int y2 = INT;

			for(j = x1; j <= x2; ++j){
				for(k = y1; k <= y2; ++k){
					b[j][k] = true;
				}
			}
		}


		int res = 0;
		while(true){
			res++;
			for(i = 1; i <= 100; ++i){
				for(j = 1; j <= 100; ++j){
					c[i][j] = b[i][j];

					if (b[i][j-1] == false && b[i-1][j] == false){
						c[i][j] = false;	
					}
					
					if (b[i][j-1] == true && b[i-1][j] == true){
						c[i][j] = true;
					}
				}
			}

			bool found = false;
			for(i = 1; i <= 100; ++i) for(j = 1; j <= 100; ++j) {
				b[i][j] = c[i][j];
				if(b[i][j] == true) found = true;
			}

			if (found == false) break;
		}

       // end of solution


        // print result
		printf("Case #%d: ",nCase);
        printf("%d",res);
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
