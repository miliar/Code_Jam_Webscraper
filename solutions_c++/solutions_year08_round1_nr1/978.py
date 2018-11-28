#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

const char INFILE_NAME[]        = "in.in";
const char OUTFILE_NAME[]       = "gcj.Out";

ifstream fin;						// Input file
ofstream fout;						// Output file


int main()
{
	fout.open(OUTFILE_NAME, ios::out);

	if (fout)
	{
		fin.open(INFILE_NAME, ios::in);
	}

	int cases;
	fin >> cases;

	for( int acase = 0; acase < cases; acase++ )
	{
		int num;
		fin >> num;

		int sum = 0;

		int vec1[8];
		int vec2[8];
		for( int i = 0; i < num; i++)
		{
			fin >> vec1[i];
		}
		for( int i = 0; i < num; i++)
		{
			fin >> vec2[i];
		}

		for( int i = 0; i < num; i++)
		{
			sum += *max_element(vec1,vec1+num-i) * *min_element(vec2,vec2+num-i);

			bool bool1 = false;
			bool bool2 = false;

			for( int j = 0; j < num-i; j++)
			{
				if( !bool1 && vec1[j] == *max_element(vec1,vec1+num-i) )
				{
					vec1[j] = vec1[num-i-1];
					bool1 = true;
				}
				if( !bool2 && vec2[j] == *min_element(vec2,vec2+num-i) )
				{
					vec2[j] = vec2[num-i-1];
					bool2 = true;
				}
			}
		}

		cout << "Case #" << acase+1 << ": "  << sum << endl;
		fout << "Case #" << acase+1 << ": "  << sum << endl;
	}

	if (fin)
	{
		fin.close();
	}
	fout.close();

}
