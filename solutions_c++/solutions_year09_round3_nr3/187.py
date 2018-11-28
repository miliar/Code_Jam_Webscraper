#include <iostream>

using namespace std;

int n,no,ans;
int dp[102][102];
int dat[102];
int i,ii,p,q;

int getdp(int begi, int endi)
{
    int temp;
    
    if(dp[begi][endi]!=-1) return dp[begi][endi];
    else
    {
    if(begi+1==endi)
    {
    dp[begi][endi] = 0;
    }
    else
    {
    int mx = 10000000; 
    for(int i=begi+1;i<endi;i++) 
     {
     temp = getdp(begi,i) + getdp(i,endi);        
     if(mx>temp) mx = temp;
     }
    
    dp[begi][endi] = mx + dat[endi]-dat[begi] - 2;
    }
}   
    //cout << dp[begi][endi] << endl; 
    return dp[begi][endi];
}

int main()
{
    cin >> n; no = 0;
    
    while(n--)
    {no++;
    
    cin >> p >> q;
    for(i=1;i<=q;i++) cin >> dat[i];
    dat[0] = 0; dat[q+1] = p+1;
    
    for(i=0;i<=q+1;i++)
     for(ii=0;ii<=q+1;ii++) dp[i][ii] = -1;
    
    ans = getdp(0,q+1);
    
    cout << "Case #" << no << ": " << ans << endl;
    }
}
