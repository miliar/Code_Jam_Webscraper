#include <iostream>
#include <fstream>
#include <bitset>
#include <cstdlib>

using namespace std;

char base_elements[] =  {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
static const int nBaseEls = sizeof(base_elements) / sizeof(char);
static const int NMax = 100;
char gen[nBaseEls][nBaseEls];
bitset<nBaseEls> neg[nBaseEls];

void clearTables()
{
	memset(gen, 0, sizeof(gen));
	memset(neg, 0, sizeof(neg));
}

int toIndex(char c)
{
	for (int i = 0; i < nBaseEls; i++)
		if (base_elements[i] == c)
			return i;

	return -1;
}

void readC(istream & fin)
{
	int C;
	fin >> C;
	for (int nC = 0; nC < C; nC++)
	{
		string couple;
		fin >> couple;
			
		int a = toIndex(couple[0]);
		int b = toIndex(couple[1]);
		gen[a][b] = couple[2];
		gen[b][a] = couple[2];
	}
}

void readD(istream & fin)
{
	int D;
	fin >> D;
	for (int nD = 0; nD < D; nD++)
	{
		string couple;
		fin >> couple;
			
		int a = toIndex(couple[0]);
		int b = toIndex(couple[1]);
		neg[a][b] = true;
		neg[b][a] = true;
	}
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	int T;
	fin >> T;
	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		clearTables();

		readC(fin);
		readD(fin);

		bitset<nBaseEls> forbidden, prevForbidden;
		char element_list[NMax];
		int nElements = 0;
		
		int N;
		fin >> N;

		string invoked;
		fin >> invoked;
		
		for (int iInvoked = 0; iInvoked < N; iInvoked++)
		{
			element_list[nElements++] = invoked[iInvoked];

			if (nElements == 1)
			{
				prevForbidden = forbidden;
				forbidden |= neg[ toIndex(element_list[0]) ];
				continue;
			}

			int iA = toIndex(element_list[nElements - 1]);
			int iB = toIndex(element_list[nElements - 2]);
			char g;
			if (iA >= 0 && iB >= 0 && (g = gen[iA][iB]) != 0)
			{
				element_list[nElements - 2] = g;
				nElements--;
				forbidden = prevForbidden;
			}
			else if (forbidden[iA])
			{
				nElements = 0;
				forbidden = 0;
			}
			else
			{
				prevForbidden = forbidden;
				forbidden |= neg[iA];
			}
		}

		fout << "Case #" << nTestCase << ": [";
		for (int i = 0; i < nElements; i++)
		{
			if (i)
				fout << ", ";
			fout << element_list[i];
		}
		fout << "]" << endl;
	}

	return 0;
}
