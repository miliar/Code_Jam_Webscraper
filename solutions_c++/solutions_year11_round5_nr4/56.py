#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

string s;
string cur;
long long x;
int n;

void Load()
{
	cin >> s;
	cur = s;
	n = s.length();

}

bool Do(int i) 
{
	if (i == n) {
		long long t = sqrt(x+0.0)-1;
		while (t*t < x) t++;
		if (t*t == x) {
			cout << cur << "\n";
			return true;
		}
		return false;
	}
	x <<= 1;
	if (s[i] != '1') {
		cur[i] = '0';
    	if(Do(i+1)) return true;	
	}
	if (s[i] != '0') {
		x++;
		cur[i] = '1';
    	if(Do(i+1)) return true;
   	}
	x >>= 1;
	return false;
}


void Solve()
{
    x = 0;
	Do(0);
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
