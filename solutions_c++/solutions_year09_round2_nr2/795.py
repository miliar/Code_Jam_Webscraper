#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
int t,count=0;
cin>>t;
while(t--)
{
 count++;
 char a[25];int b[25];
int i,j,k;
   cin>>a;
   for(i=0;i<strlen(a);i++)
     b[i]=a[i]-'0';
   for(i=strlen(a)-2;i>=0;i--)
     if(b[i]<b[i+1])
       break;
   if(i!=-1)
{
   int min=100,min1;
   for(j=i+1;j<strlen(a);j++) 
     if(b[j]<min && b[j]>b[i])
       {
          min1=j; min=b[j];
       }
    swap(b[min1],b[i]);
  sort(b+i+1,b+strlen(a));

 cout<<"Case #"<<count<<": ";
  for(i=0;i<=strlen(a)-1;i++)
  cout<<b[i];
  cout<<endl;
}
else
{
 sort(b,b+strlen(a));
 for(i=0;i<=strlen(a)-1;i++)
  if(b[i]!=0)break;
 swap(b[i],b[0]);
cout<<"Case #"<<count<<": ";
  cout<<b[0]<<"0";
  for(i=1;i<=strlen(a)-1;i++)
  cout<<b[i];
  cout<<endl;

}
}
}
