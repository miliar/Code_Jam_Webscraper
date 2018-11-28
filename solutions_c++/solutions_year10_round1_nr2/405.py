
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int tc,tt;
int D,AD,M,N,ans;
int ar[110];
int dp[110][260];

int chg(int a, int b)
{
 if(a==-1) return b;
 if(a>b) return b; else return a;
}

int main() 
{
    cin >> tc;
    for(int tt=0;tt<tc;tt++)
    {
     cin >> D >> AD >> M >> N;
     memset(dp,-1,sizeof(dp));
     for(int i=0;i<N;i++) cin >> ar[i];
          
     for(int i=0;i<256;i++) dp[0][i] = abs(i-ar[0]);
     dp[0][ar[1]] = chg(dp[0][ar[1]],D);
     
     for(int i=0;i<N-1;i++)
      for(int ii=0;ii<256;ii++)
      {
       
       for(int iii=0;iii<256;iii++)
       {
        if(abs(ii-iii)<=M) dp[i+1][iii] = chg(dp[i+1][iii],dp[i][ii]+(abs(iii-ar[i+1])));
        else if(M!=0)
        {
         int temp = (abs(ii-iii)-1)/M;
         temp *= AD;
         dp[i+1][iii] = chg(dp[i+1][iii],dp[i][ii]+temp+(abs(iii-ar[i+1])));
        }
       }
       
       dp[i+1][ii] = chg(dp[i+1][ii], dp[i][ii] + D);       
      }
     /*
     for(int i=0;i<N;i++){
      for(int ii=0;ii<10;ii++)
      cout << dp[i][ii] << " ";
      cout << endl;}
     */
     ans = 255*255;  
     for(int i=0;i<256;i++) if(ans>dp[N-1][i]) ans = dp[N-1][i];
     
     cout << "Case #" << tt+1 << ": ";
     cout << ans << endl;
    }
}
