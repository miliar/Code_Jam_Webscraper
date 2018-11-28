// Rob Keim
// Google Code Jam - Qualifying Round
// Problem 2 - Train Timetable

#include <algorithm>
#include <deque>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

deque<double> depA, depB, arrA, arrB;
int N, T, NA, NB;
string tmp;
double t1, t2;

void parseLine(string asdf)
{
	t1 = atoi(asdf.substr(0, 2).c_str()) + (atoi(asdf.substr(3, 2).c_str()) / 60.0);
	t2 = atoi(asdf.substr(6, 2).c_str()) + (atoi(asdf.substr(9, 2).c_str()) / 60.0) + (T / 60.0);

	return;
}

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");

	getline(fin, tmp);
	N = atoi(tmp.c_str());
	for (int ctr = 1; ctr <= N; ctr++)
	{
		int numAtA = 0, numAtB = 0;
		depA.clear();
		depB.clear();
		arrA.clear();
		arrB.clear();
		getline(fin, tmp);
		T = atoi(tmp.c_str());
		
		getline(fin, tmp);
		int space;
		space = tmp.find(" ");
		NA = atoi(tmp.substr(0, space).c_str());
		NB = atoi(tmp.substr(space,tmp.length() - space).c_str());

		for (int i = 0; i < NA; i++)
		{
			getline(fin, tmp);
			parseLine(tmp);
			depA.push_back(t1);
			arrB.push_back(t2);

		}
		for (int i = 0; i < NB; i++)
		{
			getline(fin, tmp);
			parseLine(tmp);
			depB.push_back(t1);
			arrA.push_back(t2);
		}
		sort(depA.begin(), depA.end());
		sort(depB.begin(), depB.end());
		sort(arrA.begin(), arrA.end());
		sort(arrB.begin(), arrB.end());

		while (depA.size() > 0)
		{
			if ((arrA.size() == 0) || (depA.at(0) < arrA.at(0)))
			{
				numAtA++;
				depA.pop_front();
			}
			else
			{
				depA.pop_front();
				arrA.pop_front();
			}
		}
		while (depB.size() > 0)
		{
			if ((arrB.size() == 0) || (depB.at(0) < arrB.at(0)))
			{
				numAtB++;
				depB.pop_front();
			}
			else
			{
				depB.pop_front();
				arrB.pop_front();
			}
		}
		cout << "Case #" << ctr << ": " << numAtA << " " << numAtB << endl;
		fout << "Case #" << ctr << ": " << numAtA << " " << numAtB << endl;
	}

	return 0;
}
