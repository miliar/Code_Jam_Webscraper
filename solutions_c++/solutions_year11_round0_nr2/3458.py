#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <sstream>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define INF 2000000000
#define EPS 1e-11
#define MAX_N 100002
using namespace std;

#ifdef _WIN32 
typedef __int64 int64; 
#else 
typedef long long int64; 
#endif 

int conv(char x)
{
	if(x == 'Q')return 1;
	else if(x == 'W') return 2;
	else if(x == 'E') return 3;
	else if(x == 'R') return 4;
	else if(x == 'A') return 5;
	else if(x == 'S') return 6;
	else if(x == 'D') return 7;
	else if(x == 'F') return 8;
	else return 0;
}


int
main()
{
	char invoke[10][10];
	int opposed[10][10];
	vector<char> magic;
	int T,C,D,N,psize;
	string temp1;
	int pos1,pos2,cek;
	cin >> T;
	for(int a = 1; a <= T;a++)
	{
		magic.clear();
		temp1.clear();
		for(int i = 0;i < 10;i++)
		{
			for(int  j = 0;j < 10;j++)
			{
				invoke[i][j] = '#';
				opposed[i][j] = 0;
			}
		}
		cin >> C;
		for(int k = 0;k < C;k++)
		{
			temp1.clear();
			cin >> temp1;
			pos1 = conv(temp1[0]);
			pos2 = conv(temp1[1]);
			invoke[pos1][pos2] = temp1[2];
			invoke[pos2][pos1] = temp1[2];
		}
		cin >> D;
		for(int l = 0;l < D;l++)
		{
			temp1.clear();
			cin >> temp1;
			pos1 = conv(temp1[0]);
			pos2 = conv(temp1[1]);
			opposed[pos1][pos2] = 1;
			opposed[pos2][pos1] = 1;
		}
		cin >> N;
		temp1.clear();
		cin >> temp1;
		for(int  m = 0;m < N;m++)
		{
			 pos1 = conv(temp1[m]);
			 if(magic.size() != 0)
			 {
  				 pos2 = conv(magic.back());
				 if(invoke[pos1][pos2] != '#')
				 {
					magic.pop_back();
					magic.push_back(invoke[pos1][pos2]);
				 }
				 else
				 {
					cek  = 0;
					psize = magic.size();
					for (int  o =0;o < psize;o++)
					{
						pos2 = conv(magic[o]);
						if(opposed[pos1][pos2])
						{
							cek = 1;
						}
					}
					if(cek)magic.clear();
					else magic.push_back(temp1[m]);
				 }
			 }
			 else
			 {
				 magic.push_back(temp1[m]);
			 }
		}
		cout << "Case #" << a << ": [";
		psize = magic.size();
		if(psize == 0)cout << "]" << endl;
		else
		{
			for (int i = 0;i < psize-1;i++)
			{
				cout << magic[i] << ", ";
			}
			cout << magic[psize-1] << "]" << endl;
		}
	}
return 0;
}
