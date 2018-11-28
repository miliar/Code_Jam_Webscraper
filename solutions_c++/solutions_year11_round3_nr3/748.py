#include <cstdio>
#include <iostream>
#include <fstream>
//#include <string>
#include <math.h>

using namespace std;


int main(int argc, char* argv[])
{
	ifstream fin ("C-small-attempt0.in");
	//ifstream fin ("C-large.in");
    ofstream fout ("C-output-small.txt");
	//ofstream fout ("C-output-large.txt");

	int cases;
	fin >> cases;
	/*{string buffer;
	getline(fin,buffer);} //if needed to read the next lines as lines*/

	for(int i=0; i<cases; i++)
	{
		cout << "Case #"<<(i+1) <<": ";
		fout << "Case #"<<(i+1) <<": ";

		int n;
		fin >> n;
		int l;
		fin >> l;
		int h;
		fin >> h;

		
		int *other = new int[n];

		for(int j=0; j<n; j++)
		{
			fin >> other[j];
		}

		
		int k = h-l + 1;
		//int *notes = new int[k];
		bool found = false;
		for(int j=0; j<k; j++)
		{
			bool canplay = true;
			for(int jj=0; jj<n; jj++)
			{
				if((j+l)%other[jj] != 0 && other[jj]%(j+l) != 0)
					canplay = false;
			}
			if(canplay && !found)
			{
				cout<<(j+l)<<endl;
				fout<<(j+l)<<endl;
				found = true;
			}
		}

		if(!found)
		{
			cout<<"NO"<<endl;
			fout<<"NO"<<endl;
		}


		//delete [] notes;
		delete [] other;
	}
	system("pause");
	return 0;
}