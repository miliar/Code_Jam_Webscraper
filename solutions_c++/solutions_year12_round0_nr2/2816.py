#include <fstream>

using namespace std;

int main()
{
	int T, N, S, p, t, counter;
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("output.txt");
	input >> T;
	for(int i = 1; i <= T; i++)
	{
		counter = 0;
		input >> N >> S >> p;
		for(int j = 0; j < N; j++)
		{
			input >> t;
			if(p == 0)
				counter++;
			else if( p == 1 && t > 0)
				counter++;
			else if(t >= 3*p - 2)
				counter++;
			else if(t == 3*p - 3 || t == 3*p - 4)
			{
				if( S > 0 && p != 1)
				{
					S--;
					counter++;
				}
			}
		}
		output << "Case #" << i << ": " << counter << endl;
	}
}