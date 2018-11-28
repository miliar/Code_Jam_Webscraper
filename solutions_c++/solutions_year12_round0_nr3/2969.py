
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <vector>

using namespace std;

ofstream outfile;
ifstream infile;

void setup()
{
	infile.open( "input.in");
	outfile.open( "output.txt");
}

void cleanup()
{
	infile.close();
	outfile.close();
}

void result( int i, int answer)
{
	cout << "Case #" << (i+1) << ": " << answer << endl;
	outfile << "Case #" << (i+1) << ": " << answer << endl;
}

struct Pair
{
	int a;
	int b;
	bool equals( Pair& other)
	{
		if( (other.a == a && other.b == b) || (other.a == b && other.b == a) )
		{
			return true;
		}
		return false;
	}
};

int digitCount( int a)
{
	int b = 0;
	while( a > 0)
	{
		a /= 10;
		b ++;
	}
	return b;
}

int rearange( int number, int amount)
{
	int digits = digitCount(number);
	int newnumber = number * (pow(10.0, amount));
	int highNumber = newnumber / (pow(10.0, digitCount(number)));
	newnumber += highNumber;
	return newnumber % (int)(pow(10.0, digitCount(number)));
}

int main()
{
	setup();

	int numberOfPuzzles;
	infile >> numberOfPuzzles;

	for( int i = 0; i < numberOfPuzzles; i ++)
	{
		int n;
		int m;

		infile >> n;
		infile >> m;

		vector<Pair> v;

		for( int j = n; j <= m; j ++)
		{
			// for the number of digits
			for( int k = 1; k < digitCount(m); k ++)
			{
				// rearrange
				int rearranged = rearange( j, k);
				Pair current;
				current.a = j;
				current.b = rearranged;
				// if not in vector, put in vector
				// if it doesn't have a leading zero and they aren't the same number
				if( digitCount(current.b) == digitCount(current.a) && current.a != current.b && current.b <= m && current.b >= n)
				{
					bool inVector = false;
					for( int vLook = 0; vLook < v.size(); vLook ++)
					{
						if( v[vLook].equals( current))
						{
							inVector = true;
							vLook = v.size();
						}
					}
					if( inVector == false)
					{
						v.push_back( current);
					}
				}

			}
		}
		result( i, v.size());
	}

	cleanup();
	system("pause");
}

