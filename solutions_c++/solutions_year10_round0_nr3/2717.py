#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <queue>

using namespace std;

class ThemePark
{
	int R, k, N, g;
	int testcaseNum;
	ifstream& input;
	ofstream& output;
public:
	ThemePark(ifstream& input, ofstream& output) : input(input), output(output) {}
	void runtc()
	{
		string line;
		input >> testcaseNum;
		getline(input, line);	// skip new line character of first line
		for (int i = 0; i < testcaseNum; i++)
		{
			input >> R >> k >> N;
			getline(input, line);
			queue<int> groups;
			for (int j = 0; j < N; j++)
			{
				input >> g;
				groups.push(g);
			}
			getline(input, line);

			int sum = 0;
			int partialSum = 0;
			queue<int> baseGroups = groups;
			int round = 0;

			for (int j = 1; j <= R; j++)
			{
				queue<int> temp;
				int people = 0;
				while (true)
				{
					if (people + groups.front() > k)
						break;
					g = groups.front();
					people += g;
					groups.pop();
					temp.push(g);
					if (groups.empty())
						break;
				}
				while (!temp.empty())
				{
					groups.push(temp.front());
					temp.pop();
				}
				sum += people;
				if (groups == baseGroups)
				{
					round = j;
					partialSum = sum;
					break;
				}
			}

			if (round > 0)
			{
				sum = 0;
				int mod = R % round;
				int divisor = R / round;
				sum += divisor*partialSum;

				for (int j = 0; j < mod; j++)
				{
					queue<int> temp;
					int people = 0;
					while (true)
					{
						if (people + groups.front() > k)
							break;
						g = groups.front();
						people += g;
						groups.pop();
						temp.push(g);
						if (groups.empty())
							break;
					}
					while (!temp.empty())
					{
						groups.push(temp.front());
						temp.pop();
					}
					sum += people;
				}
			}
			output << "Case #" << i + 1 << ": " << sum << endl;
		}
	}
};

int main(int argc, char* argv[])
{
	ifstream input(argv[1]);
	ofstream output(argv[2]);
	ThemePark t(input, output);
	t.runtc();
}
