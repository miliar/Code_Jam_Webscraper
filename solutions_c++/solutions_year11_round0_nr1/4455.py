#include <fstream>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define max(x, y) x>y?x:y
#define min(x, y) x<y?x:y


int main()
{
	ifstream input ("A-small.in");
	ofstream output ("A-small.out");
	

	int i, j, t;
	int T, N;
	int distance, time;
	int r1Pos, r2Pos, oneStepTime;
	char robotName;
	pair<char, int> anCommand;	
	
	
	input >> T;

	for(t = 0; t < T; ++t)
	{
		vector<pair<char, int>> orders;
		input >> N;
		time = 0;
		oneStepTime = 0;
		r1Pos = 1;
		r2Pos = 1;

		for(i = 0; i < 2*N; i=i+2)
		{
			input >> robotName;
			input >> distance;

			anCommand.first = robotName;
			anCommand.second = distance;
			orders.push_back(anCommand);

		}

		for(i = 0; i < N; ++i)
		{
			oneStepTime = abs(r1Pos - orders[i].second) + 1;
			time = time + oneStepTime;

			if(i == N-1)
				break;

			r1Pos = orders[i].second;

			for(j = i+1; j < N; ++j)
			{
				if(orders[i].first == orders[j].first)
					continue;
				
				if(orders[j].second > r2Pos)
					r2Pos = min(r2Pos + oneStepTime, orders[j].second);
				else if(orders[j].second < r2Pos)
					r2Pos = max(r2Pos - oneStepTime, orders[j].second);
				else
					;

				break;
			}
		

			if(orders[i].first != orders[i+1].first)
			{
				int tmp;
				tmp = r1Pos;
				r1Pos = r2Pos;
				r2Pos = tmp;
			}
		
		}

		output << "Case #" << t+1 << ": " << time << endl;
		

	}

	return 0;
}