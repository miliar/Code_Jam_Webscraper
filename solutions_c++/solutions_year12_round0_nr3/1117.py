#include <fstream>
using namespace std;
int nd, e;
void recycle(int &n)
{
	int temp = n % 10 * e;
	n = (n  + temp) / 10;
}
int main()
{
	int t, i, a, b, j, temp, c, result;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for(i = 1; i <= t; i++)
	{
		fin >> a >> b;
		result = 0;
		temp = a;
		nd = 0;
		e = 1;
		while(temp != 0)
		{
			temp /= 10;
			e *= 10;
			nd++;
		}
		for(j = a; j <= b; j++)
		{
			temp = j;
			c = 0;
			do
			{
				recycle(temp);
				if(temp < j && temp >= a)
					goto next;
				if(temp >= a && temp <= b)
					c++;
			}
			while(temp != j);
			result += c * (c - 1) / 2;
			next:;
		}
		fout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}