#include "stdafx.h"

#include <vector>
#include <string>
#include <fstream>
using namespace std;

int solve(const vector<string>& ss, const vector<string>& query)
{
	int s = ss.size(), q = query.size();
	vector<vector<int>> A(q+1, vector<int>(s, 100000));

	for (int i = 0; i < s; ++i)
	{
		A[q][i] = 0;
	}

	for (int j = q-1; j >= 0; --j)
	{
		for (int i = 0; i < s; ++i)
		{
			if (ss[i] != query[j])
			{
				A[j][i] = A[j+1][i];
			}
			for (int k = 0; k < s; ++k) if (k != i)
			{
				A[j][i] = min(A[j][i], 1+A[j+1][k]);
			}
		}
	}

	int ret = INT_MAX;
	for (int i = 0; i < s; ++i) ret = min(ret, A[0][i]);
	return ret;
}

int main()
{
	FILE* fin = fopen("A.in", "rt");
	FILE* fout = fopen("A.out", "wt");

	int numCase;
	fscanf(fin, "%d", &numCase);

	for (int caseNo = 1; caseNo <= numCase; ++caseNo)
	{
		int s,q;
		vector<string> ss;
		vector<string> query;

		fscanf(fin, "%d\n", &s);
		for (int i = 0; i < s; ++i)
		{
			char buf[200];
			fgets(buf, sizeof(buf), fin);
			buf[strlen(buf)-1] = 0;
			ss.push_back(buf);
		}
		fscanf(fin, "%d\n", &q);
		for (int i = 0; i < q; ++i)
		{
			char buf[200];
			fgets(buf, sizeof(buf), fin);
			buf[strlen(buf)-1] = 0;
			query.push_back(buf);
		}

		fprintf(fout, "Case #%d: %d\n", caseNo, solve(ss, query));
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
