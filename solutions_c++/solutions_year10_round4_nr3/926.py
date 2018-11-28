#include<iostream>
using namespace std;

int main(){
    int num=0;
    long t,r,i,j,x1,x2,y1,y2,ans;
    cin>>t;
    while(t--){
               cin>>r;
               int r1=0;
              int  a[105][105]={0};
              for(int k=0;k<r;k++)
               {
                          cin>>x1>>y1>>x2>>y2;
                          if(x1>x2)x1^=x2^=x1^=x2;
                          if(y1>y2)y1^=y2^=y1^=y2;
                          for(i=x1;i<=x2;i++)
                                             for(j=y1;j<=y2;j++)
                                                               if(a[i][j]==0){a[i][j]=1;r1++;}
                          //cout<<r1<<endl;
               }
               ans=0;
               while(r1>0){
                           for(i=100;i>=0;i--)
                                             for(j=100;j>=0;j--)
                                                               if(i==0){
                                                                       if(j==0){
                                                                               if(a[i][j]==1){a[i][j]=0;r1--;}
                                                                               }
                                                                       else if(a[i][j-1]==0)if(a[i][j]==1){a[i][j]=0;r1--;}
                                                                       }
                                                               else if(j==0){
                                                                            if(a[i-1][j]==0)if(a[i][j]==1){a[i][j]=0;r1--;}
                                                                            }
                                                               else {
                                                                     if(a[i-1][j]==a[i][j-1]){
                                                                                             if(a[i-1][j]==0){
                                                                                                              if(a[i][j]==1){a[i][j]=0;r1--;}
                                                                                                              }
                                                                                              else if(a[i][j]==0){a[i][j]=1;r1++;}
                                                                                              }
                                                                    }
                           ans++;
                           }
               cout<<"Case #"<<++num<<": "<<ans<<endl;
                 }
    
    return 0;
    }
