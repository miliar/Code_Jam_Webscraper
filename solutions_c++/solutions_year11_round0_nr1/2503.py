#include<iostream>
#include<math.h>
using namespace std;
int main()
 { int t,k,tt,t1,t2,o,b,tn=0,y,n,i;char c;cin>>t;
   while(t--)
    {cin>>n;tn++;
     o=1;b=1;t1=0;t2=0;tt=0;
     for(i=0;i<n;i++)
       {cin>>c>>k; 
        if(c=='O'){y=abs(k-o)-t1;if(y<0)y=0;y++;t1=0;t2+=y;tt+=y;o=k;}
        if(c=='B'){y=abs(k-b)-t2;if(y<0)y=0;y++;t2=0;t1+=y;tt+=y;b=k;} 
       }
     cout<<"Case #"<<tn<<": "<<tt<<endl;
   }
    return 0;
 }
     
