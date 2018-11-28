/***************************************************
 * Author: Alexandru Palcuie
 * Country: Romania
 * Contest: Google Codejam 2011
 * Email: alex [dot] palcuie [at] gmail [dot] com
 * Website: http://palcu.blogspot.com/
 * Year: 2011
****************************************************/

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cstring>

using namespace std;

typedef vector<int> VI;
typedef vector<pair<int,int> > VPI;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

//Constants
const int N = 50;

//Global Vars

//Structs

//Solve Functions
void debug_matrix(char m[N][N], int x, int y){
        int i,j;
        for(i=0;i<x;++i){
                for(j=0;j<y;++j)
                        printf("%c",m[i][j]);
                printf("\n");
        }
}

void solve(){
        char m[N][N];
        memset(m,0,sizeof(m));
        bool isBlue;
        int i,j,x,y;
        scanf("%d %d\n",&x,&y);

        for(i=0;i<x;++i){
                for(j=0;j<y;++j){
                        scanf("%c ",&m[i][j]);
                        if (m[i][j] == '#')
                                isBlue = true;
                }
                scanf("\n");
        }

        if (isBlue == false){
                debug_matrix(m,x,y);
        }

        for(i=0;i<x;++i){
                for(j=0;j<y;++j){
                        if (m[i][j] == '#'){
                                if (i+1<x && j+1<y && m[i+1][j]=='#' && m[i][j+1]=='#' && m[i+1][j+1]=='#'){
                                        m[i][j] = '/';
                                        m[i+1][j] = '\\';
                                        m[i][j+1] = '\\';
                                        m[i+1][j+1] = '/';
                                }
                                else{
                                        printf("Impossible\n");
                                        return;
                                }
                        }
                }
        }
        debug_matrix(m,x,y);
        return;
}

int main()
{
        #ifndef ONLINE_JUDGE
        freopen("codejam.in","r",stdin);
        freopen("codejam.out","w",stdout);
        #endif

        int n; scanf("%d",&n);
        for(int i=1;i<=n;++i){
                printf("Case #%d:\n",i);
                solve();
        }

        return 0;
}
