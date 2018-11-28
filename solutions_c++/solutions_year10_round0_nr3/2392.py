#include <fstream>
#include <iostream>
#include <queue>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream infile;
	infile.open("C-small.in");

	int test_cases = 0;
	infile >> test_cases;

	for (int i = 0; i < test_cases; i++)
	{
		queue<int> line;
		int euros = 0;

		int R = 0, k = 0, N = 0;
		infile >> R >> k >> N;

		for (int j = 0; j < N; j++)
		{
			int group = 0;
			infile >> group;
			line.push(group);
		}

		for (int x = 0; x < R; x++)
		{
			int seats = k;
			queue<int> on_coaster;
			while (seats >= 0)
			{
				// If the group can get on the roller coaster, put them on
				if (line.empty())
					break;
				if (seats - line.front() >= 0)
				{
					euros += line.front();
					seats -= line.front();
					on_coaster.push(line.front());
					line.pop();
				} else {
					break;
				}
			}

			while (!on_coaster.empty())
			{
				line.push(on_coaster.front());
				on_coaster.pop();
			}
		}

		printf("Case #%i: %i\n", i + 1, euros);
	}
}