#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int x;
	cin >> x;
	for(int i = 0; i < x; i++)
	{
		int N, S, p;
		cin >> N >> S >> p;

		std::vector< int > scores;
		for(int j = 0; j < N; j++)
		{
			int score;
			cin >> score;
			scores.push_back(score);
		}

		int total = 0;
		for(int j = 0; j < scores.size(); j++)
		{
			if( scores[j] >= p * 3 - 2 )
				total++;
			else if( scores[j] >= p * 3 - 4 && S > 0 && scores[j] >= 2 )
			{
				total++;
				S--;
			}
		}

		std::cout << "Case #" << i+1 << ": " << total << std::endl;
	}
	return 0;
}