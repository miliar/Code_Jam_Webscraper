// A.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <vector>

std::ifstream in ("A.in");
std::ofstream out ("A.out");

int N, S, Q;


std::vector <std::string> engines;
std::vector <std::string> queries;


void input()
{
	engines.clear();
	queries.clear();


	in >> S;

	std::string str = "";
	std::getline (in, str);
	for (int i=0; i<S; i++)
	{
		std::getline (in, str);
		engines.push_back (str);
	}

	in >> Q;
	std::getline (in, str);
	for (int i=0; i<Q; i++)
	{
		std::getline (in, str);
		queries.push_back (str);
	}
}



int solve(int start)
{
	if (start >= queries.size())
	{
		return 0;
	}
	int max = 0;
	for (int i=0; i<engines.size(); i++)
	{
		int m = 0;
		for (int k=start; k<queries.size(); k++)
		{
			if (engines[i] == queries[k])
				break;
			m++;
		}
		if (m > max)
			max = m;
	}
	
	if (start + max >= queries.size())
		return 0;

	return 1 + solve (start + max);
}

int main()
{
	in >> N;
	for (int k=0; k<N; k++)
	{
		input();
		out << "Case #" << k+1 << ": " << solve(0) << "\n";
	}
	return 0;
}

