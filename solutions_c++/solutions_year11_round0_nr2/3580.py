#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

using namespace std;

#define vs vector<string>
#define vi vector<int>
#define vii vector<vector<int>>
#define ll long long
#define pb push_back
#define si size()
#define FOR(i,j,k) for(int i = (j) ; i <= (k) ; i++ )
#define FORN(i,j,k) for(int i = (j) ; i >= (k) ;i--)
#define MAX 1000000

void fit(int cmap[26][26], int dmap[26][26])
{
		FOR(l,0,25)
			FOR(r,0,25)
				cmap[l][r] = dmap[l][r] = -1;
}

int main()
{
	ifstream fin("2.in");
	ofstream fout("out2.in");

	int t, i = 1;
	int c,d,n;
	char temp[5],str[1000];

	int cmap[26][26], dmap[26][26];

	fin >> t;

	while(i <= t)
	{
		fin >> c;

		fit(cmap,dmap);

		FOR(j,0,c - 1)
		{
			fin >> temp;
		
			int a = temp[0] - 'A';
			int b = temp[1] - 'A';
			int c = temp[2] - 'A';
			
		//	cout << a << " " << b  << " " << c << endl;
			cmap[a][b] = cmap[b][a] = c;
		}
		
		fin >> d;
		
		FOR(j,0,d - 1)
		{
			fin >> temp;
		
			int a = temp[0] - 'A';
			int b = temp[1] - 'A';
			
		//	cout << a << " " << b  << endl;
			dmap[a][b] = dmap[b][a] = 0;
		}

		fin >> n;

		fin >> str;
		
		/////////////////////////////////PROCESSING////////////////////////////////////////
		int last = 0;
		char ans[1000];
		int curr = 1;
		
		ans[0] = str[0];

		FOR(j,1,strlen(str) - 1)
		{
			int k = str[j] - 'A';
			int l;

			if(curr == last)
			{
				ans[curr] = str[j];
				curr++;
				continue;
			}	
			else
			{
				l = ans[curr - 1] - 'A';
			}

			if(cmap[k][l] != -1)
			{
				int temp = cmap[k][l];
				temp += 'A';

				ans[curr - 1] = temp;
			}
			else
			{
				bool val = 1;

				FORN(re,curr - 1,last)
				{
					int a = str[j] - 'A';
					int b = ans[re] - 'A';

					if(!dmap[a][b])
					{
						last = curr;
						val = 0;
						break;
					}
				}

				if(val)
				{
					ans[curr] = str[j];
					curr++;
				}

			}
		}	

		///////////////////////////////DONE///////////////////////////////
		
		curr--;

		fout << "Case #" << i << ": [";
		
		
		FOR(ty,last,curr)
		{
			if(ty == curr)
				fout << ans[ty];
			else
				fout << ans[ty]  << ", ";

		}
		
		fout << "]\n";		
			
		i++;
		
	}

	return 0;
}
