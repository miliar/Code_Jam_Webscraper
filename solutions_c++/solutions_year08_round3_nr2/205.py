#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int dig[40];

long long lim;

void filldig(string line)
{
	for( int i = 0; i != line.length(); i++ )
	{
		dig[i] = line[i] - '0';
	}
	int len = line.length() - 1;
	lim = static_cast<long long>( pow(3.0, len ) );
} 

int main(int argc, char* argv[])
{
	string fname;
	if ( argc != 2 )
	{
		cout<<"enter input file name: ";
		cin>>fname;
	}
	else
		fname = argv[1];
	
	ifstream infile(fname.c_str());
	ofstream outfile("output.txt");

	int N;
	infile>>N;
	
	for( int i = 0; i != N; i++ )
	{
		string line;
		
		infile>>line;
		
		filldig(line);
		
		long long res;
		long long res1;
		long long res2;
		
		res = 0;

		int op;
		
		int x;

		long long test;
		int m;

		for ( long long j = 0; j != lim; j++ )
		{
			test = j;
			
			m = 1;
			op = 1;
			res1 = 0;
			res2 = dig[0];
			
			int count = line.length() - 1;
			while( true )
			{	
				if ( count == 0 )
				{
					res1 += res2 * op;
					res2 = 0;
					break;
				}
				
				x = test%3;
				switch(x)
				{
				case 0:
					res2 = res2 * 10 + dig[m];
					m++;
					test = test / 3;
					break;
				case 1:
					res1 += res2 * op;
					res2 = dig[m];
					op = 1;
					m++;
					test = test / 3;
					break;
				case 2:
					res1 += res2 * op;
					res2 = dig[m];
					op = -1;
					m++;
					test = test /3;
					break;
				}
				count--;
			}

			if ( res1 < 0 )
				res1 *= -1;
			if ( res1 <= 0 || res1 % 2 == 0 || res1 % 3 == 0 || res1 % 5 == 0 || res1 % 7 == 0 )
			{
				res++;
			}
		}	
		
		
		outfile<<"Case #"<<i+1<<": "<<res<<endl;
	}

}
	
