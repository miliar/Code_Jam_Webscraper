// CodeJam.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{

	ifstream fin("B-small.in");
	ofstream fout("Output.txt");

	if (fin.fail())
	{
		fout << "No se puede abrir arcihvo";
		fin.close();
		fout.close();
		return 1;
	}

	int cantTest;
	char aux;
	fin >> cantTest >> aux;
	fin.putback(aux);

	for (int i = 0; i < cantTest; i++)
	{
		//char lastNumber[21];
		string lastNumber;

		int cantNum[11] = {0,0,0,0,0,0,0,0,0,0,0};
		int cantCur[11] = {0,0,0,0,0,0,0,0,0,0,0};
		int sigDig[11] = {0,0,0,0,0,0,0,0,0,0,0};

		getline(fin, lastNumber);

		int sizeFirst = lastNumber.size();
		for (int j = 0; j < sizeFirst; j++)
		{
			lastNumber.insert(lastNumber.begin(), '0');
		}

		for (int j = 0; j < lastNumber.size(); j++)
		{
			cantNum[lastNumber.at(j) - 48]++;
		}
		cantNum[0] = 0;

		int sig = 0;
		for (int j = 10; j >= 0; j--)
		{
			sigDig[j] = sig;
			if (cantNum[j] > 0) { sig = j; }
		}

		/*for (int j = 0; j < 11; j++)
		{
			fout << sigDig[j] << ' ';
		}
		fout << endl;*/

		bool found = false;

		while (!(found))
		{

			int h = lastNumber.size() - 1;
			do {
				lastNumber.at(h) = sigDig[lastNumber.at(h) - 48] + 48;
				h--;
			} while ((h >= 0) && (lastNumber.at(h+1) == '0'));

			for (int j = 0; j < 11; j++)
			{
				cantCur[j] = 0;
			}
			for (int j = 0; j < lastNumber.size(); j++)
			{
				cantCur[lastNumber.at(j) - 48]++;
			}
			cantCur[0] = 0;

			for (int j = 0; j < 11; j++)
			{
				cout << cantCur[j] << ' ';
			}


			found = true;
			for (int j = 0; j < 11; j++)
			{
				if (cantCur[j] != cantNum[j]) { found = false; }
			}

		}

		while (lastNumber.at(0) == '0') {
			lastNumber.erase(lastNumber.begin());
		}
		
		fout << "Case #" << (i+1) << ": " <<  lastNumber << endl;
	}

	fin.close();
	fout.close();
	
	return 0;
}

