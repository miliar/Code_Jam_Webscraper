#include <fstream>
#include <set>
#include <string>
using namespace std;

set<string> s1, s2;
ifstream fin("A-small.in");
ofstream fout("A-small.out");

int main(void)
{
	char s[1000];
	int N;
	fin >> N;
	fin.getline(s, 1000);
	for (int test_no = 1; test_no <= N; test_no++)
	{
		s1.clear();
		int S, Q;
		fin >> S;
		fin.getline(s, 1000);
		for (int i = 0; i < S; i++)
		{
			fin.getline(s, 1000);
			s1.insert(s);
		}
		fin >> Q;
		fin.getline(s, 1000);
		int res = 0;
		s2 = s1;
		for (int i = 0; i < Q; i++)
		{
			fin.getline(s, 1000);
			s2.erase(s);
			if (s2.empty())
			{
				res++;
				s2 = s1;
				s2.erase(s);
			}
		}
		fout << "Case #" << test_no << ": " << res << endl;
	}
	return 0;
}
