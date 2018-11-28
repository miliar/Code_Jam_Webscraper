#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    long long t,n,k,i=1,flag=0,flag1=0,temp;
    char s1[]="Case #";
    char of[]="OFF";
    char on[]="ON";
    cin>>t;
    while(t--)
    {
       cin>>n>>k;
       flag1=0;
       flag=pow(2,n)-1;
       temp=flag;
       while(flag<=k)
       {
        if(flag==k)
           {
            flag1=1; 
            break;      
           }
        else {flag=(flag+1+temp);}//cout<<flag;}
           
       }//inner while
       if(flag1) {cout<<s1<<i++<<": "<<on<<endl;}
       else {cout<<s1<<i++<<": "<<of<<endl;}          
    }
return 0;
}
