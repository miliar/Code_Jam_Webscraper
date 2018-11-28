#include <iostream>
#include <fstream>
#include <conio.h>
#include <ios>

#include <queue>

using namespace std;

void main()
{
	cout << "Press any key to execute." << endl;
	_getch();

	/*loading file section*/
	ifstream inFile;
	inFile.open("C-small-attempt1.in");
	if (!inFile.is_open())
	{
		cout << "Input File dose not exist." << endl;
		return;
	}

	/*reading file section*/
	//pre-reading
	ofstream outFile;
	outFile.open("C-small-attempt1.out", ios_base::out|ios_base::trunc);
	if (!inFile.is_open())
	{
		cout << "Output File could not open." << endl;
		return;
	}
	int case_Count;
	//add parameter to be used here
	long ride_count, seat_count, group_count;

	//reading procedure
	inFile >> case_Count;
	for (int i=0; i<case_Count; i++)
	{
		//²Ù×÷Çø
		queue<long> group_queue;
		queue<long> roller_queue;
		inFile >> ride_count >> seat_count >> group_count;
		for (int j=0; j<group_count; j++)
		{
			long tgroup;
			inFile >> tgroup;
			group_queue.push(tgroup);
		}
		long earning = 0;
		for (int j=0; j<ride_count; j++)
		{
			long tride = 0;// = group_queue.front();
			long tearning = 0;
			while (group_queue.front() <= seat_count-tride)
			{
				long tgroup = group_queue.front();
				roller_queue.push(tgroup);
				group_queue.pop();
				tride += tgroup;
				tearning = tride;
				if (group_queue.empty())
				{
					break;
				}
			}
			while (!roller_queue.empty())
			{
				group_queue.push(roller_queue.front());
				roller_queue.pop();
			}
			earning += tearning;
		}
		outFile << "Case #" << i+1 << ": " << earning << endl;
	}

	/*exit section*/
	cout << "Press any key to exit." << endl;
	_getch();
	inFile.close();
	outFile.close();
	return;
}