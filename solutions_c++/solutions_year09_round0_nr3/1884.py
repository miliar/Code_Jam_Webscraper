#include<iostream>
#include<math.h>
#include<string>
using namespace std;

int main()
{
    int n,c2=1;
    cin>>n;
    getchar();
    while(n--)
    {
     
         string s="welcome to code jam";
         string t1,t;
         int i,j,k;
         getline(cin,t);
        // cout<<t<<endl;         
      
         int l1=s.length();
         int l2=t.length();
         long long a[2][10001]={0};
         if(s[0]==t[0]) a[0][0]=1;
            else a[0][0]=0;
      
         for(j=1;j<l2;j++)
          if(s[0]==t[j]) a[0][j]=(a[0][j-1]+1)%10000;
              else a[0][j]=a[0][j-1];
         for(i=1;i<l1;i++)
           {
             if(s[i]==t[0] && a[0][l2]) a[1][0]=1;
                      else a[1][0]=0;
             
             for(j=1;j<l2;j++)
                   {
                    if(s[i]==t[j]) a[1][j]=(a[0][j-1]+a[1][j-1])%10000;
                    else a[1][j]=a[1][j-1];
                   }
              for(j=0;j<l2;j++){a[0][j]=a[1][j];a[1][j]=0;}
           }                        
         cout<<"Case #"<<c2<<": ";
         a[0][l2-1]%=10000;
         if(a[0][l2-1]<10) cout<<"000";
         else if(a[0][l2-1]<100) cout<<"00";
         else if(a[0][l2-1]<1000) cout<<"0";
         cout<<a[0][l2-1]%10000<<endl;
         c2++;
     }
    
    return 0;
}      
             
             
             
                    
