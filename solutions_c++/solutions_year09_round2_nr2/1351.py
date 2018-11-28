#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;

bool okay (int a , int b)
{
	int c1[10] = {0} , c2[10] = {0};	
	int a1 = a , b1 = b;
	while (a1)
	{
		c1[a1 % 10] ++;	
		a1 /= 10;
	}
	
	while (b1)
	{
		c2[b1 % 10] ++;	
		b1 /= 10;
	}


	bool ok = 1;
	FORZ (i , 10)
		if (i && c1[i] != c2[i])	ok = 0;
		
	return ok;
}





int main ()
{
	int T = GI;
	FORZ (t , T)
	{
		int n = GI;		
		int ans = n + 1;
		
		while (true)
		{
			if (okay (ans , n))	break;
			ans ++;
		}
		
		printf ("Case #%d: %d\n" , t + 1 , ans);
		
	}
	return 0;
}



