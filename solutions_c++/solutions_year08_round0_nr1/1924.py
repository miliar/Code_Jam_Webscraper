#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

void main()
{
	ifstream in("A-large.in");
	ofstream out("Alarge.out");

	int tc;
	in >>tc;
	for (int cc = 0;cc < tc;cc++)
	{
		map<string, int> eng;
		int s, q, e;
		e = 0;
		in >>s;
		char buf[102];
		in.getline(buf, 101);
		for (int i = 0;i < s;i++)
		{			
			in.getline(buf, 101);
			string ce;
			ce = buf;
			eng[ce] = e++;
		}
		in >>q;
		vector <int> queries(q);
		in.getline(buf, 101);
		for (int i = 0;i < q;i++)
		{
			in.getline(buf, 101);
			string cq;
			cq = buf;
			queries[i] = eng[cq];
		}

		vector <vector<int> > P(s, vector<int>());
		for (int i = 0;i < s;i++)
			for (int j = 0;j < q;j++)
				if (queries[j] == i)
					P[i].push_back(j);

		int res = 0;
		int pos = 0;


		while (1)
		{
			int mi, mj;
			mi = mj = -1;
			for (int i = 0;i < s;i++)
			{
				int j = 0;
				while (j < P[i].size() && P[i][j] < pos)
					j++;

				if (j >= P[i].size())
					goto out;

				if (mi == -1 || P[i][j] > P[mi][mj])
				{
					mi = i;
					mj = j;
				}
			}

			pos = P[mi][mj];
			res++;
		}
out:;
		out <<"Case #"<<cc + 1 <<": " <<res <<endl;
	}
}
