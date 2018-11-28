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
	
	int T = readint();


	for (int test=0; test<T; test++)
	{
		uint64_t ans = 0;
		string in = readstring();
		
		int digit[64];
		memset(digit, -1, sizeof(digit));
		
		int base = 2;
		int nextDigit = 1;
		
		for (int i=0; i<in.size(); i++)
		{
			if (digit[i] == -1)
			{
				digit[i] = nextDigit;
				for (int j=i+1; j<in.size(); j++)
				{
					if (in[i] == in[j])
					{
						digit[j] = nextDigit;
					}
				}
				
				if (nextDigit == 1)
				{
					nextDigit = 0;
				}
				else if (nextDigit == 0)
				{
					nextDigit = 2;
				}
				else
				{
					nextDigit++;
					base++;
				}
			}
		}
		
		for (int i=0; i<in.size(); i++)
		{
			ans = ans * base;
			ans += digit[i];
		}		
		cout << endl << base << endl;
		cerr << "Case #" << test+1 << ": " << ans << endl;
	}
	
	
	cout << "time used " << float(clock()-start)/CLOCKS_PER_SEC << endl;
}

