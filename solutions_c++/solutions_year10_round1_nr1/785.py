#include <iostream>
#include <string>
using namespace std;
const int N = 50;
char a[N][N], b[N][N];
bool s1, s2;
int n, k;

void init(){
    int i, j; string s;
    cin >> n >> k; s1 = false; s2 = false;
    for (i=0;i<n;i++){
        cin >> s;
        for (j=0;j<n;j++)
            a[i][j] = s[j];
    }
}

void check(int x,int y){
    if (b[x][y]=='.') return;
    int xx, yy;
    if (!s1&&b[x][y]=='R'){
        if (y+k<=n) {
            for (yy=y+1;yy<y+k&&b[x][yy]=='R';yy++);
            if (yy==y+k) s1=true;
        }
        if (!s1&&x+k<=n){
            for (xx=x+1;xx<x+k&&b[xx][y]=='R';xx++);
            if (xx==x+k) s1=true;
        }
        if (!s1&&x+k<=n&&y+k<=n){
            for (xx=x+1,yy=y+1;xx<x+k&&yy<y+k&&b[xx][yy]=='R';xx++,yy++);
            if (xx==x+k&&yy==y+k) s1=true;
        }
        if (!s1&&x+k<=n&&y-k>=-1){
            for (xx=x+1,yy=y-1;xx<x+k&&yy>y-k&&b[xx][yy]=='R';xx++,yy--);
            if (xx==x+k&&yy==y-k) s1=true;
        }
    }
    if (!s2&&b[x][y]=='B') {
        if (y+k<=n) {
            for (yy=y+1;yy<y+k&&b[x][yy]=='B';yy++);
            if (yy==y+k) s2=true;
        }
        if (!s2&&x+k<=n){
            for (xx=x+1;xx<x+k&&b[xx][y]=='B';xx++);
            if (xx==x+k) s2=true;
        }
        if (!s2&&x+k<=n&&y+k<=n){
            for (xx=x+1,yy=y+1;xx<x+k&&yy<y+k&&b[xx][yy]=='B';xx++,yy++);
            if (xx==x+k&&yy==y+k) s2=true;
        }
        if (!s2&&x+k<=n&&y-k>=-1){
            for (xx=x+1,yy=y-1;xx<x+k&&yy>y-k&&b[xx][yy]=='B';xx++,yy--);
            if (xx==x+k&&yy==y-k) s2=true;
        }
    }

}

void solve(){
    int i, j, k;
    memset(b, '.', sizeof(b));
    for (i=0;i<n;i++){
        k = n;
        for (j=n-1;j>=0;j--){
            if (a[i][j]!='.') b[--k][n-i-1] = a[i][j];
        }
    }

    for (i=0;i<n;i++){
        for (j=0;j<n;j++){
            check(i, j);
            //cout << b[i][j];
        }
        //cout << endl;
    }


}

int main(){
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int T, i;
    cin >> T;
    for (i=1;i<=T;i++){
        init(); solve();
        if (s1&&s2) printf("Case #%d: Both\n", i); else
        if (s1) printf("Case #%d: Red\n", i); else
        if (s2) printf("Case #%d: Blue\n", i); else
        printf("Case #%d: Neither\n", i);
    }
}
