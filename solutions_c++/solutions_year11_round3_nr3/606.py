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

int other[10005];
int main()
{
    FILE *in=fopen("C-small-attempt0.in","r");
    FILE *out=fopen("C-small-attempt0.out","w");

    int t;
    int cntt=0;
    fscanf(in,"%d",&t);
    int n,l,h;
    bool flag;
    while(t--)
    {
        cntt++;
        fprintf(out,"Case #%d: ",cntt);
        fscanf(in,"%d%d%d",&n,&l,&h);
        for(int i=0;i<n;i++)
        {
            fscanf(in,"%d",&other[i]);
        }
        flag=false;
        int ans;
        for(int d=l;d<=h;d++)
        {
            int i;
            for(i=0;i<n;i++)
            {
                if(other[i]%d!=0 && d%other[i]!=0)
                    break;
            }
            if(i==n)
            {
                flag=true;
                ans=d;
                break;
            }
        }
        if(flag) fprintf(out,"%d\n",ans);
        else fprintf(out,"NO\n");
    }
    return 0;
}

