#include <iostream>
#include <stdio.h>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int nTestCases;
	int N, M;

	FILE *in_file;
	FILE *out_file;

	in_file = fopen("prob1_in.txt", "r");
	out_file = fopen("prob1_out.txt", "w+");

#define in_file stdin
#define out_file stdout

	if (in_file == NULL || out_file==NULL)
		return 0;

	fscanf(in_file, "%d\n", &nTestCases);

	for (int i=1; i<=nTestCases; ++i)
	{
		set<string> adirs;
		set<string> rdirs;
		char str[256];

		fscanf (in_file, "%d", &N);
		fscanf (in_file, "%d", &M);

		adirs.insert(string("/"));
		for (int k=0; k<N; ++k)
		{
			fscanf (in_file, "%s", str);
			adirs.insert(string(str));
		}

		int cnt=0;
		for (int k=0; k<M; ++k)
		{
			fscanf (in_file, "%s", str);

		//	rdirs.insert(string(str));
		//}

		//for (set<string>::iterator it=rdirs.begin(); it!=rdirs.end(); ++it)
		//{
			string st(str);// = *it;

			string::size_type sz=st.find("/", 1);
			while (sz != string::npos)
			{
				string stt = st.substr(0, sz);
				if (adirs.find(stt) == adirs.end())
				{
					++cnt;
					adirs.insert(stt);
				}

				sz = st.find("/", sz+1);
			}

			string stt=st.substr(0, sz);
			if (adirs.find(stt) == adirs.end())
			{
				++cnt;
				adirs.insert(stt);
			}


			//rdirs.insert(string(str));
		}

		fprintf (out_file, "Case #%d: %d\n", i, cnt);
	}


	fclose(in_file);
	fclose(out_file);

	return 0;
}
