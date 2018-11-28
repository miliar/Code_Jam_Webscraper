#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

int main(int argc, char* argv)
{
	int cases;
	cin >> cases;
	int S, P, N, R;

	for(int i = 0; i < cases; i++)
	{
		cin >> N;
		cin >> S;
		cin >> P;
		R = 0;
		int scores[N];
		
		for(int k = 0; k < N; k++)
		{
			cin >> scores[k];
		}
		
		for(int k = 0; k < N; k++)
		{
			int trip[3] = {0, 0, 0};
			
			while(scores[k] > 3)
			{
				trip[0] += 1;
				trip[1] += 1;
				trip[2] += 1;
				scores[k] -= 3;
			}
			
			if(scores[k] == 3)
			{
				if(trip[0] + 2 == P)
				{
					if(S > 0)
					{
						trip[0] += 2;
						trip[1] += 1;
						scores[k] -= 3;
						S -= 1;
					}
					else
					{
						trip[0] += 1;
						trip[1] += 1;
						trip[2] += 1;
						scores[k] -= 3;
					}
				}
				else
				{
					trip[0] += 1;
					trip[1] += 1;
					trip[2] += 1;
					scores[k] -= 3;
				}
			}
			else if(scores[k] == 2)
			{
				if(trip[0] + 2 == P)
				{
					if(S > 0)
					{
						trip[0] += 2;
						scores[k] -= 2;
						S -= 1;
					}
					else
					{
						trip[0] += 1;
						trip[1] += 1;
						scores[k] -= 2;
					}
				}
				else
				{
					trip[0] += 1;
					trip[1] += 1;
					scores[k] -= 2;
				}
			}
			else if(scores[k] == 1)
			{
				trip[0] += 1;
				scores[k] -= 1;
			}
						
			if(trip[0] >= P || trip[1] >= P || trip[2] >= P)
			{
				R += 1;
			}
		}
		
		cout << "Case #" << (i+1) << ": " << R << endl;
	}
	
	return 0;
}
