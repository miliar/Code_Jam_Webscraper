#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;


int main()
{
	int T;
	cin>>T;
	for (int i = 0;i<T;i++)
	{
		int R, k, N;
		cin>>R;
		cin>>k;
		cin>>N;

		int g[1000];
		for (int j = 0; j < N; ++j) {
			cin>>g[j];
		}

		int gi_offset = 0;
		int euro = 0;
		for (int j = 0; j < R; ++j) {
			int people = 0;
			int gi = 0;
			while (people + g[(gi_offset + gi) % N] <= k) {
				people += g[(gi_offset + gi) % N];
				gi++;
				if (gi == N) break;
			}
			gi_offset = (gi_offset + gi) % N;
			euro += people;
		}

		printf("Case #%d: %d\n", i+1, euro);
	}

	return 0;
}
