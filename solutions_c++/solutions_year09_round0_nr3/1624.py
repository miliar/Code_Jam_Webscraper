#include<iostream>
using namespace std;
int dp[500][100];
int main()
{
    string w="welcome to code jam";
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int N;
    scanf("%d\n",&N);
    for(int caso=1;caso<=N;caso++)
    {
            string g;
            char x=0;
            while(1)
            {
                scanf("%c",&x);
                if(x=='\n')break;
                g+=x;              
            }
                //cout<<g<<endl;
                //cout<<w<<endl;
            for(int i=g.size()-1;i>=0;i--)for(int j=w.size()-1;j>=0;j--)
            {
                if(i==g.size()-1&&j==w.size()-1)
                {
                         if(w[j]==g[i])dp[i][j]=1;
                         else
                         dp[i][j]=0;
                         continue;                                
                }
                if(i==g.size()-1)
                {
                      dp[i][j]=0;
                      continue;                 
                }
                if(j==w.size()-1)
                {
                      if(w[j]==g[i])
                      {
                             dp[i][j]=(1+dp[i+1][j])%1000;                     
                      }
                      else
                      dp[i][j]=dp[i+1][j];
                      continue;                 
                }
                dp[i][j]=dp[i+1][j];
                if(g[i]==w[j])dp[i][j]=(dp[i][j]+dp[i+1][j+1])%1000;        
            }
            char A[4];
            sprintf(A,"%d",dp[0][0]);
            string s=A;
            while(s.size()<4)
            {
                   s="0"+s;
            }
            //for(int i=0;i<g.size();i++){for(int j=0;j<w.size();j++)cout<<dp[i][j]<<" ";cout<<endl;}
            cout<<"Case #"<<caso<<": "<<s<<endl;
                    
    }
return 0;    
}
