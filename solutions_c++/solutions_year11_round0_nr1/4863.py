#include <iostream>
#include <fstream>
using namespace std;

int main () {
	ifstream fin ("input.in");
	ofstream fout("output.out");
	int N = 0;
	fin >> N;

	for (int i = 1; i <= N; i++)
	{
		int P = 0;			fin >> P;
		//cout << "Case #" << i << endl;
		int oTargets[P];	int oTargetsCount = 0;
		int bTargets[P];	int bTargetsCount = 0;
		int turns[P];
		for (int j = 0; j < P; j++)
		{
			char c = 'O';	fin >> c;
			if (c == 'O')
			{
				fin >> oTargets[oTargetsCount];
				//cout << "O: " << oTargets[oTargetsCount] << endl;
				turns[j] = 0;
				oTargetsCount++;
			}
			else
			{
				fin >> bTargets[bTargetsCount];
				//cout << "B: " << bTargets[bTargetsCount] << endl;
				turns[j] = 1;
				bTargetsCount++;
			}
		}

		int oPosition = 1;	int oTarget = 1;	int oIndex = 0;
		int bPosition = 1;	int bTarget = 1;	int bIndex = 0;
		int turn = 0;		int t = 0;			bool changeTurn = false;
		while (turn < P)
		{
			t++;
			oTarget = oTargets[oIndex];

			//cout << "Time: "<< t << ", Turn: " << turns[turn] << endl;
			//cout << "O: " << oPosition << " -> " << oTarget << endl;

			if (oTarget > oPosition)
				oPosition++;
			else if (oTarget < oPosition)
				oPosition--;
			else if (turns[turn] == 0)
			{
				changeTurn = true;
				oIndex++;
			}

			bTarget = bTargets[bIndex];
			//cout << "B: " << bPosition << " -> " << bTarget << endl;
			if (bTarget > bPosition)
				bPosition++;
			else if (bTarget < bPosition)
				bPosition--;
			else if (turns[turn] == 1)
			{
				changeTurn = true;
				bIndex++;
			}

			if (changeTurn)
			{
				turn++;
				changeTurn = false;
			}
		}

		fout << "Case #" << i << ": " << t << endl;
		cout << "Case #" << i << ": " << t << endl;
	}

	fout.close();
	return 0;
}
