#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void)
{
	int n, a, b, count, inc, trans, last;
	bool first, inner;
	ofstream file;
	ifstream in;
	file.open("file.txt"); //open a file
	in.open("input.txt");

	in >> n;

	for (int i = 0; i < n; i++)
	{
		in >> a >> b;
		count = 0;
		inc = 1;
		first = false;
		last = 0;
		if (b > 9)
		{
			for (int t = a; t < b; t++)
			{
				inner = false;

				if (t < 100)
				{
					trans = (t % 10) * 10 + t / 10;
					if (trans > t && trans <= b)
					{
						count++;
						inner = true;
					}
				}
				else if (t < 1000)
				{
					trans = (t % 10) * 100 + t / 10;
					if (trans > t && trans <= b)
					{
						count++;
						inner = true;
					}

					trans = (t % 100) * 10 + t / 100;
					if (trans > t && trans <= b)
					{
						count++;
						inner = true;
					}
				}
				else if (t < 10000)
				{
					trans = (t % 10) * 1000 + t / 10;
					if (trans > t && trans <= b)
					{
						count++;
						inner = true;
					}

					trans = (t % 100) * 100 + t / 100;
					if (trans > t && trans <= b)
					{
						count++;
						inner = true;
					}

					trans = (t % 1000) * 10 + t / 1000;
					if (trans > t && trans <= b)
					{
						count++;
						inner = true;
					}
				}
/*
				if (inner)
				{
					first = true;
					last = t;
				}
				else if (first)
				{
					if (last == t - 1)
					{
						t += inc;
						inc = 1;
					}
					else
					{
						inc++;
					}
				}*/
			}
		}
		file << "Case #" << i + 1 << ": " << count << endl;
	}
	file.close(); 
    return 0;
}