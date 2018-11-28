# include <iostream>
# include <fstream>
# define MAX 200

using namespace std;

int main(int argv, char **argc)
{
	ifstream in("input.in");
	ofstream out("output.out");
	int totalCase;
	in >> totalCase;
	
	for(int caseNumber = 1; caseNumber <= totalCase; caseNumber++)
	{
		int count, min, max;
		int w[MAX];
		in >> count >> min >> max;
		for(int i = 0 ; i < count; i++)
		{
			in >> w[i];
		}

		int m;
		out << "Case #" << caseNumber << ": ";
		int flag = 0;
		int temp= 0;
		for(int i = min; i <= max; i++)
		{
			temp = 0;
			for(int j = 0; j < count; j++)
			{
				if( i % w[j] != 0 && w[j] % i != 0)
				{
					temp = 1;
					break;
				}
			}

			if(temp == 0)
			{
				flag = 1;
				out << i;
				break;
			}
		}

		if(flag == 0)
		{
			out <<"NO";
		}

		out << endl;
	}

	in.close();
	out.close();
	return 0;
}