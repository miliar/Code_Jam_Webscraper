#include <iostream>
using namespace std;
string word = "welcome to code jam";
int T;
string text;
int mod = 10000;
int dp[501][30];

int main()
{
    cin>>T;
    //cin>>text;
    getchar();
    int i;
     for(i = 1; i <= T; i++)
      {
       char a;
       text = "";
       while(1)
       {
        a = getchar();
        if(a == '\n' || a == EOF) break;
        text+=a;
       }
       //cout<< "Text:"<<text << endl;
       //cin>>text;
       int j,k,l;
       memset(dp,0,sizeof(dp));
        for(j = 0; j < text.size(); j++)
         if(text[j] == 'w') dp[j][0] = 1;
        for(j = 0; j < text.size(); j++)
         for(k = 0; k < j; k++)
          for(l = 0; l < word.size() - 1; l++)
           {
            if(text[k] != word[l]) continue;
            if(text[j] == word[l+1]) 
            {
             dp[j][l+1] += dp[k][l] % mod;
             dp[j][l+1]%=mod;
            }
           }
        int br = 0;
        for(j = 0; j < text.size();j++)
         {
           br += dp[j][word.size() - 1];
           br%=mod;
          
         /* for(k = 0; k < word.size(); k++)
          {
           cout<<dp[j][k]<<" ";
          }
          cout<<endl;
          */
         }   
         cout<<"Case #"<<i<<": ";
         int digits = 0;
         int temp = br;
         while(temp != 0)
          {
           digits++;
           temp/=10;
          }
          if(digits == 0) digits++;
         for(j = 0; j < 4 - digits; j++)
         cout<<"0";
         cout<< br <<endl;
       }
    return 0;
}
