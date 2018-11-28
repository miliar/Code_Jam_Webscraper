#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std ;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);
	int T;
	int kase;
	int p[255];
	long long ans;
	string in;
	cin >> T;
	int n, i;
	int base;
	for(kase = 1; kase <= T; kase ++)
	{
		cin >> in;
		memset(p, -1, sizeof(p));
		int sz = in.length();
		base = 0;
		for(i = 0; i < sz; i ++)
		{
			if(p[in[i]] == -1)
			{
				if(base == 0)
				{
					p[in[i]] = 1;
					base ++;	
				}
				else if(base == 1)
				{
					p[in[i]] = 0;
					base ++;	
				}	
				else
				{
					p[in[i]] = base;
					base ++;	
				}
			}	
		}
		long long b = 1;
		ans = 0;
		if(base == 1)	base = 2;
		for(i = sz - 1; i >=0; i --)
		{
			ans += b * p[in[i]];
			b *= base;
		}
		cout << "Case #" << kase << ": " << ans << endl;
		
	}
    return 0;
}


/*
Input 
   
 
   
10
11001001
cats
abcdefghijklmnopqrstuvwxyz
zig
cats


Output
Case #1: 201
Case #2: 75
Case #3: 11
 

*/
