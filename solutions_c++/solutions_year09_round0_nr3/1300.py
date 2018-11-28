#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstring>

using namespace std;

int main(int argc, char *argv[])
{
	fstream fin;
	fstream fout;
	fin.open("c.in");
	fout.open("c.out", ios_base::app);
	//
    int n;
    fin >> n;
	char x[500];
	fin.getline(x, 500);
    for(int i=0; i<n; i++)
    {
        char line[501];
		char word[20]="welcome to code jam";
		//fout << strlen(word) << endl;
		fin.getline(line, 501);
		int tab[500][19];
		for(int j=0; j<500; j++)
		{
			for(int k=0; k<19; k++)
			{
				tab[j][k]=0;
			}
		}
		/*for(int j=0; j<19; j++)
		{
			tab[0][j]=0;
		}*/
		if(line[0]=='w') tab[0][0]=1;
		for(int j=1; j<strlen(line); j++)
		{
			for(int k=0; k<19; k++)
			{
				for(int l=1; l<19; l++)
				{
					if(word[l]==line[j])
					{
						tab[j][l]=tab[j-1][l-1]+tab[j-1][l];
						tab[j][l]%=10000;
					}
					else
					{
						tab[j][l]=tab[j-1][l];
					}
				}
				if('w'==line[j])
				{
					tab[j][0]=tab[j-1][0]+1;
					tab[j][0]%=10000;
				}
				else
				{
					tab[j][0]=tab[j-1][0];
				}
			}
		}
		if(tab[strlen(line)-1][18]<10)
			fout << "Case #" << i+1 << ": 000" << tab[strlen(line)-1][18] << endl;
		else if(tab[strlen(line)-1][18]<100)
			fout << "Case #" << i+1 << ": 00" << tab[strlen(line)-1][18] << endl;
		else if(tab[strlen(line)-1][18]<1000)
			fout << "Case #" << i+1 << ": 0" << tab[strlen(line)-1][18] << endl;
		else
			fout << "Case #" << i+1 << ": " << tab[strlen(line)-1][18] << endl;
    }
	//
    fin.close();
	fout.close();
    return 0;
}
