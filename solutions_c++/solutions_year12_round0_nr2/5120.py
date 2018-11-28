#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>
	
using namespace std;

#define inf (1<<28)
#define mem(x,val) memset((x),(val),sizeof(x));

#define mx 105
int n,s,p,t[mx];
long long dp[mx][mx];
long long call(int pos,int l){
    if(l<0) return -1*inf;
    if(pos==n) {
        if(l==0) return 0;
        return -inf;
    }
    if(dp[pos][l]!=-1) return dp[pos][l];
    long long ret=0;
    for(int i=0; i<=t[pos]; i++){
        for(int j=0; j<=t[pos]; j++){
            if(i+j>t[pos]) break;
            int k=t[pos]-(i+j);
            if(abs(i-j)>2 or abs(i-k)>2 or abs(j-k)>2) continue;
            if(i>10 or j>10 or k>10) continue;
            int mxx=max(i,max(j,k));
            int ll=l-(abs(i-j)==2 or abs(i-k)==2 or abs(j-k)==2);
            ret=max(ret,call(pos+1,ll)+(mxx>=p));
        }
    }
    return dp[pos][l]=ret;
}

int main(){
	
	int test,caseno=0;
	cin>>test;
	while(test--){
	    cin>>n>>s>>p;
	    for(int i=0;i<n;i++)cin>>t[i];
	    mem(dp,-1);
	    printf("Case #%d: ",++caseno);
	    cout<<call(0,s)<<endl;
	}
    
    return 0;
}
