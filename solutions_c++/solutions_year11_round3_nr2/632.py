#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;

int a[1005];
int b[1005*1005];
int c[1005*1005];
int main()
{
    FILE *in=fopen("B-small-attempt1.in","r");
    FILE *out=fopen("B-small-attempt1.out","w");

    int cnt;
    int cntt=0;
    fscanf(in,"%d",&cnt);
    int l,t,n,cc;
    while(cnt--)
    {
        cntt++;
        fprintf(out,"Case #%d: ",cntt);
        fscanf(in,"%d%d%d%d",&l,&t,&n,&cc);
        for(int i=0;i<cc;i++)
        {
            fscanf(in,"%d",&a[i]);
        }
        c[0]=a[0];
        b[0]=a[0];
        for(int i=1;i<n;i++)
        {
            b[i]=a[i%cc];
            c[i]=c[i-1]+b[i];
        }
        /*for(int i=0;i<n;i++)
        {
            printf("%d ",b[i]);
        }
        printf("\n");
        for(int i=0;i<n;i++)
        {
            printf("%d ",c[i]);
        }
        printf("\n");*/
        int ans=1000000000;
        int dis;
        int temp;
        if(l==2)
        {
            for(int i=0;i<n;i++)
            {
                for(int j=i+1;j<n;j++)
                {
                    temp=0;
                    if(i==0)temp=0;
                    else temp=c[i-1]*2;

                    if(temp>=t)
                    {
                        temp+=b[i];
                    }
                    else if(temp+b[i]*2>t)
                    {
                        int tmp=temp;
                        temp=t;
                        temp+=b[i]-(t-tmp)/2;
                    }
                    else
                    {
                        temp+=b[i]*2;
                    }

                    temp+=(c[j-1]-c[i])*2;
                    if(temp>=t)
                    {
                        temp+=b[j];
                    }
                    else if(temp+b[j]*2>t)
                    {
                        int tmp=temp;
                        temp=t;
                        temp+=b[j]-(t-tmp)/2;
                    }
                    else
                    {
                        temp+=b[j]*2;
                    }

                    temp+=(c[n-1]-c[j])*2;
                    ans=min(ans,temp);
                }
            }
        }
        else if(l==1)
        {
            for(int i=0;i<n;i++)
            {
                temp=0;
                if(i==0)temp=0;
                else temp=c[i-1]*2;

                if(temp>=t)
                {
                    temp+=b[i];
                }
                else if(temp+b[i]*2>t)
                {
                    int tmp=temp;
                    temp=t;
                    temp+=b[i]-(t-tmp)/2;
                }
                else
                {
                    temp+=b[i]*2;
                }
                temp+=(c[n-1]-c[i])*2;
                ans=min(ans,temp);
            }
        }
        else
        {
            ans=c[n-1]*2;
        }
        fprintf(out,"%d\n",ans);
    }
    return 0;
}

