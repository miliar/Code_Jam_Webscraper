#include<iostream>
#include<stack>
using namespace std;
#define MAX 100
int alt[MAX][MAX];
char basin[MAX][MAX];
int main()
{
    int i,j,r,c,x,y,t,h,w,k,cnt;
    stack<int> mapr;
    stack<int> mapc;
    cin>>t;
    for(i=0;i<t;i++)
    {
                    for(j=0;j<MAX;j++)
                    for(k=0;k<MAX;k++)
                    {
                                      alt[j][k]=10001;
                                      basin[j][k]='\0';
                    }
                    cin>>h>>w;
                    for(j=0;j<h;j++)
                    for(k=0;k<w;k++)
                    cin>>alt[j][k];
                    cnt=0;
                    for(j=0;j<h;j++)
                    for(k=0;k<w;k++)
                    {
                                    if(basin[j][k]=='\0')
                                    {
                                                         mapr.push(j);
                                                         mapc.push(k);
                                                         while(!mapr.empty())
                                                         {
                                                                             x=r=mapr.top();
                                                                             y=c=mapc.top();
                                                                             if((r-1)>=0 && alt[r-1][c]<alt[x][y])
                                                                             {
                                                                                         x=r-1;
                                                                                         y=c;
                                                                             }
                                                                             if((c-1)>=0 && alt[r][c-1]<alt[x][y])
                                                                             {
                                                                                         x=r;
                                                                                         y=c-1;
                                                                             }
                                                                             if((c+1)<w && alt[r][c+1]<alt[x][y])
                                                                             {
                                                                                         x=r;
                                                                                         y=c+1;
                                                                             }
                                                                             if((r+1)<h && alt[r+1][c]<alt[x][y])
                                                                             {
                                                                                         x=r+1;
                                                                                         y=c;
                                                                             }
                                                                             if(x==r && y==c)
                                                                             {
                                                                                     basin[r][c]='a'+cnt;
                                                                                     mapr.pop();
                                                                                     mapc.pop();
                                                                                     while(!mapr.empty())
                                                                                     {
                                                                                                         basin[mapr.top()][mapc.top()]='a'+cnt;
                                                                                                         mapr.pop();
                                                                                                         mapc.pop();
                                                                                     }
                                                                                     cnt++;
                                                                             }
                                                                             else
                                                                             {
                                                                                 if(basin[x][y]!='\0')
                                                                                 {
                                                                                                      while(!mapr.empty())
                                                                                                      {
                                                                                                                          basin[mapr.top()][mapc.top()]=basin[x][y];
                                                                                                                          mapr.pop();
                                                                                                                          mapc.pop();
                                                                                                      }
                                                                                 }
                                                                                 else
                                                                                 {
                                                                                     mapr.push(x);
                                                                                     mapc.push(y);
                                                                                 }
                                                                             }
                                                         }
                                    }
                    }
                    cout<<"Case #"<<i+1<<":"<<endl;
                    for(j=0;j<h;j++)
                    {
                                    for(k=0;k<w;k++)
                                    {
                                                    if(k!=0)
                                                    cout<<" ";
                                                    cout<<basin[j][k];
                                    }
                                    cout<<endl;
                    }
    }
    return 0;
}
                                    
                                                                                                         
                                                                             
                                                         
    
    
