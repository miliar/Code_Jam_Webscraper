#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

int tt,n;
char line[1024];
char c[128];
int a[128];
char * p;

int main()
{
    freopen("robot.in","r",stdin);
    freopen("robot.out","w",stdout);
    gets(line);
    sscanf(line,"%d",&tt);
    for (int w=1;w<=tt;w++)
    {
        gets(line);
        sscanf(line,"%d",&n);
        p=strchr(line,' ')+1;
        for (int i=1;i<=n;i++)
        {
            sscanf(p,"%c %d",c+i,a+i);
            p=strchr(p,' ')+1;
            p=strchr(p,' ')+1;
        }
        int p1=1,p2=1,ft1=0,ft2=0,sumt=0,t;
        for (int i=1;i<=n;i++)
        {
            if (c[i]=='O')
            {
                t=max(abs(a[i]-p1)-ft1+1,1);
                sumt+=t;
                ft1=0;
                ft2+=t;
                p1=a[i];
            }
            else
            {
                t=max(abs(a[i]-p2)-ft2+1,1);
                sumt+=t;
                ft2=0;
                ft1+=t;
                p2=a[i];
            }
        }
        printf("Case #%d: %d\n",w,sumt);
    }
    return 0;
}
