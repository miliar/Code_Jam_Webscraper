//made by kuailezhish
//gl && hf
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <string>
#include <stack>
#include <sstream>
#include <cstring>
#include <ctime>
#define mem(a,b) memset(a,b,sizeof(a));
#define INF 0x3f3f3f3f
#define lldINF 0x3f3f3f3f3f3f3f3fll
#define eps 1e-8
#define lld long long
#define sqr(x) ((x)*(x))
#define ab(x) (((x)>0) ? (x) : -(x))
#define PI 3.14159265358979323846
#define psl pair<sting,lld>
#define pll pair<lld,lld>
#define pii pair<int,int>
#define MP make_pair
#define er(i) (1ll<<(i))
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define rin freopen("in.txt","r",stdin)
#define pout freopen("out.txt","w",stdout)
#pragma comment(linker, "/STACK:102400000,102400000")
using std::bitset;
using namespace std;

int d1[4][4]={{3,2,1,0},{0,1,2,3},{0,0,0,0},{0,1,2,3}};
int d2[4][4]={{-3,-2,-1,0},{0,1,2,3},{0,1,2,3},{0,0,0,0}};

int a[5][5];
int n=4,ans;

int getint(char ch){
    if (ch=='.') return 0;
    if (ch=='O') return 1;
    if (ch=='X') return 2;
    if (ch=='T') return 3;
}

int find(int x,int y,int k,int flag){
    int i,j,tem,num=0,cnt=0;
    for (i=0; i<4; i++){
        int dx,dy;
        dx=x+d1[k][i];
        dy=y+d2[k][i];
        if (1<=dx && dx<=4 && 1<=dy && dy<=4){
            if (a[dx][dy]==flag) num++;
            else if (a[dx][dy]==3) cnt++;
        }
    }
    return (num==4) || (num==3 && cnt==1);
}

int judge(int flag){
    int i,j,tem;
    for (i=1; i<=n; i++)
        for (j=1; j<=n; j++)
            for (int k=0; k<4; k++)
                if (find(i,j,k,flag)) return 1;
    return 0;
}

int main(){
    int i,j,tem,T,cas=0;
    char st[2];
freopen("A-large.in","r",stdin);
pout;

    scanf("%d",&T);
    while (T--){
        for (i=1; i<=n; i++)
            for (j=1; j<=n; j++){
                scanf("%1s",st);
                a[i][j]=getint(st[0]);
            }
        ans=0;
        if (judge(1)) ans=1;
        else if (judge(2)) ans=2;
        else {
            int num1,num2,num3;
            num1=num2=num3=0;
            for (i=1; i<=n; i++)
                for (j=1; j<=n; j++)
                    if (a[i][j]==1) num1++;
                    else if (a[i][j]==2) num2++;
                    else if (a[i][j]==3) num3++;
            if (num1+num2+num3==16) ans=3;
        }
        if (ans==0) printf("Case #%d: Game has not completed\n",++cas);
        else if (ans==1) printf("Case #%d: O won\n",++cas);
        else if (ans==2) printf("Case #%d: X won\n",++cas);
        else printf("Case #%d: Draw\n",++cas);
    }
    return 0;
}

























