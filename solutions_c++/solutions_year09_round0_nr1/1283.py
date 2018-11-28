//Judged response for input A-small: Correct!View it. 
#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int L, D, N, c, r;
string str[5001];
map<char, bool> p[16];
string s;

int main()
{
	ifstream cin("A-large.in.txt");
	ofstream cout("b.txt");
	cin >> L >> D >> N;
	for (int i = 0; i < D; i++)
	{
		cin >> s;
		str[i] = s;
	}
	for (int pp = 1; pp <= N; pp++)
	{
		for (int i = 0; i < L; i++) p[i].clear();
		cin >> s;
		c = 0;
		for (int i = 0; i < s.length(); )
			if (s[i] == '(')
			{
				for (int j = i + 1; j < s.length(); j++)
					if (s[j] == ')') 
					{
						c++;
						i = j + 1;
						break;
					}
					else p[c][s[j]] = true;
			}
			else
			{
				p[c][s[i]] = true;
				c++;
				i++;
			}
		r = 0;
		for (int i = 0; i < D; i++)
		{
			bool flag = false;
			for (int j = 0; j < L; j++)
				if (p[j].find(str[i][j]) == p[j].end()) 
				{
					flag = true;				
					break;
				}
			if (!flag) r++;
		}
		cout << "Case #" << pp << ": " << r << '\n';
	}
	return 0;
}
