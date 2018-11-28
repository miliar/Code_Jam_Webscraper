#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("B-Large.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("B-Large.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	int N; //Numbers of googlers
	int S; //Numbers of surprising triplets <= N
	int p; //

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//输入
		inFile >> N/*input data receiver*/;
		inFile >> S/*input data receiver*/;
		inFile >> p/*input data receiver*/;
		//操作区
		int yMax = 0;
		int pTri = p*3;
		for (int j=0; j<N; j++)
		{
			int Tj; // Score of googler j
			inFile >> Tj;
			if (Tj >= pTri-2)
			{
				yMax++;
			}
			else if (Tj >= pTri-4)
			{
				if (S > 0 && Tj >= 2 && Tj <= 28)
				{
					S--;
					yMax++;
				}
			}
		}

		//输出
		outFile << "Case #" << i+1 << ": " << yMax << endl;
		outFile.flush();
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}