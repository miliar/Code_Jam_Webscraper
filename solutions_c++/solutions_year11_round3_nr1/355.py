#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)

int main()
{
     freopen("inputA.txt","r",stdin);
     freopen("outputA.txt","w",stdout);

     long int t,i,j,k,n,cn=1,r,c;
     cin>>t;
     while(t--)
     {
         string str[110];
           cin>>r>>c;
           FOR(i,r)cin>>str[i];

           int b=0;
           FOR(i,r)
            FOR(j,c)
            {
                if(str[i][j]=='#')b++;
            }
            if(b%4!=0)cout<<"Case #"<<cn++<<":"<<endl<<"Impossible"<<endl;
            else{
                int g=0;
                FOR(i,r)
                    FOR(j,c)
                    {
                        if(str[i][j]=='#')
                        {
                            int f=0;
                            if(j<c-1&&str[i][j+1]=='#')
                            {
                                if(i<r-1&&str[i+1][j]=='#')
                                {
                                        if(i<r-1&&j<c-1&&str[i+1][j+1]=='#')
                                        {
                                            str[i][j]='/';
                                            str[i][j+1]='\\';
                                            str[i+1][j]='\\';
                                            str[i+1][j+1]='/';
                                            f=1;
                                        }

                                }
                            }
                            if(f==0)
                            {
                                g=1;
                            }

                        }
                    }
                    cout<<"Case #"<<cn++<<":"<<endl;
                    if(g==1)
                    cout<<"Impossible"<<endl;
                    else {
                        FOR(i,r)cout<<str[i]<<endl;

                        }
            }

     }
    return 0;
}
