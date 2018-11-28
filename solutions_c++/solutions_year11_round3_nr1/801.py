#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <algorithm>
#include <functional>
using namespace std;

#define INF (1LL<<31)-1
#define PI 2*acos(0.0)
#define FOR(i,n) for(int i = 0;i<n;++i)
#define setbit(a,b) a|=(1<<b)
#define S1(a) scanf("%d",&a)
#define S2(a,b) scanf("%d %d",&a,&b)
#define S3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define C1(a) __builtin_popcount(a)
#define gcd(a,b) __gcd(a,b)
#define ALL(a) (a.begin(),a.end())

typedef long long LL;
typedef vector<string> vs;
typedef vector<int> vi;

int main(){

    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);

    int t,ca = 0;
    scanf("%d",&t);
    while(t--){

        int R,C;
        scanf("%d %d",&R,&C);
        vector< string > grid;
        char inpt[55];
        for(int i = 0;i<R;++i){
            scanf("%s",inpt);
            grid.push_back( inpt );
        }
        bool success = true;
        bool done[ 55 ][ 55 ] = {0};
        for(int i = 0;i<R;++i)
            for(int  j = 0;j<C;++j)
                if(grid[i][j]=='#'&&!done[i][j]){

                    if( i < grid.size()-1 && j < grid[i].size()-1 && grid[i+1][j]=='#' && grid[i][j+1]=='#' && grid[i+1][j+1]=='#'){

                        grid[i+1][j]= grid[i][j+1]= '\\';grid[i+1][j+1]= grid[i][j] = '/';
                        done[i+1][j]= done[i][j+1]= done[i+1][j+1]= done[i][j] = 1;
                    }
                    else success = false;

                }
        printf("Case #%d:\n",++ca);
        if( !success )puts("Impossible");
        else
            for(int i = 0;i<R;++i)printf("%s\n",grid[i].c_str());

    }

    return 0;
}
