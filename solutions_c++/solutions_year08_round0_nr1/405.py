#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;


int main()
{
	int N, ns, nq;

	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");


	fin >> N;

	for (int tc = 1; tc <= N; ++tc)
	{
		string s;

		fin >> ns;
		getline(fin, s);

		for (int i = 0; i < ns; ++i)
			getline(fin, s);

		fin >> nq;
		getline(fin, s);

		set <string> q;
		int cnt = 0;
		for (int i = 0; i < nq; ++i)
		{
			getline(fin, s);
			q.insert(s);
			if (q.size() == ns) {
				++cnt;
				q.clear();
				q.insert(s);
			}
		}

		fout << "Case #" << tc << ": " << cnt << endl;
	}

	fin.close();
	fout.close();

	return 0;
}