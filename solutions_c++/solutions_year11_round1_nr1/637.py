#include <fstream>

#define YES "Possible"
#define NO "Broken"
#define TEST "Case #"

using namespace std;

typedef unsigned long long long_int;

int main()
{
	ifstream input("A-large.in");
	ofstream output("A-large,out");
	long_int t, n, p_d, p_g, d, g;
	bool found;
	input >> t;
	for (long_int i = 0; i < t; i++)
	{
		found = false;
		input >> n >> p_d >> p_g;
		if ((p_g == 100 and p_d != 100) or (p_g == 0 and p_d != 0))
			output << TEST << i+1 << ": " << NO << endl;
		else
		{
			for (long_int j = 1; j <= n; j++)
				if (j * p_d % 100 == 0)
				{
					found = true;
					break;
				}
			if (!found)
				output << TEST << i+1 << ": " << NO << endl;
			else
				output << TEST << i+1 << ": " << YES << endl;
		}
	}
	input.close();
	output.close();
	return 0;
}
