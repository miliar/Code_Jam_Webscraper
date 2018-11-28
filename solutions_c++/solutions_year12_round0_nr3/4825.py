#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

int main()
{
	ifstream cin("C-small-attempt1.in");
	ofstream cout("C-small-attempt1.out");

	int T, A, B;
	set <string> scores;

	cin >> T;
	for (int i=1; i<=T; i++)
	{
		cin >> A >> B;
		int output = 0;

		cout << "Case #" << i << ": ";
		if (B<10)
			output = 0;
		else
		{
			string a;
			stringstream ss;
			ss << A;
			ss >> a;
			ss.clear();

			for (int n=A; n<B; n++)
			{
				int sub = a.length()-1;
				int m = 0;

				for (int j=1; j<=sub; j++)
				{
					string nString;
					//stringstream ss;
					ss << n;
					ss >> nString;
					ss.clear();

					string subString1 = nString.substr(0, j);
					string subString2 = nString.substr(j);
					string subString = subString2 + subString1;
					ss << subString;
					ss >> m;
					ss.clear();
					
					if (m>n && m<=B && nString.length() == subString.length())
					{
						nString.append(subString);
						scores.insert(nString);
					}
				}
			}
		output = scores.size();
		scores.clear();
		}
		cout << output << endl;
	}

	system("Pause");
	return 0;
}