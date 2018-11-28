#include <iostream>
#include <cstring>

using namespace std;

int g[1024], h[1024];
int J[1024];
int V[1024];

int main()
{
	int T;
	cin >> T;
	for(int cn = 1; cn <= T; cn++)
	{
		int R, k, N;
		cin >> R >> k >> N;
		for(int i = 0; i < N; i++) cin >> g[i];
		for(int i = 0; i < N; i++)
		{
			J[i] = i;
			int tot = g[i];
			do
			{
				J[i]++; J[i] %= N;
				tot += g[J[i]];
			} while(J[i] != i && tot <= k);
			h[i] = tot - g[J[i]];
		}
		memset(V,0,sizeof(V));
		int curr = 0;
		while(!V[curr])
		{
			V[curr] = 1;
			curr = J[curr];
		}
		long long res = 0;
		int pcurr = 0;
		while(pcurr != curr && R)
		{
			res += h[pcurr];
			pcurr = J[pcurr];
			R--;
		}
		long long pro = 0;
		int len = 0;
		do
		{
			pro += h[pcurr];
			len++;
			pcurr = J[pcurr];
		} while(pcurr != curr);
		int fu = R / len;
		res += pro*fu;
		R %= len;
		while(R)
		{
			res += h[pcurr];
			pcurr = J[pcurr];
			R--;
		}
		cout << "Case #" << cn << ": " << res << endl;
	}
	return 0;
}
