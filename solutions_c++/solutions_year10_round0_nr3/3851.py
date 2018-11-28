//Timothy Wang
//timzwang@gmail.com

#include <queue>
#include <fstream>
#include <iostream>

using namespace std;

typedef short type;	//big: int
typedef int money;	//big: long?

int main()
{
	ifstream fin;
	fin.open("C-small-attempt1.in");
	ofstream fout;
	fout.open("C.in");
	short numTest;
	short test = 1;
	fin >> numTest;
	while(test <= numTest)
	{
		//Setup:
		type numRuns, carSize;
		short numGroups;
		fin >> numRuns >> carSize >> numGroups;
		queue<type> line;
		int i = 0;
		while(i < numGroups)
		{
			type group;
			fin >> group;
			line.push(group);
			i++;
		}

		//Code:
		money euros = 0;
		while(numRuns != 0)
		{
			type tempCar = 0;
			type car = 0;
			short entered = 0;
			while(true)
			{
				if(entered == numGroups)
					break;
				type curr = line.front();
				tempCar += curr;
				if(tempCar <= carSize)
				{
					car += curr;
					euros += curr;
					line.pop();
					line.push(curr);
				}
				else
					break;
				entered++;
			}
			numRuns--;
		}
		fout << "Case #" << test << ": " << euros << endl;
		test++;
	}
	fin.close();
	fout.close();
}