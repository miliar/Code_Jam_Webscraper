#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int sort(const void *x, const void *y) {
	if (*(__int64*)x > *(__int64*)y) return 1;
	else if (*(__int64*)x == *(__int64*)y) return 0;
	else return -1; 
}

 
int main(void)
{	
	int T;	
	cin >> T;

	for (int a=0; a < T; a++)
	{
		cout << "Case #" << (a+1) << ": ";
		__int64 Low = 0;
		__int64 High = 0;
		int N = 0;
		cin >> N;
		cin >> Low;
		cin >> High;

		__int64 players[10000];
	
		for (int i = 0; i < N; i++) {
			cin >> players[i];	
		}

		qsort(players, N, sizeof(__int64), sort); 

		__int64 matched = 0;
		for (__int64 i=Low; i <= High; i++)
		{
			bool ok = true;
			for (int k=0; k < N; k++)
			{
				if (((players[k] % i) != 0) 
					&& ((i % players[k]) != 0))
				{
					ok = false;
					break;
				}
			}
			if (ok) {
				matched = i;
				break;
			}
		}

		if (matched != 0) cout << matched << "\n";
		else cout << "NO\n";
	}
}
		
