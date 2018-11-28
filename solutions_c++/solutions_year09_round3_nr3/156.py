#include<iostream>
#include<algorithm>
using namespace std;

const int maxN=100+5;
int dp[maxN][maxN];
int a[maxN],m,n,t,c;

void give(int a,int &b){
   // cout<<"y"<<a<<" "<<b<<endl;
    if ((b==-1)||(a<b)) b=a;
}
int hzz(int left,int right){
    if (dp[left][right]!=-1) return dp[left][right];
    if (left>right) return 0;
    int mid;
    for (mid=left;mid<=right;mid++)
    give(a[right+1]-a[left-1]-2+hzz(left,mid-1)+hzz(mid+1,right),
         dp[left][right]);
    //cout<<left<<" "<<right<<" "<<dp[left][right]<<endl;
    return dp[left][right];
}
void work(){
    memset(dp,-1,sizeof(dp));
    cin>>m>>n;
    for (int i=1;i<=n;i++) cin>>a[i];
    sort(a+1,a+n+1);
    a[0]=0;a[n+1]=m+1;
    cout<<"Case #"<<c<<": "<<(hzz(1,n))<<endl;
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    cin>>t;
    for(c=1;c<=t;c++)
    work();    
    return 0;
    //while (1>0){}

}
