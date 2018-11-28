#include <cstdio>
#include <iostream>
using namespace std;

#define MAX 10000

bool criba[MAX+5];

int cribado()
{
	int i,j;	
	for ( i = 0 ; i <= MAX ; i++ )
		criba[i] = false;
	
	for ( i = 2 ; i <= MAX ; i++ )
	{
		if ( criba[i] == false )
		{
			for ( j = i*i ; j <= MAX ; j+=i )
				criba[j] = true;
		}
	}	
}

void orch(int t)
{
	int n,l,h;
	int i,j;
	int frec[105];
	bool f;
	
		
	cin >> n >> l >> h;
	//cout << n << l << h << endl;
	for ( i = 0 ; i < n ; i++ )
		cin >> frec[i];
	
	
	cout << "Case #"<< t << ": ";
	
	if ( l == 1 )
	{
		cout << "1" <<endl;
		return;
	}
	
	int p[MAX+1];
	
	for ( i = 0 ; i < n ; i++ )
		p[i] = 0;
	
	for ( i = 0 ; i < n ; i++ )
	{
		if ( frec[i] < 2 ) continue;
		
		for ( j = 2 ; j < frec[i] ; j++ )
			if ( frec[i] % j == 0 )
				p[j] = 1;
				
		for ( j = frec[i] ; j <= h ; j+= frec[i] )
		{
			p[j] = 1;
		}
	}
	
	for ( i = l ; i<= h ; i++ )
	{
		int cont = 0;
		for ( j = 0 ; j < n ; j++ )
		{	
			if ( p[i] == 1 )
			{
				if ( frec[j] % i == 0 ||  i % frec[j] == 0 )
					cont++;
			}
		}
		if ( cont == n )
		{
			cout << i << endl;
			return;
		}
	}
	
	cout << "NO" <<endl;
	
	return;
}


int main()
{
	int t;
	cin >> t;
	int i;
	for ( i = 1 ; i <= t ; i++ )
	{
		orch(i);
	}
	return 0;
}