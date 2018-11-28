#include<iostream>
using namespace std;
int main()
{
    int t,b=1;
    cin>>t;
    while(t--)
    {
          int n,a[101][101];
          float wp[101],owp[101],oowp[101];    
          string str;
          cin>>n;
          for(int i=0;i<n;i++)
          {
                  cin>>str;
                  for(int j=0;j<n;j++)
                  {
                         if(str[j]=='0')
                             a[i][j]=0;
                         else if(str[j]=='.')
                              a[i][j]=-1;
                         else
                             a[i][j]=1;
                  }
          }
          
          for(int i=0;i<n;i++)
          {
             int tot=0,win=0;     
             for(int j=0;j<n;j++)        
             {
                 if(a[i][j]==1)
                    win++;
                 if(a[i][j]!=-1)
                    tot++;
             }
             wp[i]=win/(float)tot;
            // cout<<wp[i]<<"\n";
          }
          
          for(int k=0;k<n;k++)
          {
               owp[k]=0;
               int megatot=0;   
               for(int i=0;i<n;i++)
               {
                 int tot=0,win=0;     
                 if(a[i][k]!=-1)
                 {
                   megatot++;
                 if(i!=k)
                 {
                    for(int j=0;j<n;j++)        
                    {
                       if(j!=k)
                       {     
                           if(a[i][j]==1)
                                 win++;
                           if(a[i][j]!=-1)
                                tot++;                 
                       }                       
                    }
                    if(tot!=0)
                          owp[k]+=win/(float)tot;
                  }                  
                  }
               }
               owp[k]/=(float)megatot;
              // cout<<owp[k]<<"\n\n";
          }             
          
          for(int k=0;k<n;k++)
          {
                  oowp[k]=0;
                  int megatot=0;
                 for(int i=0;i<n;i++) 
                 {
                       if(a[i][k]!=-1)
                       {
                               oowp[k]+=owp[i];
                               megatot++;       
                       }  
                 }
                 oowp[k]/=float(megatot);
                 //cout<<oowp[k]<<"\n";
          }
          
          cout<<"Case #"<<b++<<":\n";
          for(int k=0;k<n;k++)
          {
                cout<<(0.25*wp[k]+0.5*owp[k]+0.25*oowp[k])<<"\n";  
          }
    }
}
