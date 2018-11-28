// a.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <fstream>
#include <string>

#define dmax 5005

using namespace std;

int L, D, N;
string s[dmax];
char v[dmax];
char good[30];
string crtString;


int main()
{
	ifstream inFile;
	inFile.open("a.in");
	inFile >> L >> D >> N;
	for(int i = 0; i < D; i++)
		inFile >> s[i];

	freopen("a.out", "w", stdout);

	for(int i = 0; i < N; i++)
	{
		inFile >> crtString;
		int result = 0;
		memset(v, 0, sizeof(v));
		int para = 0, crtLet = 0;
		for(int j = 0; j < (int)crtString.size(); j++)
			if(para) {
				if(crtString[j] == ')')
				{
					para = 0;
					for(int l = 0; l < D; l++)
						if(!good[s[l][crtLet] - 'a'])
							v[l] = 1;
					crtLet++;
				}
				else good[crtString[j] - 'a'] = 1;
			}
			else {
				if(crtString[j] == '(') {
					para = 1;
					memset(good, 0, sizeof(good));
				}
				else {
					for(int l = 0; l < D; l++)
						if(crtString[j] != s[l][crtLet])
							v[l] = 1;
					crtLet++;
				}
			}
		for(int j = 0; j < D; j++)
			if(v[j] == 0) result++;

		cout << "Case #" << (i + 1) << ": " << result << endl;
	}

	return 0;
}

