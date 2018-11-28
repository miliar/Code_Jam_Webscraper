#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int t, tt;
int base;
int hash[500];
int used[100];
string a;
ifstream ifs;
ofstream ofs;

void work()
{
	int i, j, tmp;
	ifs >> a;
	for (i = 0; i < 500; ++i)
		hash[i] = -1;
	for (i = 0; i < 80; ++i)
		used[i] = false;
	
	
	hash[a[0]] = 1;
	used[1] = true;
	for (i = 1; i < a.length(); ++i)
	{		
		if (hash[a[i]] == -1)
		{
			for (j = 0; j < 80; ++j)
				if (!used[j])
				{
					hash[a[i]] = j;
					used[j] = true;
					break;
				}				
		}
	}
	
	for (i = 0; i < 80; ++i)
		if (used[i]) base = i;
	base++;
	
	long long bs;
	long long ans;
	bs = 1;
	ans = 0;
	for (i = a.length() - 1; i >= 0; --i)
	{
		ans += hash[a[i]] * bs;
		bs = bs * base;
	}
	ofs << "Case #" << (tt + 1) << ": " << ans << endl;
}

int main()
{
	ifs.open("r11.in");
	ofs.open("r11.out");
	ifs >> t;
	for (tt = 0; tt < t; ++tt)
	{
		work();
	}
	ifs.close();
	ofs.close();
}