#include <iostream>
#include <string>
#include <cstring>

//#define DEBUG
#define L 500
#define BASE 10000

using namespace std;

string t = "welcome to code jam";
long din[L+1][19];
char arg[L+2];
long len;
long m;
void init()
{
	memset(din, 0, sizeof(din));
	gets(arg);
#ifdef DEBUG
	cout << arg << "!\n";
#endif
	len = strlen(arg);
	m = t.size();
#ifdef DEBUG
	cout << "m==" << m << "  len==" << len << "\n";
#endif
}
void solve()
{
	long y, j, z;
	for(y = 0; y < len; y++)
	{
		if (arg[y] == t[0]) {din[y][0] = 1;}
		for(j = 0; j < m-1; j++)
		{
			if  (!din[y][j]) {continue;}
			for(z = y+1; z < len; z++)
			{
				if (arg[z] == t[j+1])
				{
					din[z][j+1] += din[y][j];
					din[z][j+1] %= BASE;
				}
			}
		}
	}
}
void print_ans()
{
	long ans = 0;
	long y;
	for(y = 0; y < len; y++) 
	{
		ans += din[y][m-1];
		ans %= BASE;
	}
	if (ans < 10) {cout << "000" << ans << "\n";}
	else if (ans < 100) {cout << "00" << ans << "\n";}
	else if (ans < 1000) {cout << "0" << ans << "\n";}
	else {cout << ans << "\n";}
	
}
void print_din()
{
	long y, j;
	for(y = 0; y < len; y++)
	{
		for(j = 0; j < m; j++)
		{
			cout << din[y][j] << " ";
		}
		cout << "\n";
	}
}
void logic()
{
	init();
	solve();
	print_ans();
#ifdef DEBUG
	print_din();
#endif
}
int main()
{
	long tt, y;
	cin >> tt;
	gets(arg);
	for(y = 1; y <= tt; y++)
	{
		cout << "Case #" << y << ": ";
		logic();
	}
}