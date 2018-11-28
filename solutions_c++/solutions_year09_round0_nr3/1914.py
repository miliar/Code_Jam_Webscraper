#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

int n;
string s;
string p;
int a[50];

int main()
{
	p = ("$welcome to code jam");
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf("%d\n",&n);
	
	for(int i=0; i < n; i++)
	{
		getline( cin, s );
		
		memset( a,0, sizeof(a) );
		a[0] = 1;
		for(int j = 0; j < (int)s.length(); j++)
		{
			for(int l = 1; l < (int)p.length(); l++)
				if( p[l]==s[j] )
				{
					a[l] += a[l-1];
					a[l] %= 10000;
				}
		}
		
		printf("Case #%d: %04d\n",i+1,a[(int)p.length()-1]);
		
	}
	
	return 0;
}