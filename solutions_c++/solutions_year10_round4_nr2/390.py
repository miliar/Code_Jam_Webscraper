#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

#define llong long long

const int MAX=2*1024;
const llong INF=1LL<<50;


int needed[MAX];
int cost[MAX][MAX];
int p;

llong dp[MAX][MAX][11];

llong solve(int start, int end, int gotten) {
    if(start==end)
        return (gotten>=needed[start])?0:INF;
    llong &ret=dp[start][end][gotten];
    if(ret!=-1) return ret;
    ret=INF;
    int range=(end-start+1)/2;
    //dont use it
    ret=min(ret,solve(start,start+range-1,gotten)+solve(start+range,end,gotten));
    //use it
    ret=min(ret,solve(start,start+range-1,gotten+1)+solve(start+range,end,gotten+1)+cost[start][end]);
    return ret;
}

llong solve() {
    cin>>p;
    for(int i=0;i<(1<<p);i++) {
        cin>>needed[i];
        needed[i]=p-needed[i];
    }
    int price;
    int range=2;
    for(int num=p-1;num>=0;num--,range*=2) {
        int start=0;
        for(int i=0;i<(1<<num);i++,start+=range) {
            cin>>price;
            cost[start][start+range-1]=price;
        }
    }
    memset(dp,-1,sizeof(dp));
    return solve(0,(1<<p)-1,0);
}

int main() {
    int cases;
    cin>>cases;
    for(int c=1;c<=cases;c++) {
        llong ret=solve();
        cout<<"Case #"<<c<<": "<<ret<<endl;
    }
}
