#include<iostream>
using namespace std;
int gcd(int a,int b){
	return b?gcd(b,a%b):a;
}
int main()
{
  int i,j,k,t,n;
  int ii,jj;
  int a[10];
  int ans=0;
  int tmp;
  int factor;
  freopen("B-small-attempt1.in","r",stdin);
  freopen("ou.txt","w",stdout);
 // freopen("in.txt","r",stdin);
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {  
     scanf("%d",&n);
     for(j=1;j<=n;j++)
       scanf("%d",&a[j]);
     for(ii=1;ii<=n;ii++)
        for(jj=ii+1;jj<=n;jj++)
        {
          if(a[ii]==a[jj])
          {
             a[jj]=a[n];
             n--;
           //  printf("%d %d\n",n,a[jj]);
          }
        }
     //for(ii=1;ii<=n;ii++)
      // printf("%d ",a[ii]);
     //printf("\n");
     if(n==1) ans=0;
     else
     {
        factor=abs(a[1]-a[2]);          
        for(ii=1;ii<=n;ii++)
          for(jj=ii+1;jj<=n;jj++)
          {
             tmp=abs(a[ii]-a[jj]);
              factor=gcd(factor,tmp);
         }
    // for(j=1;j<=n;j++)
      //  printf("%d ",a[j]%factor);
     //printf("\n");
       //cout<<factor<<endl;
       if(factor==1) ans=0;
       else if(a[1]%factor==0) ans=0;
	   else ans=factor-a[1]%factor;
     }
     printf("Case #%d: %d\n",i,ans);
    // cout<<ans<<endl;
  }
  //while(1);
  return 0;
}
