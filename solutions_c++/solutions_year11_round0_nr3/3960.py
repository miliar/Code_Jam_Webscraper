#include <cstdio>
#include <iostream>
using namespace std;

int numeros[1005];

int SumaBinaria(int a,int b)
{
	int r = 0;
	int i;
	for ( i = 0 ; i < 31 ; i++ )
		if ( (1 << i & a) ^ (1 << i & b) )
			r += 1 << i;
	return r;
}

int main()
{
	int t;
	int i,j,k;
	cin >> t;
	
	for ( i = 1 ; i <= t ; i++ )
	{
		int n;
		cin >> n;
		for ( j = 0 ; j < n ; j++ )
			cin >> numeros[j];
		
		int c = 1;
		int max_n = -1;
		while ( c < (1<<n) - 1)
		{
			int a = 0;
			int b = 0;
			
			int ab = 0;
			int bb = 0;
			
			int p;
			
			for ( p = 0 ; p < n ; p++ )
			{
				if ( 1 << p & c )
				{
					a += numeros[p];
					ab = SumaBinaria(ab,numeros[p]);
				}
				else
				{
					b += numeros[p];
					bb = SumaBinaria(bb,numeros[p]);
				}					
			}
			
			//cout << ab << " " << bb << endl;
			
			if ( bb == ab )
			{
				if ( a > max_n )
					max_n = a;
				else if ( b > max_n )
					max_n = b;
				//cout << max_n << endl;
			}
			c++;
		}
		if ( max_n != -1 )
			printf("Case #%d: %d\n",i,max_n);
		else
			printf("Case #%d: NO\n",i,max_n);
	}
	return 0;
}
