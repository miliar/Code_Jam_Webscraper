#include <iomanip>
#include <algorithm>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

using namespace std;

map<char, char> m,m2;
char q[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r',
	      'z','t','n','w','j','p','f','m','a','q'};

int main()
{
	string s[100];
	int n;
	scanf("%d",&n);
	getline(cin,s[0]);
	for (int i = 0; i < n; i++)
	{
		cout << "Case #" << i+1 << ": ";
		getline(cin,s[i]);
		for (int j = 0; j < s[i].size(); j++)
		{
			if (s[i][j] == ' ') cout << ' ';
			else cout << q[s[i][j] - 'a'];
		}
		cout << endl;
	}

	return 0;	
}
