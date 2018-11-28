#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int a,b;
int n,m;
int n1,n2,n3;
int t,tt;


int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("b-small-1.out","w",stdout);
    
    int i,j;
    scanf("%d",&t);
    int tt=1;
    while(t--)
    {
        scanf("%d %d",&a,&b);
        printf("Case #%d: ",tt++);
        int cnt=0;
        for(i=a;i<=b;i++)
        {
            n=i;
            n1=n/100;
            n2=(n-n1*100)/10;
            n3=(n-n1*100-n2*10);
            if(n<=10)
                continue;
            else if(n>10&&n<=99)
            {
                if((n2+n3*10)>n&&(n2+n3*10)<=b)
                {
                    //printf("   %d\n",n);
                    cnt++;
                }
            }
            else
            {
                if((n2*100+n3*10+n1)>n&&(n2*100+n3*10+n1)<=b)
                {
                    //printf("0000   %d\n",n);
                    cnt++;
                    //continue;
                }
                if((n3*100+n1*10+n2)>n&&(n3*100+n1*10+n2)<=b)
                {
                    cnt++;
                    //printf("1111   %d\n",n);
                    continue;
                }
            }
        }
        printf("%d\n",cnt);
    }
    //system("pause");
    return 0;
} 
