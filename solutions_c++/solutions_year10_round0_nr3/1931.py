#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;
const int nmax = 2005;

long long g[nmax],sum[nmax],ans[nmax];
int pos[nmax],step[nmax];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	

	int ntest;
	scanf("%i\n",&ntest);

	for (int test = 1;test <= ntest; ++test){
		

		int r,k,n;
		cin >> r >> k >> n;
		memset(sum,0,sizeof(sum));
		memset(step,0,sizeof(step));
		memset(pos,0,sizeof(pos));

		for (int i = 0;i < n; ++i) cin >> g[i];
		for (int i = 0;i < n; ++i) g[i+n] = g[i];

		int t = 0;
		while (t < n && sum[0]+g[t] <= k)
		{
			sum[0] += g[t];
			++t;
		}

		pos[0] = t;

		if (pos[0] >= n) pos[0] = 0;
		for (int i = 1;i < n; ++i)
		{
			sum[i] = sum[i-1] - g[i-1];
			while (t < n + i && sum[i] + g[t] <= k)
			{
				sum[i] += g[t];
				++t;
			}
			pos[i] = t;
			if (pos[i] >= n) pos[i] -= n;
		}

		memset(ans,-1,sizeof(ans));

		t = 0;
		long long summ = 0;

		for (int i = 0;i < r;)
		{
			if (ans[t] == -1 || (ans[t] != -1 && (r-i) <= n))
			{
				step[t] = i;
				ans[t] = summ;
				summ += sum[t];
				t = pos[t];
				++i;
			}
			else
			{
				int len = i - step[t];

				int q = (r-i) / len;

				summ += ((long long)q) * (summ - ans[t]);
				i += q * len;
			}
		}
		
		printf("Case #%i: ",test);
		cout << summ;
		
		printf("\n");
	}


	
	return 0;
}