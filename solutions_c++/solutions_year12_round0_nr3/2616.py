#include <iostream.h>
#include <fstream.h>

// Code Jam 2012
// Qualification Round
// Problem C. Recycled Numbers

int power(int num, int power)
{
	int result;
	
	result = 1;
	
	while ( power > 0 )
	{
		result = result*num;
		power--;
	}
	return result;
}

int numdigits(int num)
{
	int digits = 0;
	
	while ( num > 0 )
	{
		num = num/10;
		digits++;
	}
	return digits;
}

int rotate(int num,int places)
{
	int digits;
	int result;
	int carry;
	
	digits = numdigits(num);
	
	result = num;
	
	while ( places > 0 )
	{
		carry = result % 10;
	
		result = result/10;
		result = result + power(10,digits)*carry/10;

		places--;
	}
	return result;
}

int main(int argc, char *argv[])
{
	int A,B;
	int n,m;
	int T;
	int t;
	int d;
	int i;
	int j;
	int found;
	int answer;
	
	int mlist[8];

	ifstream inFile;
	
	if ( argc < 2 )
	{
		cout << "Running test.in" << endl;
		inFile.open("test.in");
	}
	else
	{
		inFile.open(argv[1]);
	}
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	
	for (t=0;t<T;t++)
	{
		answer = 0;
		
		inFile >> A;
		inFile >> B;
		
		for (n=A;n<B;n++)
		{
			for (i=0;i<8;i++)
			{
				mlist[i] = 0;
			}
		
			d = numdigits(n);
			for (i=1;i<d;i++)
			{
				m = rotate(n,i);
				if ( (m>n) && (m<=B) )
				{
					// check for duplicates - ie if we have already counted this particular value of m
					j = 0;
					found = 0;
					while (mlist[j] != 0)
					{
						if ( mlist[j] == m )
						{
							found = 1;
						}
						j++;
					}
					mlist[j] = m;
					
					if ( found == 0 )
					{
						answer++;
					}

				}
			}
		}
		
		cout << "Case #" << t+1 << ": "<< answer << endl;
	}
		
		
	
	inFile.close();
	return 0;
}