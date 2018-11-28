#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int T, n;
//int app[1000][1000];
vector<int> seq(200);

ifstream input;
ofstream output;

void printAnswer(int ans)
{
	if (ans < 10)
		output << "00" << ans << endl;
	else
		if (ans < 100)
			output << "0" << ans << endl;
		else
			output << ans << endl;
}

int main()
{
	input.open("C-small.in");
	output.open("C-small.out");

	seq[0] = 2;
	seq[1] = 6;
	for (int i = 2; i < 110; i++)
		seq[i] = (6 * seq[i-1] - 4 * seq[i-2] + 4000) % 1000;

	input >> T;
	for (int c = 0; c < T; c++)
	{
		input >> n;
		output << "Case #" << c + 1 << ": ";

		if (n < 100)
			printAnswer((seq[n] + 999) % 1000);
		else
		{
			n = n % 99 + 99;
			printAnswer((seq[n] + 999) % 1000);
		}
	}
	
	input.close();
	output.close();
}

	//for (int i = 0; i < 1000; i++)
	//	for (int j = 0; j < 1000; j++)
	//		app[i][j] = -1;

	//seq.push_back(2);
	//seq.push_back(6);
	//app[2][6] = 0;
	//int s = 2;

	//while (true)
	//{
	//	seq.push_back((6 * seq[s-1] - 4 * seq[s-2] + 4000) % 1000);
	//	s++;
	//	if (app[seq[s-2]][seq[s-1]] >= 0)
	//	{
	//		cout << "s = " << s << endl;
	//		cout << app[seq[s-2]][seq[s-1]] << endl;
	//		return 0;
	//	}
	//	else
	//		app[seq[s-2]][seq[s-1]] = s-1;
	//}