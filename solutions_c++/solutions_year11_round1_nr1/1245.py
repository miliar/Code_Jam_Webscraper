#include<cstdio>
#include<cstdlib>
int N,M,K,x1,T;
int GCD(int Q,int R)
{
   if(R!=0)
      return GCD(R,Q%R);
   return Q;    
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int r = 1;r<=T;r++)
    {
        scanf("%d%d%d",&K,&N,&M);
        x1 = GCD(N,100);
        //
        x1=100/x1;//printf("%d",x1);
        if(x1>K||(M==100&&N!=100)||(M==0&&N!=0))
          printf("Case #%d: Broken\n",r);
        else
          printf("Case #%d: Possible\n",r);
    }
    //system("pause");
    return 0;
}
