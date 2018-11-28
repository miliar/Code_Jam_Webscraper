#include<stdio.h>
#include<math.h>
using namespace std;
int gcd(int a,int b)
{
    if(b==0)
    return a;
    return gcd(b,a%b);
}
int main()
{
	freopen("a.in","r",stdin);
    freopen("b.txt","w",stdout);
    int t,N,a,b,c,temp,d1,d2,a1,a2,a3;
    scanf("%d",&t);
    int i=1;
    while(i<=t)
    {
        scanf("%d",&N);
        if(N==2)
        {
            scanf("%d %d",&a,&b);
            printf("Case #%d: ",i);
            if(a<b)
            {
                temp=b;
                b=a;
                a=temp;
            }
            d1=a-b;
            if(d1==0||a%d1==0)
            printf("0\n");
            else
            {
                 d1=((a/d1)+1)*d1-a;
                 printf("%d\n",d1);
            }
        }
        else 
        {
             scanf("%d %d %d",&a1,&a2,&a3);
             printf("Case #%d: ",i);
             if(a1>=a2&&a1>=a3)
             {
                  a=a1;
                  if(a2>=a3)
                  {
                      b=a2;
                      c=a3;
                  }
                  else
                  {
                      c=a2;
                      b=a3;
                  }
             }
             else if(a2>=a1&&a2>=a3)
             {
                  a=a2;
                  if(a1>=a3)
                  {
                      b=a1;
                      c=a3;
                  }
                  else
                  {
                      c=a1;
                      b=a3;
                  }
             }
             else if(a3>=a2&&a3>=a1)
             {
                  a=a3;
                  if(a2>=a1)
                  {
                      b=a2;
                      c=a1;
                  }
                  else
                  {
                      c=a2;
                      b=a1;
                  }
             }
             d1=a-b;
             d2=b-c;
             d1=gcd(d1,d2);
             if(d1==0)
             printf("0\n");
             else
             {
                 if(a%d1==0)
                 printf("0\n");
                 else
                 {
                     d1=((a/d1)+1)*d1-a;
                     printf("%d\n",d1);
                 }
             }
        }
        ++i;
    }
	return 0;
}
