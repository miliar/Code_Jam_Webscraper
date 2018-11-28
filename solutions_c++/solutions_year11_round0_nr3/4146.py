/*
	Reference: http://code.google.com/codejam
	Case name: Candy Splitting
	Created by IndoChoi
*/

#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

class GoogleCodeJam
{
private:
	// <-- Implementation here
	void Solve()
	{
		const int BUFFER_MAX = 1024*10;
		char bufLine[BUFFER_MAX] = {0};
		int nItem = 0;
		int *arrItem = 0;
		char *pItem = 0;
			
		cout << "Test Count: " <<  TestCount() << endl;
		for (int i = 0; i < TestCount(); i++)
		{
			int nXOR = 0;
			int minValue = 0;
			int addValue = 0;
			int counter = 0;
			
			fout << "Case #" <<  i+1 << ": ";

			fin.getline(bufLine,sizeof(bufLine));
			nItem = atoi(bufLine);
			arrItem = new int[nItem];
			
			fin.getline(bufLine,sizeof(bufLine));
			pItem = strtok (bufLine," ");
			while (pItem)
			{
				arrItem[counter++] = atoi(pItem);
				
				if (!minValue)
					minValue = arrItem[counter-1];
				else if (arrItem[counter-1] < minValue) 
					minValue = arrItem[counter-1];
					
				nXOR ^= arrItem[counter-1];
				addValue += arrItem[counter-1];
				
				pItem = strtok (0, " ");
			}

			if (nXOR) fout << "NO";
			else fout << addValue - minValue;
			
			delete [] arrItem;
			fout << endl;
		}	
	}
	// --> End Implementation
	
	ifstream fin;
	ofstream fout;
	bool isOpen;

	int TestCount()
	{
		static int count = 0;
		if (!count)
		{
			char buff[32] = {0};
			fin.getline(buff,sizeof(buff));
			count = atoi(buff);
		}
		return count;
	}	
public:
	GoogleCodeJam()
	{
		isOpen = false;
		fin.open("codejam.in");
		if (fin.is_open())
		{
			fout.open("codejam.out");
			isOpen = true;
		}
	}
	virtual ~GoogleCodeJam()
	{
		if (isOpen)
		{	
			fin.close();
			fout.close();
		}		
	}
	void Run()
	{
		if (isOpen)
			Solve();
		else
			cout << "Error opening input file!" << endl;
	}
};

int main()
{
	GoogleCodeJam().Run();
	return 0;
}