
#include<iostream>
using namespace std;
int main()
{
 int i, j, k, t, s, n, p, a[105], c, count;
 cin>>t;
 for(i=0;i<t;i++)
 {
  cin>>n>>s>>p;
  for(j=0;j<n;j++) cin>>a[j];
  c = (p*3)-2; count=0;
  for(j=0;j<n;j++) 
    {
     if (a[j]>=c) count++;
     else if (s>0 && c>2)
       {
        if((a[j]==c-1)||(a[j]==c-2)) {s--;count++;}
       }
    }
  cout<<"Case #"<<i+1<<": "<<count<<endl;
 }
}
