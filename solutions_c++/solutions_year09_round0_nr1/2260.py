#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <float.h>

using namespace std;

// prewritten code

#define sz(x) (int)(x).size()
#define all(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define pb push_back

#define GDB 1
#define DBG(x) if(GDB){cerr << #x <<" = "<< x << endl;}
#define DBGA(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cerr<<x[i]<<' '; cerr<<endl;}
#define DBGV(x) if(GDB){cerr << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cerr<<x[i]<<' '; cerr<<endl;}

// real code
string problem_name="a";
void init(){
    freopen( (problem_name+".in").c_str(),"rt",stdin);
    freopen( (problem_name+".out").c_str(),"wt",stdout);
}
#define MAXL 17
#define MAXD 50010
int N,L,D;

long long book[MAXD][MAXL];
long long lex[MAXL];
int main(){
    init();
    int i,j;
    int ret=0;
    char c;
    int k;
    int good;
    for(i=0;i<MAXD;i++) for(j=0;j<MAXL;j++) book[i][j]=0;
    scanf("%d %d %d\n",&L,&D,&N);
    for(i=0;i<D;i++){
        for(j=0;j<L;j++){
            c=getchar();
            book[i][j]=(1<<(int(c-'a')));
        }
        getchar();
    }
    for(k=1;k<=N;k++){
        good=1;
        ret=0;
        for(j=0;j<L;j++){
            lex[j]=0;
            c=getchar();
            if(c=='('){
                //c=getchar();
                for(i=0;((c=getchar())!=')');i++) lex[j]|=(1<<(c-'a'));
            }else{
                lex[j]|=(1<<(int(c-'a')));
            }
        }
        //DBGA(lex);
        getchar();
        for(i=0;i<D;i++){
            good=1;
            for(j=0;j<L;j++){
                if((lex[j]&book[i][j])==0) good=0;
            }
            if(good) ret++;
        }
        printf("Case #%d: %d\n",k,ret);
    }
    return 0;
}
