#include "iostream"

enum ScoreType {
	IMPOSSIBLE,
	REGULAR,
	SURPRISING
};


ScoreType scoreHigherThan(int score_given, int min_judge_score)
{
	ScoreType result = IMPOSSIBLE; // assume no result
	for (int itr = min_judge_score; itr <= 10; ++itr)
	{
		if (((3*itr)-4 == score_given) and result != REGULAR and itr-2 >= 0) result = SURPRISING;
		if (((3*itr)-3 == score_given) and result != REGULAR and itr-2 >= 0 and itr-1 >= 0) result = SURPRISING;
		if (((3*itr)-2 == score_given) and result != REGULAR and itr-1 >= 0) result = REGULAR;
		if (((3*itr)-1 == score_given) and result != REGULAR and itr-1 >= 0) result = REGULAR;
		if (((3*itr) == score_given) and result != REGULAR) result = REGULAR;
		if (((3*itr)+1 == score_given) and result != REGULAR and itr+1 <= 10) result = REGULAR;
		if (((3*itr)+2 == score_given) and result != REGULAR and itr+1 <= 10) result = REGULAR;
		if (((3*itr)+3 == score_given) and result != REGULAR and itr+2 <= 10 and itr+1 <= 10) result = SURPRISING;
		if (((3*itr)+4 == score_given) and result != REGULAR and itr+2 <= 10) result = SURPRISING;
	}

	return result;
}

int main()
{
	int test_number = 0;

	std::cin >> test_number;
	std::cin.ignore(1,'\n');

	for (int test_case = 0; test_case < test_number; ++test_case)
	{
		int num_possible = 0;
		int num_googlers, num_surprising, min_judge_score;
		std::cin >> num_googlers >> num_surprising >> min_judge_score;
		std::cin.ignore(1,'\n');
		for(int i = 0; i < num_googlers; ++i)
		{
			int score;
			std::cin >> score;
			ScoreType score_type = scoreHigherThan(score,min_judge_score);
			if (score_type == SURPRISING and num_surprising > 0) 
			{
				// std::cout << "Suprising for " << score << std::endl;
				++num_possible;
				--num_surprising;
			}	
			if (score_type == REGULAR)
			{
				// std::cout << "Not Suprising for " << score << std::endl;
				++num_possible;
			}
		}
		std::cin.ignore(1,'\n');

		std::cout << "Case #" << test_case+1 << ": " << num_possible << std::endl;
	}
}