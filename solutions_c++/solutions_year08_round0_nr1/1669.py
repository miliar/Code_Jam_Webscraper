#include <fstream>
#include <iostream>
#include <string>
//#include <vector>
#include <map>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{
    int N;
    fin >> N;
	for (int n=0; n<N; n++)
	{
		int S, Q;
		fin >> S;
		map<string, int> sEngines;
		int* points = new int[S];
		for (int s=0; s<S; s++)
		{
			string str;
			do {
				getline(fin, str);
			} while(str == "");
			sEngines[str] = s;
		}

		fin >> Q;
		int* queries = new int[Q];		//the search engine ID for each query
		for (int q=0; q<Q; q++)
		{
			string str;
			do {
				getline(fin, str);
			} while (str == "");
			queries[q] = sEngines[str];
			//cout << queries[q] << endl;
		}

		int count = Q;
		int switches = 0;
		bool done = false;
		while(!done)
		{
			for (int s=0; s<S; s++)
				points[s] = 0;

			for (int i=1; i<=count; i++)
			{
				points[queries[Q-i]] = i;
			}

			int min = Q;
			for (int s=0; s<S; s++)
			{
				if (points[s] < min) min = points[s];
			}
			if (min == 0)
				done = true;
			else
			{
				switches++;
				count = min;
			}
		}

		fout << "Case #" << n+1 << ": " << switches << endl;
	}
    return 0;
}
