#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <utility>

using namespace std;
//using namespace __gnu_cxx;

typedef long long ll;
typedef double db;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef istringstream is;
typedef ostringstream os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);--(i))
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();++(i))
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define PRINT(v) for(int (i)=0;(i)<(int)(v).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;

int **tab, **tab2;

void run(int cnum){

    REP(i,101){
        REP(j,101){
            tab[i][j] = 0;
            tab2[i][j] = 0;
        }
    }


    int r;
    scanf("%d", &r);
    int sum = 0;
    int maxx=0,maxy=0;
    REP(i,r){
        int x1,y1,x2,y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        FUP(j,x1,x2) FUP(k,y1,y2)
            if(tab[j][k] == 0){ tab[j][k] = 1; sum++; }
        maxx = max(maxx, x2);
        maxy = max(maxy, y2);
    }

    int t = 0;
    while(sum){
        FUP(i,1,maxx) FUP(j,1,maxy)
            if(tab[i][j] == 1){
                if(tab[i-1][j] == 0 && tab[i][j-1] == 0){
                    tab2[i][j] = 0;
                    sum--;
                }
                else tab2[i][j] = 1;
            }
            else{
                if(tab[i-1][j] == 1 && tab[i][j-1] == 1){
                    sum++;
                    tab2[i][j] = 1;
                }
                else tab2[i][j] = 0;
            }
        swap(tab,tab2);
        t++;
    }
    printf("Case #%d: %d\n", cnum, t);
}

int main(){
    tab = new int*[101];
    tab2 = new int*[101];
    REP(i,101){
        tab[i] = new int[101];
        tab2[i] = new int[101];
        REP(j,101){
            tab[i][j] = 0;
            tab2[i][j] = 0;
        }
    }

    int C;
    scanf("%d", &C);
    REP(i,C) run(i+1);
    return 0;
}


