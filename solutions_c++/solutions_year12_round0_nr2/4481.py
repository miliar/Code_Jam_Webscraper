#include<iostream>
#include<vector>
#include<map>
#include<fstream>
#include<algorithm>

using namespace std;

int main()
{
	ifstream fin ("in.in");
	ofstream fout ("out.out");
	int caso = 1;
	int T;
	fin >> T;
	
	int n, s, p;
	for (; T > 0; T--)
	{
		fin >> n >> s >> p;
		vector<int> v (n);
		for (int i = 0; i < n; i++) fin >> v[i];
		int res = 0, ct = 0;
		for (int i = 0; i < n; i++)
		{
			if (v[i] == 0 && p > 0) continue;
			if (v[i] >= p*3-2)
			{
				res++;
			}
			else if (v[i] >= p*3-4 && ct < s)
			{
				res++;
				ct++;
			}
		}
	
		fout << "Case #" << caso << ": " << res << endl;
		caso++;
	}
}
