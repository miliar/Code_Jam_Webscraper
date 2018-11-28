#include<iostream>
#include<cstdio>
int main()
{
    int t,T,a,b,i,j;
    float p[100000],k,ans,temp;
    freopen("C:/inputa.in","r",stdin);
    freopen("C:/outputa.txt","w",stdout);
    
    scanf("%d\n",&T);
    
    t=0;
    while(t++<T)
    {
              k=1.0;
              scanf("%d %d",&a,&b);
              for(i=0;i<a;i++)
              {scanf("%f",p+i);k*=p[i];}
              
              ans=(float)(2*b-a+2-(float)k*(b+1));
              
              if(b>a)temp=(float)b+2;
              else temp=(float)b;
              if(ans>temp)
              ans=(float)temp;
              
              for(i=a-1;i>=0;i--)
              {
                            k=(float)k/p[i];
                            temp=float(2*b-a+2+2*(a-i)-(float)k*(b+1));
                            if(temp<ans)
                            ans=temp;
                              }
              printf("Case #%d: %.6f\n",t,ans);
                 }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
