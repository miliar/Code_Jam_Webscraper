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

	int i, j, k;
	string temp;

	ofstream of("C:\\Documents and Settings\\customer\\Desktop\\A-small-out.txt");	
	//ifstream f("C:\\Documents and Settings\\customer\\Desktop\\A-small.in");
	ifstream f("C:\\Documents and Settings\\customer\\Desktop\\A-large.in");

	string D[5000];
	string Lin[15];

	int L_length;
	int D_length;
	int cases;

	char tokens[400];

	f >> L_length;
	f >> D_length;
	f >> cases;

	for(i=0; i<D_length; i++)
	{
		f >> D[i];
	}

	f.getline(tokens, 395); // prime the reading of new format

	int filter[15];
	int wordsSuccessful;
	int mode;
	int fail;

	for(i=0; i<cases; i++)
	{
		for(j=0; j<L_length; j++)
		{
			filter[j]=0;
		}

		of << "Case #" << (i+1) << ": ";

		f.getline(tokens, 395);
		j=0; // letter in token set
		k=0; // letter number
		mode=0; // inbetween mode
		while(tokens[j]!='\0')
		{
			if(mode==0)
			{
				if(tokens[j]=='(')
				{
					mode=1; // multiple input mode
				} else if(tokens[j]==' ')
				{
					 // ignore spaces
				} else {
					filter[k] |= 1 << (tokens[j]-97);
					k++; // there is only one letter outside parenthesis, go to the next one
				}
			} else {
				if(tokens[j]==')')
				{
					mode=0; // back to between mode
					k++; // now on the next letter to analyze
				} else { // only letters between parenthesis
					filter[k] |= 1<< (tokens[j]-97);
				}
			}
			j++;
		} // end of filter set up		


		// check the words
		wordsSuccessful=0;
		for(j=0; j<D_length; j++)
		{
			//cout << D[j] << " : ";
			fail=0;
			for(k=0; k<L_length; k++)
			{
				fail|=((1 << (D[j][k] -97 )) | filter[k]) ^ filter[k];

				//cout <<  fail << ", " ;
			}

			if(!fail)
			{
				wordsSuccessful++;
			}
		}
		//cout << endl;
		of << wordsSuccessful << endl;
	}

	cout << endl << "done";
	char pause;
	cin >> pause;

	return 0;
}


