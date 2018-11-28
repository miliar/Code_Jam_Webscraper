#include<iostream>
using namespace std;
int a[1110];
int b[1110];
int check(int x,int y)
{
  if(a[x]<a[y]&&b[x]>b[y]) return 1;
  if(a[x]>a[y]&&b[x]<b[y]) return 1;   
  return 0;
}
int main()
{
    int i,j,k;
    int t,n,ans;
    //freopen("A-large.in","r",stdin);
    //freopen("ou.txt","w",stdout);
    scanf("%d",&t);
    for(int ii=1;ii<=t;ii++)
    { 
      ans=0;
      scanf("%d",&n);
      for(i=0;i<n;i++)
         scanf("%d%d",&a[i],&b[i]);
      for(i=0;i<n;i++)
         for(j=i+1;j<n;j++)
             if(check(i,j)) ans++;
      printf("Case #%d: %d\n",ii,ans);
    }
   // while(1);
    return 0;
}
