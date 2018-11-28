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
	srand(12321);

	int i, j, k, l;
	int cases;

	ofstream of("C:\\Documents and Settings\\customer\\Desktop\\C-large-out.txt");	
//	ifstream f("C:\\Documents and Settings\\customer\\Desktop\\C-small.in");
	ifstream f("C:\\Documents and Settings\\customer\\Desktop\\C-large.in");


	f >> cases;



	char codejam[502]; // one extra for superstition? =]
	int current;
	const string stringInput="welcome to code jam";
	int length=stringInput.length();

	// extra value is for storing the total field
	int searchingFor[30]; // number of 'people' looking for the given letter
	int searchingForUpdate[30]; // number of 'people' looking for the given letter next loop
	searchingFor[0]=1; // there is always exactly one person searching for the first letter.


	f.getline(codejam, 501); // to deal with poor compatability between getline and streaming

	for(i=0; i<cases; i++)
	{
		f.getline(codejam, 501);
		current=0;

		for(j=1; j<(length+1); j++)
		{
			searchingFor[j]=0;
			searchingForUpdate[j]=0;
		}


		for(j=0; codejam[j]!='\0'; j++)
		{

			if(codejam[j]==stringInput[0])
			{
				searchingForUpdate[1]+=searchingFor[0]; // should be +1, done this way for generalization
			}

			for(k=1; k<length; k++)
			{
				if(codejam[j] == stringInput[k])
				{
					searchingForUpdate[k+1]=searchingFor[k+1] + searchingFor[k];
				}
			}



			for(k=1; k<length+1; k++) // apply the updates
			{
				searchingForUpdate[k]%=10000;
				searchingFor[k]=searchingForUpdate[k];
			}
		}

		of << "Case #" << i+1 << ": ";

		for (j=1; j<4; j++)
		{
			if(searchingFor[length]<pow(10.0,j))
			{
				of << '0';
			}
		}

		of << searchingFor[length] << endl;
	}

	return 0;
}