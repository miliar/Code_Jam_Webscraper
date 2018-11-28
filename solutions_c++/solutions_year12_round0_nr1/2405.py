#include <iostream>
#include <vector>
#include <cstring>
#include <string>
using namespace std;

int a[26];

void fill()
{
	a[0] = 24; a[24] = 0;
	a[9] = 20; a[20] = 9;
	a[16] = 25; a[25] = 16;
	int tmp[20] = {1, 7, 23, 12, 11, 6, 21, 15, 17, 19, 22, 5, 2, 4, 14, 10, 8, 3, 18, 13};
	for(int i = 0; i < 20; i++)
	{
		a[tmp[i]] = tmp[(i + 1) % 20];
	}
}

int main()
{
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	fill();
	int T;
	cin >> T;
	string c;
	getline(cin, c);
	for(int test = 1; test <= T; test++)
	{
		string s;
		getline(cin, s);
		string res;
		res.resize(s.size());
		for(int i = 0; i < (int)s.size(); i++)
		{
			if(s[i] != ' ')
			{
				res[i] = 'a' + a[s[i] - 'a'];
			}
			else 
				res[i] = ' ';
		}
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}