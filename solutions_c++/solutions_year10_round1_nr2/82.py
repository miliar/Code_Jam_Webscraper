#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

const int INF=1000000;

int D,I,M,N;

int vals[1000];

int dp[101][256];

int abs(int val) {
    if(val>=0) return val;
    else return -val;
}

int myCost(int a, int b) {
    if(a==b) return 0;
    if(M==0) return INF;
    return ((abs(a-b)-1) / M) * I;
}


int solve(int pos, int lastval) {
    if(pos==N) return 0;
    int &ret=dp[pos][lastval];
    if(ret!=-1) return ret;
    ret=INF;
    //try skipping this pixel
    ret=solve(pos+1,lastval) + D;
    for(int i=0;i<256;i++) {
        int res=solve(pos+1,i) + myCost(lastval, i) + abs(vals[pos] - i);
        ret=min(res,ret);
    }
    return ret;
}

int solve() {
    int ret=INF;
    for(int i=0;i<256;i++) {
        for(int j=0;j<N;j++) {
            int res=solve(j+1,i) + abs(vals[j]-i) + j * D;
            ret=min(ret,res);
        }
    }
    return ret;
}

int main() {
    int cases;
    cin>>cases;
    for(int c=1;c<=cases;c++) {
        cin>>D>>I>>M>>N;
        for(int i=0;i<N;i++) cin>>vals[i];
        memset(dp,-1,sizeof(dp));
        cout<<"Case #"<<c<<": "<<solve()<<endl;
    }
}
