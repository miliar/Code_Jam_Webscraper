#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<iomanip>
using namespace std;
struct node
{
       int x,y;
}s[10000];
int m,n;
int col[2134]={1,1};

      vector<vector<int> > mat;
      int v[10];
      int res=0;
      vector<int>pp;
void solve(int t)
{
     if(t==m+1){
                memset(v,0,sizeof(v));
                int d=1;
                for(int i=1;i<=m;i++){
                        v[col[i]]=1;
                        if(col[i]>d)d=col[i];
                        }
                        if(d<=res)return;
                        
                for(int i=1;i<=d;i++){
                        if(v[i]==0)return;
                        }
                        
                      //  cout<<"col   ";
                    //    for(int i=1;i<=m;i++)cout<<col[i]<<" ";cout<<endl;
                        for(int i=0;i<mat.size();i++){
                                vector<int>acm(d+1);
                                for(int j=0;j<mat[i].size();j++){
                                //        cout<<"mat"<<mat[i][j]<<" ";
                                        int index=mat[i][j];
                                        int cc=col[index];
                                acm[cc]=123;
                                }
                              //  cout<<endl;
                             //   for(int j=1;j<=d;j++)cout<<(int)acm[i];
                            //    cout<<endl;
                                for(int j=1;j<=d;j++)
                        if(acm[j]==0)return;
                                }
                                
                res=d;
                pp=vector<int>(m);
              for(int i=1;i<=m;i++)
              pp[i-1]=col[i];                  
     }
     else{
          for(int i=1;i<=m;i++){
                  col[t]=i;
                  solve(t+1);
          }
     }
}
int main()
{
    freopen("b1.txt","r",stdin);
    freopen("b2.txt","w",stdout);
    
    int cas;
    scanf("%d",&cas);
    for(int ii=1;ii<=cas;ii++)
    {
      
      scanf("%d%d",&m,&n);
      vector<vector<int> > a;
      vector<int>b(m);
      for(int i=0;i<m;i++)b[i]=i+1;
      a.push_back(b);
      for(int i=0;i<n;i++)scanf("%d",&s[i].x);
      for(int i=0;i<n;i++)scanf("%d",&s[i].y);
      for(int i=0;i<n;i++)
      {
              for(int j=0;j<a.size();j++)
              {
                      for(int k=0;k<a[j].size();k++)
                      {
                              if(a[j][k]==s[i].x)
                              {
                                                 for(int p=0;p<a[j].size();p++){
                                                         if(a[j][p]==s[i].y){
                                                 vector<int>c,d;
                                                 for(int jj=0;jj<=k;jj++)
                                                 c.push_back(a[j][jj]);
                                                 for(int jj=p;jj<a[j].size();jj++)
                                                 c.push_back(a[j][jj]);
                                                 for(int jj=k;jj<=p;jj++)
                                                 d.push_back(a[j][jj]);
                                                 a[j]=c;
                                                 a.push_back(d);
                                                 goto end;
                                                 }
                                                 }
                              }
                      }
              }
              end:;
      }
   //   for(int i=0;i<a.size();i++){
   //           for(int j=0;j<a[i].size();j++)cout<<a[i][j]<<" ";
   //           cout<<endl;
  //            }
      mat=a;
      res=0;
      solve(2);
     printf("Case #%d: %d\n",ii,res);
     for(int i=0;i<m;i++)printf("%d ",pp[i]);
     puts("");
     }
    return 0;
}
