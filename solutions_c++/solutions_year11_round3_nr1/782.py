#include <cstdio>
#include <iostream>
#include <fstream>
//#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	//ifstream fin ("A-small-attempt0.in");
	ifstream fin ("A-large.in");
    //ofstream fout ("A-output-small.txt");
	ofstream fout ("A-output-large.txt");

	int cases = 0;
	fin >> cases;
	/*{string buffer;
	getline(fin,buffer);} //if needed to read the next lines as lines*/

	for(int i=0; i<cases; i++)
	{
		cout << "Case #"<<(i+1) <<":"<<endl;
		fout << "Case #"<<(i+1) <<":"<<endl;

		int rows;
		fin >> rows;
		int col;
		fin >> col;
		bool done = false;

		char **tiles = new char*[rows];

		for(int j=0; j<rows; j++)
		{
			tiles[j] = new char[col];
			int counter = 0;
			for(int k=0; k<col; k++)
			{
				fin >> tiles[j][k];
				if(tiles[j][k] == '#')
				{
					counter++;
					if(counter == 2)
						counter = 0;
				}
			}
			if(counter%2 != 0 && !done)
			{
				cout<<"Impossible"<<endl;
				fout<<"Impossible"<<endl;
				done = true;
			}
		}

		if(!done)
		{
		
			for(int j=0; j<col; j++)
			{
				int counter = 0;
				for(int k=0; k<rows; k++)
				{
					if(tiles[k][j] == '#')
					{
						counter++;
						if(counter == 2)
							counter = 0;
					}
				}
				if(counter%2 != 0 && !done)
				{
					cout<<"Impossible"<<endl;
					fout<<"Impossible"<<endl;
					done = true;
				}
			}
			if(!done)
			{
				for(int j=0; j<rows; j++)
				{
					for(int k=0; k<col; k++)
					{
						if(tiles[j][k] == '#')
						{
							tiles[j][k] = '/';
							tiles[j][k+1] = '\\';
							tiles[j+1][k] = '\\';
							tiles[j+1][k+1] = '/';
						}
						cout<<tiles[j][k];
						fout<<tiles[j][k];
					}
					cout<<endl;
					fout<<endl;
				}

			}
		}


		delete[] tiles;
	}
	system("pause");
	return 0;
}