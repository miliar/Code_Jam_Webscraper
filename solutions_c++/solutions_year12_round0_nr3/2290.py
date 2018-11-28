#include <iostream>
#include <fstream>
#include <stdint.h>
#include <vector>

using namespace std;

#define BASE 10


void 
	read (ifstream &in, int &begin, int &end, int &order_count, int &order_num)
{
	in >> begin;
	in >> end;

	int rest = begin;
	order_count = 0;
	order_num = 1;

	while (rest != 0)
	{		
		rest /= BASE;
		
		if (rest != 0)
		{
			order_count += 1;
			order_num *= BASE;
		}
	}
}


int 
	digit_max (int x, int order)
{
	int max = x;

	for (int i = 0; i < order; ++i)
	{
		int rem = x % BASE;
		x = (x / BASE) + rem * order;

		if (x > max)
			max = x;
	}

	return max;
}


void
	solve (ofstream &out, int case_i, int begin, int end, int order_count, int order_num)
{			
	vector <int> found;
	found.resize (end+1, false);
			
	int recycled = 0;
	for (int n = begin; n < end; ++n)
	{
		int m = n;	
		int count = 1;
		found [n] = true;
		for (int i = 0; i < order_count; ++i)
		{	
			int rem = m % BASE;
			m = (m / BASE) + rem * order_num;		

			if (m > n && m <= end)
			{
				if (found [m] == false)
				{
					found [m] = true;
					count++;
				}	
			}	
		}
		recycled += (count * (count - 1)) / 2;
	}	
	
	cout << "Case #" << case_i << ": " << recycled << endl;
	out << "Case #" << case_i << ": " << recycled  << endl;
	
}


void
	run ()
{
	ifstream in = ifstream ("in.txt");
	ofstream out = ofstream ("out.txt");

	int case_count;
	in >> case_count;
	
	for (int i = 1; i <= case_count; ++i)
	{
		int begin;
		int end;
		int order_count;
		int order_num;

		read (in, begin, end, order_count, order_num);

		solve (out, i, begin, end, order_count, order_num);
	}

	in.close ();
	out.close ();
}


int 
	main ()
{	
	run ();

	system ("pause");
}
