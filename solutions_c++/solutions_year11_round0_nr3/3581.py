# include <iostream>
# include <fstream>

using namespace std;

int main(int argc, char **argv)
{
	ifstream in("input.in");
	ofstream out("output.out");
	int totalCase;
	in >> totalCase;
	for(int k = 1; k <= totalCase; k++)
	{
		int count;
		int w[2000];
		in >> count;
		int check = 0;
		int min = 2000000;
		int total = 0;
		for(int i = 0; i < count; i++)
		{
			in >> w[i];
			check^=w[i];
			if(min > w[i])
			{
				min = w[i];
			}
			total += w[i];
		}

		
		out << "Case #" << k << ": ";
		if(check == 0)
		{
			out << total - min;
		}
		else
		{
			out << "NO";
		}
		out << endl;
	}
	return 0;
}