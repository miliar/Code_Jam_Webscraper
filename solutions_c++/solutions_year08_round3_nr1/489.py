#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <deque>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

typedef long long ll;


int main()
{
	int ncases;

	int P, K, L;
	int * freq = new int[1000];


	cin >> ncases;
	for(int k = 0; k < ncases; k++)
	{

		cin >> P >> K >> L;
		for(int i = 0; i < L; i++)
			cin >> freq[i];

		sort(freq, freq + L, greater<int>());
		ll sum = 0;

		for(int i = 0; i < L; i++)
		{
			sum += freq[i] * (i / K + 1);
		}


		cout<<"Case #"<<(k + 1)<<": "<<sum<<endl;
	}

	return 0;
}


