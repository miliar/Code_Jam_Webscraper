#include "iostream"
#include "fstream"
#include "string"
#include "sstream"
#include "vector"
#include "math.h"

using namespace std;

bool check(int base, int n)
{
	int a = 0, b = 0;
	int nn = n;
	int j = 0;
	while (b != 1)
	{
		b = 0;
		do
		{
			a = 0;
			a += nn % base;
			a = a*a;
			b += a;
			nn = nn / base;
			if(nn / base == 0)
			{
				a = 0;
				a += nn % base;
				a = a*a;
				b += a;
			}
		}while(nn / base);
		nn = b;
		j++;
		if(j > 20)
			break;
	}
	if(b == 1)
		return true;
	return false;
}

string convert(int base, int n)
{
	string s;
	do
	{
		char *c = new char[10];
		int a = n%base;
		itoa(a, c, base);
		s.insert(0, c);
		n = n/base;
		if(n/base == 0)
		{
			a = n%base;
			itoa(a, c, base);
			s.insert(0, c);
		}
	}while(n/base);
	return s;
}

void main()
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");
	int T;
	infile >> T;
	infile.get();
	for(int i=0; i<T; i++)
	{
		int base[10];
		memset(base, 0, 10*sizeof(int));
		char *buf = new char[100];
		infile.getline(buf, 100);
		istringstream istr(buf);
		int j=0;
		int bmax = 0;
		int bmax2 = 0;
		int total = 0;
		while(!istr.eof())
		{
			istr >> base[j++];
			total++;
			if(base[j-1] > bmax)
			{
				bmax2 = bmax;
				bmax = base[j-1];
			}
		}
		bool b_base[10];
		for(j = 2; j<(int)pow((double)bmax, (double)bmax2); j++)
		{
			int count = 0;
			int k=0;
			while(base[k])
			{
				if(check(base[k], j))
				{
					k++;
					count++;
				}
				else
					break;
			}
			if(count == total)
				break;
		}
		outfile << "Case #" << i+1 << ": " << j << endl;
		cout << "Case #" << i+1 << ": " << j << endl;
	}
	infile.close();
	outfile.close();
}