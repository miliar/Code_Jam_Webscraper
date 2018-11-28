#include <iostream>
#include <fstream>

using namespace std;

int gcd(int a, int b)
{
	int x = 1;
	for (int i = 1; i <= 100; i++)
	{
		if ( (a%i == 0) && (b%i == 0))
		{
			x = i;
		}
	}

	return x;
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt", ios::out | ios::trunc);

	int sizeOfTests = 0;
//read
	if (in == 0 || out == 0)
	{
		cout << "Epic fail!";
		return 0;
	}
	in >> sizeOfTests;





	for (int k = 0; k < sizeOfTests; k++)
	{
		int pd = 0, pg = 0,
			m1 = 0, n1 = 0, gcd1 = 0; //D<=G
		long long int n = 0;
		bool ispossible = true;
		in >> n;
		in >> pd;
		in >> pg;

		m1 = pd;
		n1 = 100;

		//find gcd
		gcd1 = gcd(m1, n1);
		m1/=gcd1;
		n1/=gcd1;

		if (n1<=n)
		{
			switch(pd)
			{
			case 0:
				{
					if (pg != 100)
					{
						ispossible = true; 
					}
					else
					{
						ispossible = false;
					}
					break;
				}
			case 100:
				{
					if (pg != 0)
					{
						ispossible = true; 
					}
					else
					{
						ispossible = false;
					}
					break;
				}
			default:
				{
					if (pg != 0 && pg != 100)
					{
						ispossible = true; 
					}
					else
					{
						ispossible = false;
					}
					break;
				}
			}
		}
		else
		{
			ispossible = false;
		}







		if (ispossible)
		{
			out << "Case #" << k+1 << ": Possible" << endl;
		}
		else
		{
			out << "Case #" << k+1 << ": Broken" << endl;
		}
	}


	return 0;
}