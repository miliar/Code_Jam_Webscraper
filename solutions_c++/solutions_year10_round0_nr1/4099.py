#include <fstream>
#include <string>

using namespace std;

int main()
{
	string solutions[10000];
	int cases=0, N=0, K=0, counter=0, SCounter=0, initial=1, intHelp=1, doubler=1;

	string fileName="A-large.in";
	ifstream infile(fileName.c_str());
	ofstream outfile("outfiler.txt");

	infile>>cases;

	while(counter<cases)
	{
		counter++;
		infile>>N>>K;
		initial=1;
		doubler=1;
		intHelp=1;
		while(N!=initial)
		{
			initial++;
			doubler*=2;
			intHelp+=doubler;
		}

		if(K==intHelp)
		{
			solutions[SCounter]="ON";
		}
		else
		{
			solutions[SCounter]="OFF";
			initial=intHelp;
			intHelp++;
			while(K>initial)
			{
				initial+=intHelp;
				if(K==initial)
				{
					solutions[SCounter]="ON";
				}
			}
		}

		SCounter++;
	}

	

	for(int i=0; i<cases; i++)
		outfile<<"Case #"<<(i+1)<<": "<<solutions[i]<<endl;

	return 0;
}