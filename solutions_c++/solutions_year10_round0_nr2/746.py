#include <iostream>
#include <fstream>

using namespace std;

int gcd(int, int);

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");

	int c;

	fin >> c;

	int i, n, j, cha1, cha2;

	int a[3];

	int shang, total;

	for( i = 1; i <= c; i++)
	{

		fin >> n;

		for( j = 0; j < n; j++)
			fin >> a[j];
		fout << "Case #" << i << ": ";
		if( n == 2)
		{
			if(a[0] > a[1])
				swap(a[0], a[1]);
			if( a[1] - a[0] == 1)
				fout << 0 << endl;
			else
			{
				shang = a[1] - a[0];
				total = shang;
				
				if( a[0] % shang == 0)
					fout << 0 << endl;
				else
				{
					while( a[0] > total )
						total += shang;
					fout << total - a[0] << endl;
				}
			}

		}
		else
		{

			if( a[0] > a[1] )
				swap(a[0], a[1]);
			if( a[1] > a[2] )
				swap(a[1], a[2]);
			if( a[0] > a[1] )
				swap(a[0], a[1]);

			cha1 = a[1] - a[0];
			cha2 = a[2] - a[1];
			


			shang = gcd(cha1, cha2);

			total = shang;

			if( a[0] % shang == 0)
				fout << 0 << endl;
			else
			{
				while( a[0] > total )
					total += shang;
				fout << total - a[0] << endl;
			}
		}
		
	}
	return 0;
}
int gcd( int m, int n)
{
	int temp;
	if( m == 0)
		return n;
	if( n == 0 )
		return m;
	if( m < n)
	{
		temp = m;
		m = n;
		n = temp;
	}
	while( n != 0)
	{
		temp = m % n;
		m = n;
		n = temp;
	}
	return m;
}