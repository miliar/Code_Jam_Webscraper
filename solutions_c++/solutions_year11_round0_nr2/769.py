#include <stdio.h> 
#include <vector> 
#include <list>
#include <string>
#include <set>
#include <algorithm> 
#include <fstream> 
#include <iostream> 
using namespace std;
char z[200];

int main() 
{ 
	int T;
	cin >> T;
	
	for (int test = 1; test <= T; ++test)
	{
		char matrix[256][256]={0};
		set<int> cbad[256];
		int C,D,N;
		cin >> C;
		for (int i = 0; i < C; ++i)
		{
			string s;
			cin >> s;
			matrix[s[0]][s[1]] = matrix[s[1]][s[0]] = s[2];
		}
		cin >> D;
		for (int i = 0; i < D; ++i)
		{
			string s;
			cin >> s;
			cbad[s[0]].insert(s[1]);
			cbad[s[1]].insert(s[0]);
		}
		cin >> N;
		int cpos = -1;
		for (int i = 0; i < N; ++i)
		{
			char c;
			cin >> c;
			if (cpos >= 0 && matrix[z[cpos]][c])
			{
				z[cpos] = (matrix[z[cpos]][c]);
			}
			else
			{
				bool clr = 0;
				for (int i = 0; i <= cpos; ++i)
				{
					if (cbad[z[i]].find(c) != cbad[z[i]].end())
					{
						cpos = -1;
						clr = 1;
						break;
					}
				}
				if (!clr)
					z[++cpos] = c;
			}
		}
		cout << "Case #" << test << ": [";
		for (int i = 0; i <= cpos-1; ++i)
		{
			cout << z[i] << ", ";
		}
		if (cpos != -1)
		{
			cout << z[cpos];
		}
		cout << "]\n";		
	}
#ifndef ONLINE_JUDGE
#ifndef FULLREDIRECT
	ifstream console("CONIN$");
	char fdasfadsfdasfdsa;
	console.getline(&fdasfadsfdasfdsa,1);
	console.close();
#endif
#endif
	return 0; 
}