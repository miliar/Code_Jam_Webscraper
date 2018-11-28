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


char board[200][200];
char myBoard[200][200];

char pieces[2] = {'B', 'R'};
bool win[2];

int main (void){
    int attempt = 0;
    bool console = false;

    openFile('A', LARGE, attempt, console);

	int totalCase = INT;
    int i, j, k;

    double start = clock();
    double last = start;
    double end;

	for(int nCase = 1; nCase <= totalCase; ++nCase){
		
		// solution
		int N = INT;
		int K = INT;
		
		rep(i, N) scanf("%s", &board[i]);

		memset(myBoard, '.', sizeof(myBoard));

		rep(i, N) {
			k = N - 1;

			for(j = N - 1; j >= 0; --j){
				if (board[i][j] != '.'){
					myBoard[i][k] = board[i][j];
					k--;
				}
			}
		}
		
		//rep(i, N) {
		//	rep(j, N) cerr<<myBoard[i][j]; cerr<<endl;
		//}

		win[0] = false;
		win[1] = false;

		int p;
		rep(p, 2){
			char c = pieces[p];

			// horizontal
			rep(i, N){
				int ct = 0;
				rep(j, N){
					if (myBoard[i][j] == c) ct++;
					else ct = 0;

					if (ct == K) win[p] = true;
				}
			}

			// vertical
			rep(j, N){
				int ct = 0;
				rep(i, N){
					if (myBoard[i][j] == c) ct ++;
					else ct = 0;

					if (ct == K) win[p] = true;
				}
			}

			// diagonal - forward
			int dx = 1;
			int dy = 1;
			rep(i, N){
				int x = i;
				int y = 0;
				
				int ct = 0;
				while(x < N && y < N){
					if (myBoard[x][y] == c) ct++;
					else ct = 0;

					if (ct == K) win[p] = true;
				
					x += dx;
					y += dy;
				}
			}

			rep(i, N){
				int x = 0;
				int y = i;

				
				int ct = 0;
				while(x < N && y < N){
					if (myBoard[x][y] == c) ct++;
					else ct = 0;

					if (ct == K) win[p] = true;

						
					x += dx;
					y += dy;
				}

			}

			dx = -1;
			dy = 1;

			rep(i, N){
				int x = i;
				int y = 0;
				
				int ct = 0;
				while(x >=0 && y < N){
					if (myBoard[x][y] == c) ct++;
					else ct = 0;

					if (ct == K) win[p] = true;
				
					x += dx;
					y += dy;
				}
			}

			rep(i, N){
				int x = N - 1;
				int y = i;

				
				int ct = 0;
				while(x >=0 && y < N){
					if (myBoard[x][y] == c) ct++;
					else ct = 0;

					if (ct == K) win[p] = true;

					
					x += dx;
					y += dy;
				}

			}


		}
		string res;
		if (win[0] == true && win[1] == true) res = "Both";
		else if (win[0] == true) res = "Blue";
		else if (win[1] == true) res = "Red";
		else res = "Neither";
       // end of solution


        // print result
		printf("Case #%d: ",nCase);
		cout<<res;
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
