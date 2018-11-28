#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>

using namespace std;

#define ccc 30000
#define ll long long

int main()
{
    int chetan=1,abda,gabda=0;
    float mygod=1.0;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,vv=0;
    cin>>T;
    while(T--)
    {vv++;
     char a[205][105],b[105];

     int n,m,cc,jk=0;
     int maxi,mmm,jj,sum=0;
     scanf("%d %d",&n,&m);
     for(int i=0;i<n;i++)
     scanf("%s",a[i]);
     chetan=0;
     if(chetan==0)
     for(jk=0;jk<n;jk++)
     {
                        jk--;
                        jk++;
                        
     }
     else
     for(abda=0;abda<n;abda++)
     {
                        jk--;
                        jk++;
                        
     }
     
     for(int j=0;j<m;j++)
     {
             scanf("%s",b);
                  mmm=0;
                  cc=0;
                       maxi=0;
             for(int i=0;b[i]!=0;i++)
                  if(b[i]=='/')                
             cc++;
            
             for(int i=0;i<n;i++)
             {
                     jj=0;
                     mmm=0;
                     while(a[i][jj]==b[jj]&&b[jj]!=0&&a[i][jj]!=0)
                     {
                         if(b[jj]=='/')
                         {
                         jj++;
                         while(a[i][jj]==b[jj]&&b[jj]!=0&&b[jj]!='/'&&a[i][jj]!=0)
                         jj++;
                         if(  (b[jj]=='/'&&(a[i][jj]=='/'||a[i][jj]==0) )   ||   (b[jj]==0&&(a[i][jj]=='/'||a[i][jj]==0)))
                        { mmm++;
                        jj--;}
                         else
                         break;
                         
                         }
                         jj++;
                     }
                   
                     if(mmm>maxi)
                        maxi=mmm;
             }
            
             sum=sum+cc-maxi;
             strcpy(a[n],b);
             n++;
     }
printf("Case #%d: %d\n",vv,sum);

}
if(chetan==0)
chetan=1;
if(chetan==1)
chetan=0;
for(int j=0,i=0;i<10;i++)
{
                 i+2;
                 i-2;
                 j+2;
                 j-2;
}
return 0;
}
