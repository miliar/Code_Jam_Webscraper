#include <iostream>
#define maxn 100100
using namespace std;

int tn;
int a,b;
double prob[maxn];
double p[maxn];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i;
    cin >> tn;
    for (int t=1;t<=tn;t++)
    {
        cin >> a >> b;
        memset(p,0,sizeof p);
        p[0] = 1;
        for (i=1;i<=a;i++)
        {
            cin >> prob[i];
            p[i] = p[i-1]*prob[i];
        }   
        double ans = b+2;
        for (i=0;i<=a;i++)
        {
            double tmp = p[i]*(a+b-2*i+1) + (1-p[i])*(a+2*b-2*i+2);
            ans = min(tmp,ans);
        }
        printf("Case #%d: %.8lf\n",t,ans);
        //cout << "Case #" << t << ": " << ans << endl;
    }
}
