#include <fstream>

using namespace std;

int main()
{
	int N, A, B, counter;
	ifstream input;
	ofstream output;
	input.open("C-small-attempt2.in");
	output.open("output.txt");
	input >> N;
	for(int i = 1; i <= N; i++)
	{
		counter = 0;
		input >> A >> B;
		for(int j = A; j <= B; j++)
		{
			for(int k = j+1; k <= B; k++)
			{
				if(k < 100 && j < 100 && j > 10 && k > 10)
				{
					if(k/10 == j%10 && k%10 == j/10)
					{
						counter++;
					}
				}
				else if(k < 1000 && j < 1000 && j > 100 && k > 100)
				{
					if((k/10 == j%100 && k%10 == j/100) || (k%100 == j/10 && k/100 == j%10))
					{
						counter++;
					}
				}
			}
		}
		output << "Case #" << i << ": " << counter << endl;
	}
}