#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main()
{
	int N, t, na, nb;

	//ifstream fin("B-small.in");
	//ofstream fout("B-small.out");
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");


	fin >> N;

	for (int tc = 1; tc <= N; ++tc)
	{
		string s;
		vector <pair<int,int> > v;

		fin >> t >> na >> nb;

		for (int i = 0; i < na; ++i)
		{
			fin >> s;
			int m = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
			v.push_back(make_pair(m, 2));
			fin >> s;
			m = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
			v.push_back(make_pair(m+t, 0));
		}

		for (int i = 0; i < nb; ++i)
		{
			fin >> s;
			int m = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
			v.push_back(make_pair(m, 3));
			fin >> s;
			m = (s[0]-'0')*600 + (s[1]-'0')*60 + (s[3]-'0')*10 + (s[4]-'0');
			v.push_back(make_pair(m+t, 1));
		}

		int a = 0, b = 0, sa = 0, sb = 0;

		sort(v.begin(), v.end());

		for (int i = 0; i < v.size(); ++i) {
			switch (v[i].second) {
				case 0:
					++sb;
					break;
				case 1:
					++sa;
					break;
				case 2:
					if (sa == 0) ++a;
					else --sa;
					break;
				case 3:
					if (sb == 0) ++b;
					else --sb;
					break;
			}
		}

		fout << "Case #" << tc << ": " << a << " " << b << endl;
	}

	fin.close();
	fout.close();

	return 0;
}