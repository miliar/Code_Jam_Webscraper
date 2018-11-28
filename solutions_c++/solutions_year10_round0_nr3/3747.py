#include <iostream>
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;

#include <string>
using std::string;

#include <queue>
using std::queue;

#include <cstdlib>

void solve();

int main(int argc, char* argv[])
{
	solve();
}

void solve()
{
	ifstream input_file("input.txt");
	string line;

	if (input_file.is_open())
	{
		getline(input_file, line);

		int no_cases = atoi(line.c_str());

		for (int i = 0; i < no_cases; i++)
		{
			int R = 0;				// number of times roller coaster will run
			int k = 0;				// max no. of people coaster can hold 
			int N = 0;				// size of group
			int money = 0;

			input_file >> R >> k >> N;

			queue<int> group;

			for (int j = 0; j < N; j++)
			{
				int temp;
				input_file >> temp;

				group.push(temp);
			}

			for (int iteration = 0; iteration < R; iteration++)
			{
				queue<int> tempGroup;
				int size = 0;

				for (int y = 0; y < group.size(); y++)
				{
					if (size + group.front() > k)
						break;

					tempGroup.push(group.front());
					group.pop();

					size += tempGroup.back();
					group.push(tempGroup.back());
				}

				money += size;
			}

			cout << "Case #" << i + 1 << ": " << money << endl;
		}
	}
}