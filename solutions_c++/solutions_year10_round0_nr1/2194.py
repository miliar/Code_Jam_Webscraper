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
	inFile.open("A-large.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("A-large.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	int snapper_count;
	long snap_times;

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//²Ù×÷Çø
		inFile >> snapper_count;
		inFile >> snap_times;
		long j = 1;
		for (int k=0; k<snapper_count; k++)
		{
			j &= snap_times;
			if (!j)
			{
				break;
			}
			snap_times >>= 1 ;
		}
		outFile << "Case #" << i+1 << ": ";
		if (j)
		{
			outFile << "ON" <<endl;
		}
		else
		{
			outFile << "OFF" << endl;
		}
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}