#include <iostream>
#include <sstream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

#define MAXS 100
#define MAXQ 1000
#define MAXNAME 100


#ifndef UINT32_MAX
#define UINT32_MAX 4294967295U
#endif

using namespace std;

int get_line_number()
{
	int n;

	string s_temp;
	getline(cin, s_temp);
	istringstream s_temp2(s_temp);
	s_temp2 >> n;

	return n;
}


int main()
{
	int N;
	N = get_line_number();
	for (int n=1; n<=N; n++)
	{
		string s_names[MAXS];
		map<string, int> s_numbers;
		int S;

		S = get_line_number();
		for (int s = 0; s < S; s++)
		{
			string search_name;
			getline(cin, search_name);
			s_names[s] = search_name;
			s_numbers[search_name] = s;
		}

		int queries[MAXQ];
		int Q;
		Q = get_line_number();
		for (int q = 0; q < Q; q++)
		{
			string search_name;
			getline(cin, search_name);
			queries[q] = s_numbers[search_name];
		}

		int Y = 0;
		int *qbegin = queries;
		while (qbegin != queries+Q)
		{
			int *nextsearch = qbegin;
			for (int s = 0; s < S && nextsearch != queries+Q; s++)
			{
				int *candidate = find(qbegin, queries+Q, s);
				if (candidate > nextsearch)
				{
					nextsearch = candidate;
				}
			}

			if (nextsearch != queries+Q)
				Y++;

			qbegin = nextsearch;
		}


		cout << "Case #" << n << ": " << Y << endl;
	}
}

