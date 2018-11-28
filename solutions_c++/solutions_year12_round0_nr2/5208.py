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
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <stdlib.h>
#include <ctime>
#include <cstring>

using namespace std;

#define all(x) (x).begin(),(x).end()

map<int,int> M,M2;




int a[1000];
int n,p,s;

int f1(int x)
{
	int b = x/3;
	int m = x%3;
	if( m == 0 ) return b;
	return b+1;
}

int f2(int x)
{
	int b = x/3;
	int m = x%3;
	if( m == 0 )
	{
		if( b > 0 ) return b+1;
		return b;
	}
	if( m == 1 )
		return b+1;
	return b+2;
}

int solve(void)
{
	int answer = 0;
	
	int b[10];
	
	for(int i = 0; i < n; i++)
	{
		b[i] = 0;
		if( i < s ) b[i] = 1;
	}
	
	for(int k = 0; k < 100; k++)
	{
		next_permutation(&b[0],&b[n]);
		
		int res = 0;
		
		for(int i = 0; i < n; i++)
		{
			int w = f1(a[i]);
			if( b[i] )
			{ 
				w = f2(a[i]);
				//printf("1");
			} //else printf("0");
			
			if( w >= p ) 
				res++;
		}
		//printf("\n");
		if( res > answer ) answer = res;
					
	}
	
	return answer;
}



int main()
{	
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	
	cin >> t; 
	
	for(int i = 0; i < t; i++)
	{
		cin >> n >> s >> p;
		for(int j = 0; j < n; j++) cin >> a[j];
		printf("Case #%d: %d\n",i+1,solve());
	}
	
	fclose(stdout);
	return 0;
}
