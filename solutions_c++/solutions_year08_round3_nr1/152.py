
#include <math.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define INF 100000000


int main()
{
	int N, P, K, L;
	vector <pair <int,int> > freq;
	cin >> N;
	
	for (int t = 0; t < N; t++)
	{
		cin >> P >> K >> L;
	

		freq.resize(L);	
		for (int i = 0; i < L; i++)
		{
			freq[i].second = i;
			cin >> freq[i].first;
		}
	
		sort(freq.begin(), freq.end());
		reverse(freq.begin(), freq.end());
	
		long long res = 0;
		int p = 1;
		int k = K;
		for (int i = 0; i < L; i++)
		{
			res += freq[i].first*p;
			k--;
			if (k == 0)
			{
				P--;
				p++;
				k = K;
			}
			
			if (P == 0)
				break;
		}
		
		cout << "Case #" << t+1 << ": " << res << endl;
	}

	return 0;
}
