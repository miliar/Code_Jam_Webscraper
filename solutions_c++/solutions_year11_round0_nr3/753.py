#include <fstream>
using namespace std;

ifstream input("input.txt");
ofstream output("output.txt");

int main()
{
	int t,n;
	input >> t;
	for (int i=0;i<t;++i)
	{
		input >> n;
		int s=0, min = 999888777, xor = 0, v;
		for (int j=0; j<n; ++j)
		{
			input >> v;
			s += v;
			if (min>v) min=v;
			xor^=v;
		}
		output << "Case #" << i+1 << ": ";
		if (xor) output << "NO" << endl;
		else
			output << s-min << endl;
	}
	return 0;
}