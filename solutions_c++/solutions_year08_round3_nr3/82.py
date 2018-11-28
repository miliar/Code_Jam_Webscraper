#include <iostream>
#include <vector>
using namespace std;
vector<__int64> v;
__int64 coun[1005], input[1005] ;
__int64 solve()
{
	__int64 sum = 0 ,i , j;;
	for(i = 0; i<v.size(); i ++) 
	{
		coun[i] = 1 ;
	}
	for(i = 0; i < v.size(); sum=( sum + coun[i] ) % 1000000007, i ++)
	{
		for(j=i+1; j<v.size(); j ++)
		{
			if( v[i] < v[j] ) 
			{
				coun[j] = ( coun[i] + coun[j] ) % 1000000007;
			}
		}
	}
	return sum;
}
void in (__int64 m)
{
	for(int i = 0; i < m; i ++ ) 
	{
		//cin >> input[i];
		scanf("%I64d", &input[i]);
	}
}
void init(__int64 n, __int64 m, __int64 X, __int64 Y, __int64 Z)
{
	int i;
	for(i=0 ; i<n; i++) 	
	{
		v.push_back(input[i % m]);
		input[i % m] = ( X * input[i%m] + Y * (i + 1) ) % Z;
	}
}
int main()
{
	__int64 i, n, m, X, Y, Z, ca = 1, test;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%I64d", &test);
	while(test --)
	{
		v.clear();
		scanf("%I64d %I64d %I64d %I64d %I64d", &n, &m, &X, &Y, &Z);
		in(m);
		init( n , m , X , Y, Z );
		printf("Case #%I64d: %I64d\n", ca++, solve());
	}
	return 0;
}