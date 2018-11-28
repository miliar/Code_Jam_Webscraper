#include <iostream>
#include <fstream>
#include <vector>

bool need_to_be_surprising_p(int t, int minval)
{
	int minval_1 = (minval > 1) ? minval - 1 : 0;
	int minval_2 = (minval > 2) ? minval - 2 : 0;
	return (((minval >= 1) && (minval >= 2) && ((minval + (minval_1) + (minval_2)) == t)) // surp
			|| ((minval >= 2) && ((minval + 2*(minval_2)) == t))) // surp
		;
}

bool can_contain_p(int t, int minval)
{
	int minval_1 = (minval > 1) ? minval - 1 : 0;
	int minval_2 = (minval > 2) ? minval - 2 : 0;
	return ((3*minval <= t) // unsurp
		    || ((minval >= 1) && ((2*minval + (minval_1)) == t)) // unsurp
			|| ((minval >= 1) && ((minval + 2*(minval_1)) == t)) // unsurp
			|| ((minval >= 1) && (minval >= 2) && ((minval + (minval_1) + (minval_2)) == t)) // surp
			|| ((minval >= 2) && ((minval + 2*(minval_2)) == t)) // surp
		);
}

size_t process_case(std::ifstream& infile)
{
	size_t N;
	int S;
	int p;
	infile >> N >> S >> p;
	std::vector<int> t;
	std::vector<bool> used;
	size_t k = 0;
	for (size_t idx = 0; idx < N; ++ idx)
	{
		int tmp;
		infile >> tmp;
		t.push_back(tmp);
		used.push_back(false);
	}

	// first loop -- use up quota of surprising
	for (size_t idx = 0; (S>0) && (idx < t.size()); ++ idx)
	{
		if (used[idx])
			continue;

		bool can_contain = can_contain_p(t[idx], p);
		if (!can_contain)
			continue;

		bool need_to_be_surprising = can_contain && need_to_be_surprising_p(t[idx], p);
		if (can_contain && need_to_be_surprising && S > 0)
		{
			std::cerr << "Including " << idx << std::endl;
			-- S;
			++ k;
			used[idx] = true;
		}
	}

	// // second loop -- remove all cannot contain, but can be surprising
	// for (size_t idx = 0; (S>0) && (idx < t.size()); ++ idx)
	// {
	// 	if (used[idx])
	// 		continue;

	// 	bool can_contain = can_contain_p(t[idx], p);
	// 	bool can_be_surprising = can_be_surprising_p(t, p);
	// 	if (!can_contain && can_be_surprising && S > 0)
	// 		-- S;
	// }


	// third loop -- count remaining can contains but do not need to be surprising
	std::cerr << "final loop: " << std::endl;
	for (size_t idx = 0; idx < t.size(); ++ idx)
	{
		if (used[idx])
			continue;

		bool can_contain = can_contain_p(t[idx], p);
		if (!can_contain)
		{
			std::cerr << "cannot contain: "  << t[idx] << " index " << idx << std::endl;
			continue;
		}

		bool need_to_be_surprising = can_contain && need_to_be_surprising_p(t[idx], p);
		if (can_contain && !need_to_be_surprising)
		{
			std::cerr << "Including " << idx << std::endl;
			used[idx] = true;
			++ k;
		}
		else
		{
			// we're out of surprising quota
			continue;
		}
	}
	return k;
}

int main(int argc, char** argv)
{
	std::ifstream infile(argv[1]);
	std::ofstream outfile(argv[2]);

	size_t ncases;
	infile >> ncases;
	for (size_t idx = 0; idx < ncases; ++ idx)
	{
		std::cerr << "Processing case " << (idx + 1) << " of " << ncases << std::endl;
		size_t res = process_case(infile);
		outfile << "Case #" << (idx+1) << ": " << res << std::endl;
	}
	outfile.close();
	infile.close();

	return 0;
}
