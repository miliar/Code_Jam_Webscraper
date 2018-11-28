#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int main()
{
 int t,r,k,n,i,j,m,l,sum,temp,num=1;
 int* g;
 int* tempg;

 cin>>t;

 freopen("out3.txt","w",stdout);

 while(t--)
 {
  sum=0;
 
  cin>>r>>k>>n;

  g = (int*)malloc(sizeof(int)*n);
  tempg = (int*)malloc(sizeof(int)*n);

  for(i=0; i<n; i++)
    cin>>*(g+i);

  //ride starts
  for(i=0; i<r; i++)
  {
    temp=0;
    
    for(j=0; j<n; j++)
    {
     if(temp+g[j]<=k)
       temp+=g[j];
     else
       break;
    }

    sum+=temp;
    //do circular shifts here
    for(l=0,m=j; m<n; m++,l++)
      tempg[l] = g[m];
    for(m=0; m<j; m++)
     tempg[l++] = g[m];

    for(j=0; j<n; j++)
     g[j] =tempg[j];
   
  }
  cout<<"Case #"<<num<<": ";
  cout<<sum<<endl;
  num++;
 }
return 0;
}