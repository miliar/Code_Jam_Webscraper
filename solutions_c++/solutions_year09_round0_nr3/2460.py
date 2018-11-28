#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

char line[31];
int test(int index, int nextletter);
char base[20] = "welcome to code jam";
int linelength;
int sum;


int main()
{
	
	ifstream fin("C-small-attempt2.in");
	ofstream fout("output.txt");
	
	int n_testcase;
	fin.getline(line, 31, '\n');
		
	n_testcase = atoi(line);

	for(int i=0; i<n_testcase; i++)
	{
		fin.getline(line, 31, '\n');
		//cout << line << endl;
	    linelength = strlen(line);
		int nextletter = 0;

		sum = 0;

		for(int j=0; j<linelength+1; j++)
		{
			if(line[j] == 'w')
			{
				test(j+1, 1);
			}
		}
		
		fout << "Case #" << i+1 <<": ";
		int temp = sum;
		if(1000 <= sum && sum < 10000)
			fout << "";
		if(100 <= sum && sum < 1000)
			fout << "0";
		if(10 <= sum && sum < 100)
			fout << "00";
		if(0<= sum && sum < 10)
			fout << "000";

		fout << sum << endl;
		
	}
	return 1;
}
int test(int index, int nextletter)
{
 	for(int i=index; i<linelength+1; i++)
	{
		if(line[i] == base[nextletter])
		{
			
			test(i+1, nextletter+1);
			if(nextletter == 18)
			{
				sum += 1;
			}
		}
	}

	return 0;
}
