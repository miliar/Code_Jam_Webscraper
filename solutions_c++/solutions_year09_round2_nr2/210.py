#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

//#define ONLINE

int main()
{

	ifstream in("B-large.in");
	ofstream out("out.txt");

	int n;
	in >>n;
	for (int i = 0;i < n;i++)
	{
		string s;
		in >>s;
		string copy = s;
		if (!next_permutation(s.begin(), s.end()))
		{
			int imin = -1;
			for (int i = 0;i < s.size();i++)
				if (s[i] != '0' && (imin == -1 || s[i] < s[imin]))
					imin = i;

			char c = s[imin];
			s.erase(s.begin() + imin);

			sort(s.begin(), s.end());
			string ss;
			ss += c;
			s.insert(0, ss);
			s.insert(1, "0");
		}
		out <<"Case #" <<i + 1 <<": " <<s <<endl;
	}

	return 0;
}