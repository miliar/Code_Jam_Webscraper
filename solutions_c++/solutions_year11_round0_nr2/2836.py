#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef std::pair<char, char> Oppose;
typedef std::pair<std::pair<char, char>, char> Combination;



void
exec_test(int test_id)
{
	std::vector<Oppose> oppose;
	std::vector<Combination> combination;
	std::vector<char> sequence;

	int n_comb = 0;
	scanf("%d", &n_comb);
	for (int i = 0; i < n_comb; ++i)
	{
		char buf[3];
		scanf("%*[ ]%3[A-Z]", buf);
		combination.push_back(make_pair(make_pair(buf[0], buf[1]), buf[2]));
	}

	int n_oppo = 0;
	scanf("%d", &n_oppo);
	for (int i = 0; i < n_oppo; ++i)
	{
		char buf[2];
		scanf("%*[ ]%3[A-Z]", buf);
		oppose.push_back(make_pair(buf[0], buf[1]));
	}

	int n_seq = 0;
	scanf("%d", &n_seq);
	scanf("%*[ ]");
	for (int i = 0; i < n_seq; ++i)
	{
		int ch = getchar();
		sequence.push_back((char)ch);
	}

	//printf("========== for testcase %d ==========\n", test_id + 1);
	//printf("---combinations---\n");
	//for (auto iter = combination.begin(); iter != combination.end(); ++iter)
	//{
	//	auto c = (*iter).first;
	//	auto r = (*iter).second;
	//	printf("%c %c => %c\n", c.first, c.second, r);
	//}
	//printf("---oppositions---\n");
	//for (auto iter = oppose.begin(); iter != oppose.end(); ++iter)
	//{
	//	printf("%c <-> %c\n", (*iter).first, (*iter).second);
	//}

	//printf("---sequence---\n");
	//for (auto iter = sequence.begin(); iter != sequence.end(); ++iter)
	//{
	//	printf("%c -> ", *iter);
	//}
	//printf("\n");
	

	std::vector<char> result;
	for (auto iter = sequence.begin(); iter != sequence.end(); ++iter)
	{
		// just append invocation once.
		result.push_back(*iter);

		// apply combination
		for (auto c = combination.begin(); c != combination.end(); ++c)
		{
			auto comb = (*c).first;
			if ((comb.first == result[result.size()-1] && comb.second == result[result.size()-2])
					|| (comb.first == result[result.size()-2] && comb.second == result[result.size()-1]))
			{
				result.pop_back();
				result.pop_back();
				result.push_back((*c).second);
			}
		}

		// apply oppositions
		for (auto o = oppose.begin(); o != oppose.end(); ++o)
		{
			auto rr = std::find(result.begin(), result.end(), (*o).first);
			if (rr == result.end()) break; // break if not found.
			auto ll = std::find(result.begin(), result.end(), (*o).second);
			if (ll == result.end()) break; // break if not found.

			// clear list
			result.clear();
		}
	}

	printf("Case #%d: [", test_id + 1);
	int iii = 0;
	for (auto iter = result.begin(); iter != result.end(); ++iter)
	{
		printf(iii++ == 0 ? "%c" : ", %c", *iter);
	}
	printf("]\n");

	// FIXME: test_id must start with 1
}

int
main(int argc, char const **argv)
{
	int n_testcases = 0;
	scanf("%d", &n_testcases);

	for (int i = 0; i < n_testcases; ++i)
		exec_test(i);
	
	return 0;
}
