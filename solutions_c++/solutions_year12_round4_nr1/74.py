#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

int n;
int d[20000];
int h[20000];
int f[20000];
int L;

int main()
{
    freopen("A-largee.in","r",stdin);
    freopen("a.out","w",stdout);
    int NT,CT=0;
    cin >> NT;
    while (NT)
    {
        NT--;CT++;
        cin >> n;
        for (int i=0;i<n;i++) cin >> d[i] >> h[i];
        cin >> L;
        
        for (int i=1;i<n;i++) f[i]=-1;
        f[0]=d[0];
        
        for (int i=1;i<n;i++)
        {
            for (int j=0;j<i;j++) if (f[j]>=d[i]-d[j])
            {
                int l;
                if (d[i]-d[j]>h[i]) l=h[i];else l=d[i]-d[j];
                if (f[i]<l) f[i]=l;
                break;
            }
            
        }
        
    //    for (int i=0;i<n;i++) cout << f[i] << ' ';cout << endl;
        
        int ans=0;
        for (int i=0;i<n;i++) if (f[i]+d[i]>=L) ans=1;
        
        if (ans==1) printf("Case #%d: YES\n",CT);else printf("Case #%d: NO\n",CT);
    }
}
        
    
