#include <iostream>
using namespace std;
int tn,t;
int n;
int a[1020];
bool v[1020];
double ans;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int i,j;
    cin >> tn;
    for (t=1;t<=tn;t++)
    {
        cin >> n;
        ans=0;
        memset(v,0,sizeof v);
        
        for (i=1;i<=n;i++)
            cin >> a[i];
        for (i=1;i<=n;i++)
            if (!v[i])
            {
                int len=1;
                int tmp=i;
                v[tmp]=true;
                while (!v[a[tmp]])
                {
                      tmp=a[tmp];
                      len++;
                      v[tmp]=true;
                }
                if (len>1)
                    ans+=len;
            }
        printf("Case #%d: %.6lf\n",t,ans);
    }
}
