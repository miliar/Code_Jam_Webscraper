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
#include <cstring>
using namespace std;

int main()
{
    FILE *in=fopen("C-small-attempt0.in","r");
    FILE *out=fopen("C-small-attempt0.out","w");

    int t;
    int cntt=0;
    int temp[1005];
    int total;
    int n;
    fscanf(in,"%d",&t);
    while(t--)
    {
        total=0;
        cntt++;
        fscanf(in,"%d",&n);
        int a=0;
        int b=0;
        int ra=0;
        int rb=0;
        int ans=-1;
        memset(temp,0,sizeof(temp));
        for(int i=0;i<n;i++)
        {
            fscanf(in,"%d",&temp[i]);
        }
        for(int i=0;i<(int)pow(2,n);i++)
        {
            a=0;
            b=0;
            ra=0;
            rb=0;
            for(int j=0;j<n;j++)
            {
                if((1<<j) & i)
                {
                   a= a^temp[j];
                   ra= ra+temp[j];
                }
                else
                {
                    b= b^temp[j];
                    rb= rb+temp[j];
                }
            }
            if(a==b && rb!=0 &&ra!=0) ans=max(ans,max(rb,ra));
        }
        if(ans==-1)
        {
            fprintf(out,"Case #%d: NO\n",cntt);
            //printf("Case #%d: NO\n",cntt);
        }
        else
        {
            fprintf(out,"Case #%d: %d\n",cntt,ans);
            //printf("Case #%d: %d\n",cntt,ans);
        }
    }
}
