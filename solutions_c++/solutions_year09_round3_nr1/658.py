#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#define MAX_LONG_LONG 9223372036854775807
#define MAX_INT  2147483647
#define MAX_LONG 2147483647
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
char number[100];
char tmp[100];
int flags[300];
int f[300];
int len;


int main() {
	freopen("..//input.txt", "rt", stdin);
	freopen("..//output.txt", "wt", stdout);
	int tc; 
	scanf("%d", &tc);

	for(int t = 1; t <= tc; t ++)
	{
		scanf("%s", number);
		len = strlen(number);
		memset(flags, 0, sizeof(flags));
		int base = 0;

		for(int i = 0;i < len; i ++)
		{
			flags[number[i]] = 1;
		}
		for(int i = 'a'; i <= 'z'; i ++)
		{
			base = base + flags[i];
		}
		for(int i = '0'; i <='9'; i ++)
		{
			base = base + flags[i];
		}
		memset(f, -1, sizeof(f));
		long long n = 0;
		if(base == 1) base = 2;
		n = pow(double (base), double (len - 1)) ;


		f[number[0]] = 1;
		if(len > 1)
		{
			for(int i = 1; i < len; i ++)
			{
				if(number[i] != number[0])
				{
					f[number[i]] = 0;
					break;
				}

			}
		}
		
		int j = 2;

		for(int i = 1; i < len; i ++)
		{
			if(f[number[i]] != -1)
				n = n + pow(double(base), double(len - i - 1))*f[number[i]];
			else
			{
				f[number[i]] = j;
				n = n + pow(double(base), double(len - i - 1))*j;
				j++;
			}
		}
		printf("Case #%d: %lld\n", t, n);
	}
}
