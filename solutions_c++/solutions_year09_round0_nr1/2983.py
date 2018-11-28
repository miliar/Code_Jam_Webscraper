#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
 
using namespace std;

typedef __int64 ll;

int startarr[20];
int cntarr[20];
int presentarr[20];

int D, L;

ll totcnt;

string ip;

vector <string> dict;


void preprocess(string ip)
{
	int pos = 0;

	for(int k = 0; k < ip.size();)
	{
		
		if(ip[k] == '(')
		{
			k++;
			startarr[pos] = k;
			int len = 0;
			for(;k < ip.size();)
			{
				if(ip[k] == ')')
				{
					cntarr[pos] = len;
					k++;
					pos++;
					break;
				}
				else
				{
					len++;
					k++;
				}
			}
		}
		else
		{
			startarr[pos] = k;
			cntarr[pos] = 1;
			pos++;
			k++;
		}
	}
}

int compare(string gen, int k, int d)
{
	if(gen[k] == dict[d][k])
	{
		return d;
	}
	else
	{
		for(; d < D; d++)
		{
			int val;
			val = dict[d].compare(0, (k+1), gen);
			if(val < 0)
			{
				continue;
			}
			else if(val == 0)
				return d;
			else
				break;
		}
	}
	return 0xFFFFFFFF;
}

void gensequence(string gen, int k, int d)
{
	if(k == L)
	{
		totcnt++;
		return;
	}
	else
	{
		while(presentarr[k] < cntarr[k])
		{
			gen += ip[startarr[k]+presentarr[k]];
			presentarr[k]++;
			int val;
			if((val = compare(gen, k, d)) != 0xFFFFFFFF)
			{
				gensequence(gen, k+1, val);
			}
			gen.resize(k);
			if(k == 0)
				d = 0;
		}
		presentarr[k] = 0;
		return;
	}
}



int main(int argc, char *argv[])
{
	ifstream fin;
	ofstream fout;

	fout.open("outputfile.txt");

	fin.open(argv[1]);

	int N;

	fin >> L >> D >> N;

	getline(fin,ip);

	dict.resize(D);

	for(int i = 0; i < D; i++)
	{
		getline(fin,ip);
		dict[i] = ip;
	}

	sort(dict.begin(), dict.end());



	for(int j = 0; j < N; j++)
	{
		getline(fin, ip);

		preprocess(ip);

		string gen;
		totcnt = 0;

		for(int k = 0; k < L; k++)
		{
			presentarr[k] = 0;
		}
		gensequence(gen, 0, 0);

		fout << "Case #" << j+1 << ": " << (int)totcnt <<"\n";

		printf("Cnt = %d\n", j);

	}

	return 0;
}

