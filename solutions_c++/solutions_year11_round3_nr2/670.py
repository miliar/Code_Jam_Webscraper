#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main(int argc, char** args)
{
	int T;
	cin >> T;
	
	for (int cas = 0; cas < T; cas++)
	{
		long long L, t;
		int	N, C;
		cin >> L >> t >> N >> C;
		//cout << L << " " << t << " " << N << " " << C;
		
		vector<int>	stars;
		stars.reserve(N);
		
		for (int c = 0; c < C; c++)
		{
			int a;
			cin >> a;
			
			for (int n = c; n < N; n += C)
				stars[n] = a;
		}
		
		/////////////////////
		
		vector<int>	speedup;
		speedup.reserve(N);
		
		////////////////////
		
		long long	totalTime = 0;
		long long	startTime = 0;
		for (int n = 0; n < N; n++)
		{
			long long	fullTime = stars[n] * 2;
			long long	endTime = startTime + fullTime;
			
			totalTime += fullTime * 2;

			if (startTime > t)
				speedup[n] = stars[n] * 2;
			else if (endTime > t)
				speedup[n] = endTime - t;
			else
				speedup[n] = 0;

			startTime += fullTime - speedup[n];
			//cout << speedup[n] << endl;
		}
		
		////////////////////

		for (int l = 0; l < L; l++)
		{
			int	id = 0;
			long long	biggest = 0;
			for (int n = 0; n < N; n++)
				if (biggest < speedup[n])
				{
					id = n;
					biggest = speedup[n];
				}
								
			speedup[id] = 0;
			totalTime -= biggest;
		}
		
		////////////////////
		
		cout << "Case #" << (cas+1) << ": " << (totalTime >> 1) << endl;
	}
}

