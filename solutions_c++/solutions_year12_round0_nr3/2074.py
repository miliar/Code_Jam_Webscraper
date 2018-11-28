#include "stdafx.h"

#define PROBLEM_NAME "Prob_C"
#define PROBLEM_SMALL_INPUT "C-small-attempt0"
#define PROBLEM_LARGE_INPUT "C-large"

bool less_than(char* strA, size_t offsetA, char* strB, size_t offsetB, size_t len)
{
	for (size_t i=0; i<len; ++i)
	{
		char chA = strA[(i+offsetA)%len];
		char chB = strB[(i+offsetB)%len];
		if (chA < chB)
			return true;
		else if (chA == chB)
			continue;
		else
			return false;
	}
	return false;
}

int main(int argc, char* argv[])
{
//	set_fio(PROBLEM_NAME ".txt");
//	set_fio(PROBLEM_NAME ".txt", PROBLEM_NAME ".out.txt");
//	set_fio(PROBLEM_SMALL_INPUT ".in");
//	set_fio(PROBLEM_SMALL_INPUT ".in", PROBLEM_SMALL_INPUT ".out.txt");
//	set_fio(PROBLEM_LARGE_INPUT ".in");
	set_fio(PROBLEM_LARGE_INPUT ".in", PROBLEM_LARGE_INPUT ".out.txt");

/*
	bool b1 = less_than("1234", 0, "1235", 0, 4);
	bool b2 = less_than("1234", 0, "1234", 0, 4);
	bool b3 = less_than("1235", 0, "1234", 0, 4);
	bool b4 = less_than("1567", 0, "2123", 0, 4);
	bool b5 = less_than("2345", 0, "1234", 0, 4);
	bool b6 = less_than("2000", 0, "1444", 0, 4);
*/
	int T;
	fin >> T;

	for (int cases=1; cases<=T; ++cases)
	{
		int iA, iB;
		fin >> iA >> iB;
		char A[128], B[128], n[128];
		sprintf(A, "%d", iA);
		sprintf(B, "%d", iB);
		size_t len = strlen(A);

		set<string> check;

		int count = 0;
		for (int in=iA; in<=iB; ++in)
		{
			sprintf(n, "%d", in);
			for (size_t i=0; i<len; ++i)
			{
				// (n,i) == m
				if (less_than(n, i, A, 0, len))
					continue;
				if (less_than(B, 0, n, i, len))
					continue;
				if (!less_than(n, 0, n, i, len))
					continue;

				string s = n;
				s += ',';

				//fout << "(" << n << ", ";
				for (size_t j=0; j<len; ++j)
				{
					char ch = n[(i+j)%len];
					//fout << ch;
					s += ch;
				}
				//fout << ")" << endl;

				set<string>::iterator it = check.find(s);
				if (it == check.end())
				{
					check.insert(s);
					count++;
				}
			}
		}

		fout << "Case #" << cases << ": " << count << endl;
	}

	return 0;
}
