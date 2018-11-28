#include <fstream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

ifstream in ("B.in");
ofstream out ("B.out");

int T;

vector <string> V;

int main()
{
	in >> T;
	for (int t = 0; t < T; ++t)
	{
		string S, s;
		in >> S;
		s = S;
		//V.clear();
		//sort(s.begin(), s.end());
		//V.push_back(s);
		if (next_permutation(s.begin(), s.end()))
		{
			out << "Case #" << t + 1 << ": " << s << "\n";
		}
		else
		{
			string tmp;
			sort (S.begin(), S.end());
			int y = 0;
			while (S[y] == '0')
			{
				++y;
			}
			swap(S[0], S[y]);
			tmp.push_back(S[0]);
			tmp.push_back('0');
			for (int i = 1; i < S.size(); ++i)
			{
				tmp.push_back(S[i]);
			}
			
			out << "Case #" << t + 1 << ": " << tmp << "\n";
		}
		/*while (next_permutation(s.begin(), s.end()))
		{
			V.push_back(s);
		}
		sort(V.begin(), V.end());
		int x = 0;
		while (x < V.size() && V[x] != S)
		{
			++x;
		}
		while (x < V.size() && V[x] == S)
		{
			++x;
		}
		if (x == V.size())
		{
			string tmp;
			sort (S.begin(), S.end());
			int y = 0;
			while (S[y] == '0')
			{
				++y;
			}
			swap(S[0], S[y]);
			tmp.push_back(S[0]);
			tmp.push_back('0');
			for (int i = 1; i < S.size(); ++i)
			{
				tmp.push_back(S[i]);
			}
			
			out << "Case #" << t + 1 << ": " << tmp << "\n";
			//out << "Case #" << t + 1 << ": " << S[0];
			//out << '0';
			//for (int i = 1; i < S.size(); ++i)
			//{
			//	out << S[i];
			//}
			//out << "\n";
		}
		else
		{
			out << "Case #" << t + 1 << ": " << V[x] << "\n";
		}
		*/
		
	}
	return 0;
}