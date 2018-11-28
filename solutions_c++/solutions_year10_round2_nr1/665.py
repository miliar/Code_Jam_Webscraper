#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<list>
#include<map>
/* Author
Saurabh Agrawal
*/
#include<string>
#include<set>
#include<algorithm>
using namespace std;

#define mm 30000
#define ll long long

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,vv=0;
    int k;
    cin>>T;
    while(T--)
    {vv++;
     char a[205][105],b[105];
     int n,m,cc;
     int maxi,mmm,jj,sum=0;
     scanf("%d %d",&n,&m);
     for(int i=0;i<n;i++)
     scanf("%s",a[i]);
     for(int j=0;j<m;j++)
     {//printf("hi");
                     for(k=0;k<2;k++);
             scanf("%s",b);
                  mmm=0;
                  cc=0;
                       maxi=0;
             for(int i=0;b[i]!=0;i++)
                  if(b[i]=='/')                
             cc++;
            // printf("cc=%d\n",cc);
             for(int i=0;i<n;i++)
             {
                     jj=0;
                     mmm=0;
                     while(a[i][jj]==b[jj]&&b[jj]!=0&&a[i][jj]!=0)
                     {
                         if(b[jj]=='/')
                         {//&&a[i][jj+1]==b[jj+1])
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
                    //mmm--;
                        // printf("mmm=%d\n",mmm);
                     if(mmm>maxi)
                        maxi=mmm;
             }
            // printf("maxi=%d  sum=%d\n",maxi,sum);
             sum=sum+cc-maxi;
             strcpy(a[n],b);
             n++;
     }
printf("Case #%d: %d\n",vv,sum);

}
//while(1);
return 0;
}
