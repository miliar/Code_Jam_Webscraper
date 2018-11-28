#include <iostream>
using namespace std;

int main()
{
    freopen("s.txt","w",stdout);
    int t,n,i,j,k,num[105];
    char s[105][105];
    double wp[105],owp[105],oowp[105],wp1,owp1,oowp1;
    cin>>t;
    for(k=1;k<=t;k++)
    {
       cin>>n;
       for(i=0;i<n;i++)
         for(j=0;j<n;j++)
           cin>>s[i][j];

       for(i=0;i<n;i++)
       {
         num[i]=0;
         for(j=0;j<n;j++)
           if(s[i][j]!='.')
             num[i]++;
       }
       for(i=0;i<n;i++)
       {              
         wp1=0;
         for(j=0;j<n;j++)
           if(s[i][j]=='1')
             wp1=wp1+1;

         wp[i]=wp1/num[i];
       }
       for(i=0;i<n;i++)
       {              
         owp1=0;
         for(j=0;j<n;j++)
           if(s[i][j]!='.')
           {
             if(s[j][i]=='0')
               owp1+=wp[j]*num[j]/(num[j]-1);
             else
               owp1+=(wp[j]*num[j]-1)/(num[j]-1);
           }
         owp[i]=owp1/num[i];
       }
       for(i=0;i<n;i++)
       {              
         oowp1=0;
         for(j=0;j<n;j++)
           if(s[i][j]!='.')
             oowp1+=owp[j];


         oowp[i]=oowp1/num[i];
       }   
       cout<<"Case #"<<k<<":"<<endl;
       for(i=0;i<n;i++)
         cout<<0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]<<endl;
    }
    return 0;
}
