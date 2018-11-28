#include <iostream>
using namespace std;

int pow(int a,int n)
{
  int ans=1;
  
  while (n--) ans*=a;
  
  return(ans);
}

int Count(int n,int A,int B)
{
  int sum;
  int t=n;
  int digits=0;
  int i,j;
  
  while (t) { ++digits; t/=10; }
  if (digits==0) digits=1;
  
  int a[10];
  
  a[1]=n;
  for (i=2; i<=digits; ++i) a[i]=a[i-1]/10+a[i-1]%10*pow(10,digits-1);
  for (i=1; i<=digits; ++i)
    for (j=i+1; j<=digits; ++j)
      if (a[i]>a[j])
        a[i]^=a[j]^=a[i]^=a[j];
        
  for (i=1; i<=digits; ++i)
    if ( ! (a[i]>=pow(10,digits-1)&&a[i]>=A&&a[i]<=B))
      a[i]=-1;
      
  for (i=1; i<=digits; ++i)
    for (j=i+1; j<=digits; ++j)
      if (a[j]==a[i])
        a[j]=-1;
        
  sum=digits;
  for (i=1; i<=digits; ++i)
    if (a[i]==-1)
      --sum;
      
  for (i=1; a[i]==-1; ++i);
  if (a[i]<n) sum=0;

  return(sum*(sum-1)/2);
}

int main()
{
  freopen("C-large.in","r",stdin);
  freopen("C-large.out","w",stdout);
  
  int T,i,j;
  
  cin>>T;
  for (i=1; i<=T; ++i)
    {
      int sum=0;
      int A,B;
      
      cin>>A>>B;
      
      for (j=A; j<=B; ++j)
        sum+=Count(j,A,B);
      
      cout<<"Case #"<<i<<": "<<sum<<endl;
    }

  fclose(stdin);
  fclose(stdout);
  
  return(0);
}
