#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

typedef __int64 ll;

int present[256];

int pos[256][100];

int main()
{

	ifstream fin;
	ofstream fout;

	string ip;

	fin.open ("input.txt", ifstream::in);

	fout.open("output.txt");

	int N;

	fin >> N;

	getline(fin, ip);

	for(int i = 0; i < N; i++)
	{
		ip.resize(0);

		getline(fin, ip);

		for(int j = 0; j < 256; j++)
		{
			present[j] = 0;
		}

		for(j = 0; j < ip.size(); j++)
		{
				pos[ip[j]][present[ip[j]]] = j;
				present[ip[j]] += 1;
				
		}

		int numvalues = 0;

		for(j = 0; j < 256; j++)
		{
			if(present[j] > 0)
			{
				numvalues++;
			}
		}

		int temp[100];

		int num = 0;

		for(j = 0; j < ip.size(); j++)
		{
			if(present[ip[j]] > 0)
			{
				for(int k = 0; k < present[ip[j]]; k++)
				{
					temp[pos[ip[j]][k]] = num;
				}
				present[ip[j]] = 0;
				num++;
			}
			
		}
		for(j = 0; j < ip.size(); j++)
		{
			if(temp[j] == 0)
			{
				temp[j] = 1;
			}
			else if(temp[j] == 1)
			{
				temp[j] = 0;
			}
		}



		

		ll out;

		out = 0;

		ll basevalue = 1;

		if(numvalues == 1)
			numvalues = 2;
		for(j = ip.size()-1; j >= 0; j--)
		{
			out += temp[j]*basevalue;
			basevalue = basevalue*numvalues;
		}

		char outchar[100];

		int numvar;
		numvar = 0;
		while(out > 0)
		{
			outchar[numvar] = (out%10) + '0';
			out = out/10;
			numvar++;
		}

		

		fout << "Case #" << i+1 << ": " ; 
		for(j = numvar-1; j >= 0; j--)
		{
			fout << outchar[j];
		}

		fout << "\n";
		
		
	}

	return 0;
	

}