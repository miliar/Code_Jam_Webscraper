#include<iostream>

using namespace std;

int x[10000];
int v[10000];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N,K,B,time;
		cin >> N >> K >> B >> time;
		for (int i = 0; i < N; i++) cin >> x[i];
		for (int i = 0; i < N; i++) cin >> v[i];
		int s1 = 0;
		int s2 = 0;
		int ans = 0;
		for (int i = N - 1  ; i >= 0; i--)
		{
			if (v[i] * time >= B - x[i])
			{
				ans += s2;
				s1 ++;
			}
			else s2 ++;
			if (s1 == K) break;
		}	
		cout << "Case #" << t + 1 << ": ";
		if (K != s1) cout << "IMPOSSIBLE" << "\n"; else cout << ans << "\n";
		
	}
}
