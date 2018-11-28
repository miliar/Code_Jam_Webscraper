#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
int calculate_bribe(int k[],int p,int q)
{
int r[10001];int d=0,m,n,e,c,i;
fill(r,r+10001,1);
for(i=0;i<q;i++)
  {
    m=k[i]-1;
   while(r[m]==1 && m>0)
    {d++;m--;}
   m=k[i]+1;
    while(r[m]==1 && m<=p)
    {d++;m++;}
    r[k[i]]=0;
  }
return d;
} 
int main()
{
int t,count1=0;
cin>>t;
while(t--)
{count1++;
  int p,q,i,j,k[101],c;
  cin>>p>>q;
  
   
  
  for(i=0;i<q;i++)
    { 
        cin>>k[i];
    }
   //for(i=0;i<(int)pow(2.0,q);i++)
    c=calculate_bribe(k,p,q);
   while(next_permutation(k,k+q))
       {
          c=min(c,calculate_bribe(k,p,q));
          
       }
    cout<<"Case #"<<count1<<": "<<c<<endl;      
    
}
return 0;
}
