#include<cstdio>
//#include<cstdlib>
//#include<cstring>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ks;
    scanf("%d",&ks);
    int t=1,n,k;
    //bool s[30];
    while(ks--)
    {
      scanf("%d%d",&n,&k);
      
      //memset(s,0,sizeof(s));
      
      int a=k&((1<<n)-1);
      int b=(1<<n)-1;
      bool ans=false;
      if(a==b)
       ans=true;
       
       printf("Case #%d: %s\n",t++,ans?"ON":"OFF");
      }
      return 0;
}
        
      
