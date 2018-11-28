#include<iostream>
#include<set>
#include<vector>
#include<math.h>
#include<algorithm>
#include<cstdio>
#include<map>
#include<stack>
#include<deque>
#include<queue>
using namespace std;
int main()
{
    char s[50][50],res[50][50];
    int t,r,c,i,j,count,num=0;
    cin>>t;
    while(t--)
    {
              cin>>r>>c;
              num++;
              count=0;
              for(i=0;i<r;i++)
              {
              for(j=0;j<c;j++)
              {
              cin>>s[i][j];
              if(s[i][j]=='#')
              count++;
              }
              }
              int m[50][50]={0};
              if(count%4==0)
              {
                            for(i=0;i<r;i++)
                            {
                                            
                                            for(j=0;j<c;j++)
                                            {
                                                            if(s[i][j]=='.')
                                                            res[i][j]='.';
                                                            else if(s[i][j]=='#')
                                                            {
                                                                 if((s[i+1][j]=='#') && (s[i][j+1]=='#') && (s[i+1][j+1]=='#') && (m[i][j]==0) && (m[i+1][j]==0) && (m[i][j+1]==0) && (m[i+1][j+1]==0))
                                                                 {
                                                                                     res[i][j]='/';
                                                                                     res[i+1][j]='\\';
                                                                                     res[i][j+1]='\\';
                                                                                     res[i+1][j+1]='/';
                                                                                     m[i][j]=1;
                                                                                     m[i+1][j]=1;
                                                                                     m[i][j+1]=1;
                                                                                     m[i+1][j+1]=1;
                                                                                    // j++;
                                                                                     }
                                                             }
                                                            }
                                            }
                                            
                                            int count=0;
                                            char t;
                                            for(i=0;i<r;i++)
                                            {
                                                            for(j=0;j<c;j++)
                                                            {
                                                                            t=res[i][j];
                                                                            if((t=='.') || (t=='/') ||(t=='\\'))
                                                                            count++;
                                                                            }
                                                            }
                                                            if(count!=(r*c))
                                                            cout<<"Case #"<<num<<":\nImpossible\n";
                                                            else
                                                            {
                                                                cout<<"Case #"<<num<<":\n";
                                                                for(i=0;i<r;i++)
                                                                {
                                                                                for(j=0;j<c;j++)
                                                                                cout<<res[i][j];
                                                                                cout<<"\n";
                                                                                }
                                                            }
                                                            
                                                            
                            }
                            else
                            cout<<"Case #"<<num<<":\nImpossible\n";
              }
    return 0;
    }












