#include <fstream>
#include <istream>
#include <iostream>
#include <assert.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

int resolve2(int S, int P, std::vector<int> & t)
{
	int ret = 0;

	for (size_t i = 0; i < t.size(); i++)
	{
		int s1, s2, s3;
		int s = t[i];
		s1 = P;
		int left = s - s1;
		if (left < 0)
		{
			continue;
		}
		s2 = left / 2;
		s3 = left - s2;
		int min = std::min(s2, s3);
		int diff = s1 - min;

		if (diff < 2)
		{
			ret++;
		}
		else if (diff == 2)
		{
			if (S > 0)
			{
				S--;
				ret++;
			}
		}
	}

	return ret;
}

int resolve(int S, int P, std::vector<int> & t)
{
	int ret = 0;

	for (size_t i = 0; i < t.size(); i++)
	{
		int s = t[i];

		if (s >= 3*P - 2)
		{
			ret++;
		}
		else if (s >= 3*P - 4)
		{
			if (3*P - 4 < 0)
			{
				continue;
			}

			if (S > 0)
			{
				S--;
				ret++;
			}
		}
		else
		{
			continue;
		}

	}
	return ret;
}


int main(int argc, char *argv[])
{
	assert(argc == 2);

	ifstream ifs(argv[1], ifstream::in);

	int nline = 0;
	char line[1024];

	ifs.getline(line, sizeof(line) / sizeof(line[0]));

	nline = strtol(line, NULL, 10);

//	printf("%d\n", nline);

	for (int i = 1; i <= nline; i++)
	{

		int N = 0; // dancer number
		int S = 0; // supprising number
		int P = 0; // at least point
		std::vector<int> t; // total points of dancers

		// read input
		ifs >> N;
		ifs >> S;
		ifs >> P;

		for (int j = 0; j < N; j++)
		{
			int tmp = 0;
			ifs >> tmp;
			t.push_back(tmp);
		}

		ifs.getline(line, sizeof(line) / sizeof(line[0]));

//		printf("%d %d %d ", N, S, P);
//
//		for (size_t j = 0; j < t.size(); j++)
//		{
//			printf("%d ", t.at(j));
//		}
//		printf("\n");

		assert(size_t(N) == t.size());

		// resolve the case
		int result = resolve2(S, P, t);

		printf("Case #%d: %d\n", i, result);
	}

	return 0;
}
