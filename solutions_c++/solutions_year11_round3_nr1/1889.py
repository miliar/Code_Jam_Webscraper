#include <cstdlib>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

int main() 
{
	/*string fname = "1C-A-small-attempt0";   // for small input file at first attempt*/
    string fname = "1C-A-large";          // for large input file
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
    int T,R,C,f;
    char A[51][51];
    scanf("%d", &T);
	for (int c = 1; c <= T; ++c) 
    {
		scanf("%d %d",&R,&C);
		f=0;
		for(int d = 1 ; d <= R ; d++){
                        scanf("%s",&A[d]);
                        }

        for ( int d =1 ; d <= R ;d++){
                for(int e = 0 ; e < C ;e++){
                        if(A[d][e]=='#' && A[d+1][e]=='#' && A[d][e+1]=='#' && A[d+1][e+1]=='#') 
                        {A[d][e]='/';A[d+1][e+1]='/';A[d+1][e]='\\';A[d][e+1]='\\';}
                        if(A[d][e]=='#')
                        f++;
                        }
                }            
        printf("Case #%d:\n",c);
        if(f==0)
        for ( int d =1 ; d <= R ;d++){
                for(int e = 0 ; e < C ;e++){
                        printf("%c",A[d][e]);
                        }
                printf("\n");
                }
        else
        printf("Impossible\n");
        }
	return 0;
}
