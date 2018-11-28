#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


void main()
{
    int N = 0;
    cin >> N;
    
    int i;
    for(i = 0; i < N; i++)
    {
		int P;
		cin >> P;
		int K;
		cin >> K;
		int L;
		cin >> L;

		vector<long> freq(L);

		int j;
		for(j = 0; j < L; j++)
		{
			cin >> freq[j];
		}

		sort(freq.rbegin(), freq.rend());

		__int64 presses = 0;
		int keyPos = 1;
		int key = 1;
		bool possible = true;
		for(j = 0; j < L; j++)
		{
			presses += freq[j] * keyPos;
			
			key++;

			if (key > K)
			{
				key = 1;
				keyPos++;

				if (keyPos > P && j < L - 1)
				{
					possible = false;
					break;
				}
			}
		}
		
		if (possible)
	        cout << "Case #" << (i + 1) << ": " << presses << endl;
		else
			cout << "Case #" << (i + 1) << ": Impossible" << endl;
    }
}

