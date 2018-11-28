#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dist[1000010];

main ()
{
	int t;
//	freopen( "sample.txt", "r", stdin ); freopen( "sample-o.txt", "w", stdout );
//	freopen( "B-small-attempt0.in", "r", stdin ); freopen( "B-small-attempt0.out", "w", stdout );
	freopen( "B-large.in", "r", stdin ); freopen( "B-large.out", "w", stdout );
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int L,N,C;
		long long ti;

		cin >> L >> ti >> N >> C;
		int arr[C];
		for (int i = 0; i < C; i++) cin >> arr[i];

		for (int i = 0; i < N; i++)
		{
			dist[i] = arr[i % C];
		}
	
		long long tot = 0;
		for (int i = 0; i < N; i++)
		{
			tot += dist[i]*2;
			if (tot >= ti)
			{
				
				dist[N] = (tot-ti)/2;
				sort(dist+i+1,dist+N+1);
				reverse(dist+i+1,dist+N+1);
				int rem = N-i;
				tot = ti;
				for (int j = 1; j <= min(rem,L); j++)
				{
					tot += dist[i+j];
				}
				
				if (L < rem)
				{
					for (int j = L+1; j <= rem; j++) tot += dist[i+j]*2;
				}
				break;
			}
		}

		cout << "Case #" << T << ": " << tot << "\n";
	}
}
