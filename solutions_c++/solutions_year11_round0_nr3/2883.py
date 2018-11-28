#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

int main(int argc, char** args)
{
	unsigned int T;
	cin >> T;
	
	for (unsigned int t = 0; t < T; t++)
	{
		unsigned int N;
		cin >> N;
	
		vector<unsigned int>	candies;
		candies.reserve(N);
	
		for (unsigned int i = 0; i < N; i++)
		{
			unsigned int c;
			cin >> c;
			candies.push_back(c);
		}
		
		sort(candies.begin(), candies.end());
		
		char*	value = new char[N];
		unsigned int 	sr = 0, pr = 1; // Real
		unsigned int 	sx = 0, px = 1; // XOR
		
		for (unsigned int i = 0; i < N; i++)
			value[i] = (i == 0) ? 1 : 0;
			
		bool	 		found = false;
		unsigned int	bestSeanValue = 0;	
		
		while (true)
		{		
			// Calculate values
			sr = pr = sx = px = 0;
			for (unsigned int i = 0; i < N; i++)
			{
				//cout << (int)value[i] << ", ";
			
				if (value[i] == 0)
				{
					sr += candies[i];
					sx ^= candies[i];
				}
				else
				{
					pr += candies[i];
					px ^= candies[i];
				}
			}
			
			if (sx == px)
			{
				found = true;
				if (bestSeanValue < sr) bestSeanValue = sr;
			}
			
			//cout << endl;
			//cout << sr << " (" << sx << ") - " << pr << " (" << px << ")" << endl;
			
			// Next permuation
			bool done = false;
			for (unsigned int i = 0; i < N; i++)
			{
				if (value[i] == 0)
				{
					value[i] = 1;
					break;
				}
				
				value[i] = 0;
				if (i == N - 1) done = true;
			}
			
			if (done) break;
		}
		
		delete [] value;
		
		if (found)
			cout << "Case #" << (t+1) << ": " << bestSeanValue << endl;
		else
			cout << "Case #" << (t+1) << ": NO" << endl;	
	}
}

