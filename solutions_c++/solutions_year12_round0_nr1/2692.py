#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>

#define all(v) v.begin(),v.end()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ld epsylon = 1e-9;
typedef unsigned int ui;
inline long double get_time(){   
	return (long double)clock()/CLOCKS_PER_SEC;
};
//ld start_time,end_time;

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	//start_time = get_time();
	//program
	int T;
	scanf("%d\n", &T);
	string g;
	for (int t = 0; t < T; ++t)
	{
		char s[500];
		cin.getline(s,500);
		g = s;
		for (int i = 0; i < g.size(); i++)
		{
			switch (g[i])
			{
			case 'e':
				{
					g[i] = 'o';
					break;
				}
			case 'y':
				{
					g[i] = 'a';
					break;
				}
			case 'q':
				{
					g[i] = 'z';
					break;
				}
			case 'j':
				{
					g[i] = 'u';
					break;
				}
			case 'p':
				{
					g[i] = 'r';
					break;
				}
			case 'm':
				{
					g[i] = 'l';
					break;
				}
			case 's':
				{
					g[i] = 'n';
					break;
				}
			case 'z':
				{
					g[i] = 'q';
					break;
				}
			case 'l':
				{
					g[i] = 'g';
					break;
				}
			case 'c':
				{
					g[i] = 'e';
					break;
				}
			case 'k':
				{
					g[i] = 'i';
					break;
				}
			case 'd':
				{
					g[i] = 's';
					break;
				}
			case 'x':
				{
					g[i] = 'm';
					break;
				}
			case 'v':
				{
					g[i] = 'p';
					break;
				}
			case 'n':
				{
					g[i] = 'b';
					break;
				}
			case 'r':
				{
					g[i] = 't';
					break;
				}
			case 'i':
				{
					g[i] = 'd';
					break;
				}
			case 'o':
				{
					g[i] = 'k';
					break;
				}
			case 'w':
				{
					g[i] = 'f';
					break;
				}
			case 't':
				{
					g[i] = 'w';
					break;
				}
			case 'b':
				{
					g[i] = 'h';
					break;
				}
			case 'a':
				{
					g[i] = 'y';
					break;
				}
			case 'h':
				{
					g[i] = 'x';
					break;
				}
			case 'f':
				{
					g[i] = 'c';
					break;
				}
			case 'u':
				{
					g[i] = 'j';
					break;
				}
			case 'g':
				{
					g[i] = 'v';
					break;
				}
			default:
				break;
			}
		}
		printf("Case #%d: %s\n", t+1, g.c_str());
	}
	//end program
	//end_time=get_time()-start_time;
	return 0;
}