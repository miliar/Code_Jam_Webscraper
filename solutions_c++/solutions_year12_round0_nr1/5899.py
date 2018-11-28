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
	int T;
	string G;

	vector < pair<char,char> > alpha;
	alpha.push_back(make_pair('a', 'y'));
	alpha.push_back(make_pair('b', 'h'));
	alpha.push_back(make_pair('c', 'e'));
	alpha.push_back(make_pair('d', 's'));
	alpha.push_back(make_pair('e', 'o'));
	alpha.push_back(make_pair('f', 'c'));
	alpha.push_back(make_pair('g', 'v'));
	alpha.push_back(make_pair('h', 'x'));
	alpha.push_back(make_pair('i', 'd'));
	alpha.push_back(make_pair('j', 'u'));
	alpha.push_back(make_pair('k', 'i'));
	alpha.push_back(make_pair('l', 'g'));
	alpha.push_back(make_pair('m', 'l'));
	alpha.push_back(make_pair('n', 'b'));
	alpha.push_back(make_pair('o', 'k'));
	alpha.push_back(make_pair('p', 'r'));
	alpha.push_back(make_pair('q', 'z'));
	alpha.push_back(make_pair('r', 't'));
	alpha.push_back(make_pair('s', 'n'));
	alpha.push_back(make_pair('t', 'w'));
	alpha.push_back(make_pair('u', 'j'));
	alpha.push_back(make_pair('v', 'p'));
	alpha.push_back(make_pair('w', 'f'));
	alpha.push_back(make_pair('x', 'm'));
	alpha.push_back(make_pair('y', 'a'));
	alpha.push_back(make_pair('z', 'q'));
	

	ifstream cin("A-small-attempt1.in");
	ofstream cout("A-small-attempt1.out");

	cin >> T;

	getline(cin, G);

	for (int i=0; i<T; i++)
	{
		getline(cin, G);
		
		cout << "Case #" << i+1 << ": ";

		for (int j=0; j<G.length(); j++)
		{
			for (int k=0; k<alpha.size(); k++)
			{
				if (G[j] == ' ')
				{
					cout << G[j];
					break;
				}
				else if (G[j] == alpha[k].first)
				{
					cout << alpha[k].second;
					break;
				}
			}
		}
		cout << endl;
	}

	system("Pause");
	return 0;
}