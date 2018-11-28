#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int n;

int memo[105][105][105];
char who[105];
int pos[105];
const int INF = 1000000000;


int f(int a, int b, int k) { //a,b robot position, k order index
    if (k==n) return 0;
    int &ans = memo[a][b][k];
    if (ans>=0) return ans;
    ans=INF;
    if (who[k]=='O') {
        int r = abs(pos[k]-a)+1; //anar i apretar
        for (int i=-r;i<=r;++i) if (b+i>=1 and b+i<=100) 
            ans=min(ans,r+f(pos[k],b+i,k+1));
    }
    else {
        int r = abs(pos[k]-b)+1; //anar i apretar
        for (int i=-r;i<=r;++i) if (a+i>=1 and a+i<=100) 
            ans=min(ans,r+f(a+i,pos[k],k+1));
    }
    return ans;
}

int main() {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        memset(memo,-1,sizeof(memo));
        cin >> n;
        for (int i=0;i<n;++i) cin >> who[i] >> pos[i];
        cout << "Case #" << cas << ": " << f(1,1,0) << endl;
    }
}
