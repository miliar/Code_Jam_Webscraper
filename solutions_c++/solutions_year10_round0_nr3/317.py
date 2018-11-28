#include <iostream>
#include <cstdio>
#include <cstring>
#include <deque>

using namespace std;

const int maxn = 1005;
long long a[maxn*2],c[maxn*2];
int h[maxn];
deque<int> q,wait;

int main()
{
    freopen("C.in","r",stdin); freopen("C.out","w",stdout);
    int t; scanf("%d",&t);
    for (int casenum=1; casenum <= t; ++casenum){
        long long r,k; int n;
        cin >> r >> k >> n;
        q.clear();
        for (int i=1; i<=n; ++i){
            cin >> a[i]; q.push_back(i);
        }
        memset(h,0,sizeof(h));
        int now = 1,t = 0;
        while (!h[now]){
            h[now] = ++t; c[t] = 0; wait.clear();
            while (!q.empty()){
                if (c[t] + a[q[0]] > k) break;
                c[t] += a[q[0]]; wait.push_back(q[0]); q.pop_front();
            }
            while (!wait.empty()){
                q.push_back(wait[0]); wait.pop_front();
            }
            now = q[0];
        }
        long long len = t-h[now]+1;
        long long ans = 0;
        for (int i=1; i<=t-len; ++i)
            ans += c[i];
        r -= (t-len);
        long long circle = 0;
        for (int i=t-len+1; i<=t; ++i)
            circle += c[i];
        long long d = r/len; ans += circle * d;
        long long rest = r%len;
        for (int i=t-len+1; i<=t-len+rest; ++i)
            ans += c[i];
        printf("Case #%d: ",casenum); cout << ans << endl;
    }
    return 0;
}
