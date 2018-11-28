#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <ctype.h>

#define MIN(x,y) ((x)<(y))?(x):(y)
#define MAX(x,y) ((x)>(y))?(x):(y)

#define rep(i,b) for(int i = 0; i < (b); i++)
#define fo(i,a,b) for(int i = (a); i < (b); i++)
#define fos(i,a,b) for(int i = (a); i < (int)(b).size(); i++)


#include <sstream>
#include <conio.h>

using namespace std;

int number[2000];

int S;

int calc(vector<int> q)
{
	if (q.size() == 0)
	{
		return 0;
	}

	memset(number, -1, sizeof(number));
	
	fo(i, 0, q.size())
	{
		fo(j, 0, S)
		{
			fo(k,0,q.size() - i)
			{
				int v = number[i] + 1;
				if (q[i + k] != j)
				{
					if (number[i + k + 1] == -1 || number[i + k + 1] > v)
					{
						number[i + k + 1] = v;
					}
				}
				else
				{
					v ++;

					if (number[i + k + 1] == -1 || number[i + k + 1] > v)
					{
						number[i + k + 1] = v;
					}
					break;
				}
			}
		}
	}	

	return number[q.size()];
}

int main( int argc, char* argv[] )
{
	FILE* in = fopen("A-Large.in", "r");

	int N = 0;
	fscanf(in, "%d\n", &N);
	

	FILE* out = fopen("A-Large.out", "w");

	fo(i, 0, N)
	{
		S = 0;
		fscanf(in, "%d\n", &S);
	
		vector<string> engines;
		char buff[1024];
		fo(i,0,S)
		{
			string s = fgets( buff, 1024, in);
			engines.push_back(s);
		}

		vector<int> q;
		int Number = 0;
		fscanf(in, "%d\n", &Number);
		fo(j, 0, Number)
		{
			string s = fgets( buff, 1024, in);
			fo(k, 0, S)
			{
				string s1 = engines[k];
				if (s == s1)
				{
					q.push_back(k);
					break;
				}
			}
		}
		fprintf(out, "Case #%d: %d\n", i + 1, calc(q));	
	}
	fclose (out);

	fclose (in);


	return 0;
}
