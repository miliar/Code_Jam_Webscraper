#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <climits>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#define REP(i,n) for( int (i)=0;(i)<(int)(n);(i)++)
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
LL LLMAX = 9223372036854775807LL;
const int MOD = 1000000007;
const int maxn = 1000+10;
char G[4][5];
int main()
{
#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
    int T;
    scanf("%d%*c",&T);
    for(int kase = 1;kase<=T;++kase){
        bool em = false;
        bool ok = false;
        for(int i=0;i<4;++i)gets(G[i]);scanf("%*c");
        //REP(i,4)puts(G[i]);
        for(int i=0;i<4;++i){
            int c1=0,c2=0;
            for(int j=0;j<4;++j)
                if(G[i][j] == 'O')c1++;
                else if(G[i][j]=='X')c2++;
                else if(G[i][j] == 'T'){c1++;c2++;}
                else em = true;
            if(c1 == 4){
                printf("Case #%d: O won\n",kase);
                ok = 1;
            }
            else if(c2 == 4){
                printf("Case #%d: X won\n",kase);
                ok = 1;
            }else;
        }
        if(ok)continue;
        for(int i=0;i<4;++i){
            int c1=0,c2=0;
            for(int j=0;j<4;++j)
                if(G[j][i] == 'O')c1++;
                else if(G[j][i]=='X')c2++;
                else if(G[j][i] == 'T'){c1++;c2++;}
                else em = true;
            if(c1 == 4){
                printf("Case #%d: O won\n",kase);
                ok = 1;
            }
            else if(c2 == 4){
                printf("Case #%d: X won\n",kase);
                ok = 1;
            }else;
        }
        if(ok)continue;
        int c1=0,c2=0;
        for(int i=0;i<4;++i){
                if(G[i][i] == 'O')c1++;
                else if(G[i][i]=='X')c2++;
                else if(G[i][i] == 'T'){c1++;c2++;}
                else em = true;
        }
        if(c1 == 4){
                printf("Case #%d: O won\n",kase);
                ok = 1;
        }
        else if(c2 == 4){
                printf("Case #%d: X won\n",kase);
                ok = 1;
        }else;
        if(ok)continue;
        c1=0,c2=0;
        for(int i=0;i<4;++i){
                if(G[i][3-i] == 'O')c1++;
                else if(G[i][3-i]=='X')c2++;
                else if(G[i][3-i] == 'T'){c1++;c2++;}
                else em = true;
        }
        if(c1 == 4){
                printf("Case #%d: O won\n",kase);
                ok = 1;
        }
        else if(c2 == 4){
                printf("Case #%d: X won\n",kase);
                ok = 1;
        }else;
        if(ok)continue;
        if(em)printf("Case #%d: Game has not completed\n",kase);
        else printf("Case #%d: Draw\n",kase);

    }
}
