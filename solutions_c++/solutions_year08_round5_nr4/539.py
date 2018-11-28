#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <sstream>
using namespace std;
#define For(i,a,b)  for(int i=a;i<=b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define PB push_back
#define PoB pop_back
#define MP make_pair
#define fillchar(a) memset(a, 0, sizeof(a))
#define eps 1e-8
#define Long long long

#define maxn 110
int H,W,R, a[maxn][maxn];

int main(){
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int ntest;
    cin>>ntest;
    For(test,1,ntest){
        cin>>H>>W>>R;
        fillchar(a);        
        For(i,1,R) {
            int u,v;
            cin>>u>>v;
            a[u][v]=-1;
        }
        a[1][1]=1;
        For(i,1,H)
        For(j,1,W) if (a[i][j]>0){
            if (a[i+2][j+1]!=-1) a[i+2][j+1]=(a[i+2][j+1]+a[i][j])%10007;
            if (a[i+1][j+2]!=-1) a[i+1][j+2]=(a[i+1][j+2]+a[i][j])%10007;
        }
        if (a[H][W]==-1) a[H][W]=0;
        cout<<"Case #"<<test<<": "<<a[H][W]<<endl;
    }
    return 0;
}
