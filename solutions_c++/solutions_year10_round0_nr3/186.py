#include <cstdlib>
#include <cstdio>
#include <vector>
using namespace std;

int G[1001];
int GC[1001];
long long GK[1001];

int VR[1001];
long long VK[1001];

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int R, K, N;
		memset(G, 0x00, sizeof(G));
		memset(GC, 0x00, sizeof(GC));
		memset(GK, 0x00, sizeof(GK));
		memset(VR, 0x00, sizeof(VR));
		memset(VK, 0x00, sizeof(VK));

		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; i++) scanf("%d", &G[i]);
		
		for (int i = 0; i < N; i++)
		{
			int j = i;
			int c = 0;
			long long k = 0;			
			while (k + G[j] <= K && c < N) {
				c = c + 1;
				k = k + G[j];
				j = (j + 1) % N;				
			}
			GC[i] = c;
			GK[i] = k;			
		}

		int i = 0;
		int r = 0;
		long long k = 0;		
		while (r < R && VR[i] == 0)
		{
			r = r + 1;
			VR[i] = r;
			VK[i] = k;
			k = k + GK[i];
			i = (i + GC[i]) % N;
		}
		int cl = r - VR[i] + 1;
		long long ck = k - VK[i];
		int rm = R - r;
		int cc = rm / cl;
		k = k + cc * ck;
		r = r + cc * cl;
		while (r < R)
		{
			r = r + 1;
			k = k + GK[i];
			i = (i + GC[i]) % N;
		}
		printf("Case #%d: %lld\n", t, k);
	}
	return 0;
}