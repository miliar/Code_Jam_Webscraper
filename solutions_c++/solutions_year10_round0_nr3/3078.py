#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
    
	int t,cnt = 1;;
    cin >> t;
    for(int e = 0; e < t; e++)
    {
        long long ans = 0;
        int r,k,n;
        cin >> r >> k >> n;
        queue<int> q,mas[10000];
        int tmp;
        for(int i = 0; i < n; i++)
        {
            cin >> tmp;

            q.push(tmp);
        }

		int i = 0;
		while(i < r)
        {
			int l = 0,len = q.size();
			int cur = 0;
            while(cur + q.front() <= k && l++ < len)
            {
                int z = q.front();
                q.pop();
                q.push(z);
                cur += z;
            }
            ans += cur;
            cur = 0;
			i++;
        }
        cout << "Case #" << cnt++ <<": " << ans << endl;
    }
     return 0;
}
