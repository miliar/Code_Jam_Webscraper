#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <cstring>
#include <string.h>
using namespace std;

/*
Case #2: there are twenty six factorial possibilities
Case #3: 
*/
char o [] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	cin.ignore();
	string str;
	for (int i = 1; i <= t; ++i)
	{
		getline(cin, str);
		cout << "Case #" << i << ": ";
		for (int i = 0; i < str.size(); ++i)
		{
			if (str[i] == ' ')
				cout << ' ';
			else
				cout << o[str[i]-'a'];
		}
		cout << endl;
	}
	
}	