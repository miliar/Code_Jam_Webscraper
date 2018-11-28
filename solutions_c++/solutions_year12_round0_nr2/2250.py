#include <iostream>
#include <vector>
#include <sstream>
#include <set>
#include <stdexcept>
#include <fstream>

int MaxScore(int v)
{
	if( v % 3 == 0)
		return v / 3;
	return (v / 3) + 1;
}

int MaxScoreSurprising(int v)
{
	if( v == 0)
		return 0;
	return 1 + (v / 3) + ((v % 3 == 2) ? 1 : 0);

}

int Solve(std::vector<int> score, int s, int p)
{
	int goodScore = 0;

	for( size_t i = 0; i < score.size(); ++i)
	{
		if(MaxScore(score[i]) >= p)
			++goodScore;
		else if (s > 0 && MaxScoreSurprising(score[i]) >= p)
		{
			--s;
			++goodScore;
		}
	}
	return goodScore;
}

int main(int argc, char** argv)
{
/*	for( int i = 0; i < 20; i++)
	{
		std::cout << i <<  " " << MaxScore(i) << " " << MaxScoreSurprising(i) << std::endl;
	}*/

	//return 0;
	int nbTest = 0;
	std::ifstream ifs( "Debug/B-large.in");
	std::ofstream file( "Debug/B-large.out" );
	ifs >> nbTest;
	std::string line;
	std::getline(ifs, line);

	for( int test = 1; test <= nbTest; ++test )
	{
		int n, s, p;

		ifs >> n;
		ifs >> s;
		ifs >> p;
		std::vector<int> scores;

		for( int i = 0; i < n; ++i)
		{
			int score;

			ifs >> score;
			scores.push_back(score);
		}

		int maxScore = Solve(scores, s, p);

		std::cout << maxScore << std::endl;
		file << "Case #" << test << ": "<<  maxScore << std::endl;
	}
	std::cout << "Finish" << std::endl;
	return 0;
}
