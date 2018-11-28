#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int readint()
{
  int n;
  cin >> n;
  return n;
}

string readstring()
{
  string s;
  cin >> s;
  return s;
}

string readline()
{
	char buff[1000];
	cin.getline(buff,1000);
	
	if (cin.gcount() < 2)
	{
		cin.getline(buff,1000);
	}
	
	return string(buff);
}

int main(int argc, char* argv[])
{
	int start = clock();
	
	int L = readint();
	int D = readint();
	int N = readint();
	
	string words[5001];
	for (int i=0; i<D; i++)
	{
		words[i] = readstring();
	}
	
	string tests[501];
	
	for (int i=0; i<N; i++)
	{
		tests[i] = readstring();
	}
	
	for (int t=0; t<N; t++)
	{
		bool word_ok[5001];
		memset(word_ok, true, sizeof(word_ok));
		
		char* ptr = (char*)tests[t].c_str();
		
		for (int l=0; l<L; l++)
		{
			if (*ptr != '(')
			{
				for (int i=0; i<D; i++)
				{
					if (words[i][l] != *ptr)
					{
						word_ok[i] = false;
					}
				}
			}
			else
			{
				ptr++;
				bool poss[26];
				memset(poss, 0, sizeof(poss));
				
				while (*ptr != ')')
				{
					poss[(*ptr)-'a'] = true;
					ptr++;
				}
				
				for (int i=0; i<D; i++)
				{
					if (poss[words[i][l]-'a'] == false)
					{
						word_ok[i] = false;
					}
				}
			}
			ptr++;
		}
		
		int ans = 0;
		for (int i=0; i<D; i++)
		{
			if (word_ok[i])
			{
				ans++;
			}
		}
		cerr << "Case #" << t+1 << ": " << ans << endl;
	}
	
	cout << "time used " << float(clock()-start)/CLOCKS_PER_SEC << endl;
}

