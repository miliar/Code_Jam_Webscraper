#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;




int main()
{
	int num_cases;
	int i;
	long long P;
	long long K;
	long long L;

	cin >> num_cases;

	for(i=0;i< num_cases;i++)
	{
		cin >> P;
		cin >> K;
		cin >> L;

		vector <long long> freqs;
		vector <long long> bins;

		for(int j =0; j < L; j++)
		{
			long long temp;
			cin >> temp;
			freqs.push_back(temp);
		}

		for(int j =0; j < K; j++)
		{
			bins.push_back(0);
		}

		sort(freqs.begin(),freqs.end());

		long long num_key_presses = 0;
		int notpossible = 0;
		for(int j=L-1;j >=0 ; j--)
		{
			if(bins[0] == P) { notpossible = 1; break; }

			bins[0]++;
			num_key_presses += (freqs[j]*bins[0]);
			sort(bins.begin(),bins.end());

		}
	
		if(notpossible)
		{
			cout << "Case #"<<i+1<<": Impossible"<<endl;
		}
		else
		{

			cout << "Case #"<<i+1<<": "<< num_key_presses<< endl;
		}

	}
}
