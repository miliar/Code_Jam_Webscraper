#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;
char mat[256][256];
bool opposed[256][256];
int contained[256];
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int c, d, n;
		cin >> c;
		string str;
		memset(mat, 0, sizeof(mat));
		memset(opposed, false, sizeof(opposed));
		for(int i = 0; i < c; i++)
		{
			cin >> str;
			mat[str[0]][str[1]] = str[2];
			mat[str[1]][str[0]] = str[2];
		}
		cin >> d;
		for(int i = 0; i < d; i++)
		{
			cin >> str;
			opposed[str[0]][str[1]] = true;
			opposed[str[1]][str[0]] = true;
		}
		cin >> n;
		cin >> str;
		string res;
		memset(contained, 0, sizeof(contained));
		for(int i = 0; i < str.size(); i++)
		{
			if(res.size() != 0 && mat[str[i]][res[res.size() - 1]] != 0)
			{
				contained[res[res.size() - 1]]--;
				contained[mat[str[i]][res[res.size() - 1]]]++;

				res[res.size() - 1] = mat[str[i]][res[res.size() - 1]];
			}
			else
			{
				bool cleared = false;
				for(char ch = 'A'; ch <= 'Z'; ch++)
				{
					if(opposed[str[i]][ch] && contained[ch])
					{
						res.clear();
						memset(contained, 0, sizeof(contained));
						cleared = true;
						break;
					}
				}
				if(!cleared)
				{
					res.push_back(str[i]);
					contained[str[i]]++;
				}
			}
		}

		cout << "[";
		bool first = true;
		for(int i = 0; i < res.size(); i++)
		{
			if(!first)
				cout << ", ";
			first = false;
			cout << res[i];
		}
		cout << "]" << endl;
	}
	return 0;
}
