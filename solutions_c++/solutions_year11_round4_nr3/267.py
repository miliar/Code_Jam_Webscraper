#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
const int maxn = 1000000 + 10;

int prime[maxn];
bool f[maxn+1];
int cnt;

int main()
{
	memset(f,false,sizeof(f));
	f[1]=true;
    cnt=0;
    for (int i = 2; i <= maxn; i++) {
		if (!f[i]) {
			prime[++cnt]=i;
            for (int j = maxn / i; j >= 2; --j)
				f[i * j] = true;
		}
	}

    int T;
    cin >> T;
	for (int loop = 1; loop <= T; loop++) {
		long long n;
		long long ans=0;

		cin >> n;
        for (int i = 1; i <= cnt; i++) {
			int cur=0;
			long long tmp=prime[i];
            while (tmp <= n) {
                ++cur;
				tmp = tmp * (long long)prime[i];
			}

			if (cur>0)
                ans += (long long)(cur - 1);
		}
		if (n != 1)
            ans++;
        cout << "Case #" << loop << ": " << ans << endl;
	}
    return 0;
}
