#include <iostream>
#include <iostream>
using namespace std;
const int MAXN = 1001;
int a[MAXN];
long long cnt[MAXN];
bool v[MAXN];
int vis[MAXN];
int main()
{
    freopen("C-large1.in","r",stdin);
    freopen("C-large1.out","w",stdout);
    
    int cas,r,k,n;
    scanf("%d",&cas);
    for (int T = 1;T <= cas;T++)
    {
        memset(vis,0,sizeof(vis));
        scanf("%d%d%d",&r,&k,&n);
        for (int i = 0;i < n;i++)
            scanf("%d",&a[i]);
        int l = 0,x = 0,h = 0;
        for (int i = 1;i <= r;i++)
        {
            vis[l] = i;
            long long sum = 0;
            memset(v,0,sizeof(v));
            while (sum + a[l] <= k)
            {
                if (v[l])
                    break;
                v[l] = true;
                sum += a[l];
                l = (l + 1) % n;
            }
            cnt[i] = sum;
            //ans += sum;
            x++;
            if (vis[l])
            {
                h = vis[l];
                break;
            }
        }
        //cout << 'h' << h << endl;
        //cout << 'x' << x << endl;
        long long sum = 0,ans = 0;
        
        for (int i = 1;i < h;i++)
            ans += cnt[i];
        for (int i = h;i <= x;i++)
            sum += cnt[i];
            //cout << i << ' ' << cnt[i] << endl;
        //if (r >= x)
        ans += ((r-h+1) / (x-h+1)) * sum;
        for (int i = 0;i < ((r-h+1) % (x-h+1));i++)
                ans += cnt[h+i];
        printf("Case #%d: %lld\n",T,ans);
    }
}
