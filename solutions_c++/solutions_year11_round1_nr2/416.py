
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <bitset>		//UWAGA - w czasie kompilacji musi byc znany rozmiar wektora - nie mozna go zmienic
#include <cassert>
#include <iomanip>		//do setprecision
#include <ctime>
#include <complex>
using namespace std;
#define PB push_back
#define LL long long
#define ULL unsigned LL
#define LD long double

#define MR 110

string tab[MR];
bool guessed[26];

int main()
{
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		cout << "Case #" << c+1 << ": ";
		int n, m;
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			cin >> tab[i];		
		for(int i = 0; i < m; i++)
		{
			if(i)
				cout << " ";
			string s;
			cin >> s;
			string ans;
			int ile = -1;	//ile pomylek
			for(int i = 0; i < n; i++)
			{
				int res = 0;
				string pom;
				for(int j = 0; j < (int)tab[i].length(); j++)
					pom += ' ';
				for(int j = 0; j < 26; j++)
				{
					for(int k = 0; k < n; k++)
						if(tab[k].length() == pom.length() && tab[k].find(s[j]) != -1)
						{
							bool ok = 1;
							for(int l = 0; l < (int)pom.length(); l++)
								if(pom[l] != ' ' && pom[l] != tab[k][l])
								{
									ok = 0;
									break;
								}
								else if(pom[l] == ' ' && s.find(tab[k][l]) < j)
								{	//zawiera litere, ktora powinna byc odkryta, lub nie powinien jej zawierac							
									ok = 0;
									break;
								}
							if(ok)	//zgaduj
							{
								if(tab[i].find(s[j]) == -1)
									res++;
								else
									for(int k = 0; k < (int)pom.length(); k++)
										if(pom[k] == ' ' && tab[i][k] == s[j])
											pom[k] = s[j];
								break;
							}
						}
				}
				if(res > ile)
				{
					ile = res;
					ans = tab[i];
				}
			}
			cout << ans;
		}
		cout << "\n";
	}
	return 0;
}