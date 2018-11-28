#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;
int main()
{
int t,i,j,count1=0;
cin>>t;
while(t--)
{ count1++;
  char a[65];int b[65];
   cin>>a;
  b[0]=1;
   for(i=1;i<strlen(a);i++)if(a[i]==a[0])b[i]=1;else break;
   
   b[i]=0;
   int n=2;i++;
  for(;i<strlen(a);i++)
    {
      for(j=0;j<i;j++)
       { if(a[i]==a[j])
          break;
        }
         if(j!=i)
           b[i]=b[j];
         else
           {b[i]=n;n++;}
     }
  int base=n;
  
  int count=0;long long p=0;
  for(i=strlen(a)-1;i>=0;i--)
   p+=b[i]*(int)pow(base,strlen(a)-1-i);
cout<<"Case #"<<count1<<": "<<p<<endl;
}
return 0;
}
