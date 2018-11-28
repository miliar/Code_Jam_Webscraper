#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>

using namespace std;

struct robot
{
	char name;
	int pos;

	explicit robot(char name) : name(name), pos(1) {}
};

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int total = 0;
		robot O('O'), B('B');
		robot *pLastRobot = &O;
		int movesBudget = 0;

		int N;
		fin >> N;
		while (N--)
		{
			char name;
			int position;
			fin >> name >> position;

			if (name == pLastRobot->name)
			{
				int cost = abs(position - pLastRobot->pos) + 1;
				movesBudget += cost;
				total += cost;
			}
			else
			{
				pLastRobot = name == 'O' ? &O : &B;
				int cost = abs(position - pLastRobot->pos) + 1 - movesBudget;
				if (cost <= 0)
					cost = 1;
				movesBudget = cost;
				total += cost;
			}
			pLastRobot->pos = position;
		}

		fout << "Case #" << nTestCase << ": " << total << endl;
	}
}
