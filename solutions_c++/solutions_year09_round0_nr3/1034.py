#include <iostream>
#include <vector>

using namespace std;

const char q[]="_welcome to code jam";
int dp[21][501];
string t;
int sizet;

vector<int> prev[501];

int solve()
{
 memset(dp,0,sizeof(dp));
 
 getline(cin,t);
 int sizet=t.size();
 int i,j,k,to;
 
 for(i=0;i<sizet;i++) prev[i]=vector<int> ();
 
 for(i=0;i<sizet;i++)
    for(j=i-1;j>=0;j--)
        {
         if(t[i]=='e' && (t[j]=='w' || t[j]=='m' || t[j]=='d')) prev[i].push_back(j);
         else if(t[i]=='l' && t[j]=='e') prev[i].push_back(j);
              else if(t[i]=='c' && ( t[j]=='l' || t[j]==' '))  prev[i].push_back(j);
                   else if(t[i]=='o' && ( t[j]=='c' || t[j]=='t')) prev[i].push_back(j);
                        else if(t[i]=='m' && (t[j]=='o' || t[j]=='a')) prev[i].push_back(j);
                             else if(t[i]==' ' && (t[j]=='e' || t[j]=='o')) prev[i].push_back(j);
                                  else if(t[i]=='t' && (t[j]==' ')) prev[i].push_back(j);
                                       else if(t[i]=='d' && t[j]=='o') prev[i].push_back(j);
                                            else if(t[i]=='j' && t[j]==' ') prev[i].push_back(j);
                                                 else if(t[i]=='a' && t[j]=='j') prev[i].push_back(j);             
        }
 
 for(i=0;i<sizet;i++)
    if(t[i]=='w') dp[1][i]=1;
 
 for(i=2;i<20;i++)
    for(j=0;j<sizet;j++)
       { 
         dp[i][j]=0;
         if(q[i]!=t[j]) continue;
         
         to=prev[j].size();
         for(k=0;k<to;k++)
             { dp[i][j]+=dp[i-1][prev[j][k]]; dp[i][j]%=10000; }
       }       
 
  int res=0;
  for(j=0;j<sizet;j++)
     { res+=dp[19][j]; res%=10000; }
  return res;
}

int main()
{
 int tests;
 scanf("%d\n",&tests);
 for(int i=1;i<=tests;i++)
    {
     int res=solve();
     printf("Case #%d: %d%d%d%d\n",i,res/1000,(res%1000)/100,(res%100)/10,res%10);     
    }
    
 //system("pause");
 return 0;
}
