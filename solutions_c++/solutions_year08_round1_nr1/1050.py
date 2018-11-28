// googleCodeContest.cpp : Defines the entry point for the console application.
//
// Stephan Carpenter (TsuQ)

#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <stdio.h>
using namespace std;

#include <fstream>
using namespace std;

#include <string>
using namespace std;

#include <math.h>

int main()
{
	ifstream f("A-small.in");
	ofstream of("A-small-out.txt");
	int cases;
	int temp;

	signed int myArray[2][1000];

	f >> cases;
	for(int x=0; x<cases; x++)
	{
		int numbers;
		f >> numbers;

		for(int y=0; y<2; y++)
		{
			for(int z=0; z<numbers; z++) // increments both
			{
				f >> myArray[y][z];
			}
		}
		int rounds;
		rounds=0;
		while(rounds<numbers)
		{
			for(int z=0; z<numbers-1; z++) // increments both
			{
				if(myArray[0][z]>myArray[0][z+1])
				{
					temp=myArray[0][z];
					myArray[0][z]=myArray[0][z+1];
					myArray[0][z+1]=temp;
				}

				if(myArray[1][z]<myArray[1][z+1])
				{
					temp=myArray[1][z];
					myArray[1][z]=myArray[1][z+1];
					myArray[1][z+1]=temp;
				}
			}
			rounds++;
		}

		long total;
		total=0;
		for(int y=0; y<numbers; y++)
		{
			total+=myArray[0][y]*myArray[1][y];
		}

		of << "Case #" << (x+1) << ": " << total << endl;
	}
	f.close();
	of.close();


	cout << "Done." << endl;

    char a;
	cin >> a;
	return 0;
}
