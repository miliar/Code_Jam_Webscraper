#include<iostream>
#include<cstdio>
#include<cstring>
int log(int x)
{
    int j,k;
        for(j=x,k=1;j;k*=10)
     {
                 j/=10;        
     }
     return k;
}
int check(int x,int b)
{
     int i,j,k,ans=0;
     int list[10],u,y;
     bool flag;
     k=log(x);
     
     for(i=10,u=0;i<=x;i*=10)
     {
          flag=1;
          j=(x%i)*(k/i)+(x/i);
          for(y=0;y<=u;y++)if(j==list[y]){flag=0;break;}
          
          if(j<=b && j>x && flag)
                  {
                   //printf("x: %d j:%d\n",x,j);
                   list[++u]=j;
                   ans++;
                   }
     }
     return ans;
 }
int main()
{
    int t,T,i,j,k,a,b;
    freopen("C:/inputc.in","r",stdin);
    freopen("C:/outputc.txt","w",stdout);
    scanf("%d",&T);
    t=0;
    while(t++<T)
    {
                scanf("%d %d",&a,&b);
                for(i=a,j=0;i<=b;i++)
                j+=check(i,b);
                
                printf("Case #%d: %d\n",t,j);
                }
    
    fclose(stdin);
    fclose(stdout);
    system("pause");
    return 0;
    
}
