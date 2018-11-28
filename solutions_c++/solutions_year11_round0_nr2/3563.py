#include <iostream>
#include <fstream>

using namespace std;

bool isOpposed(char, char);
char isCombine(char, char);


int numCase;
int numCombine;
int numOpposed;
int numInvoke;

char n[101];
char c1[37];
char c2[37];
char c3[37];
char d1[29];
char d2[29];

int main()
{
	ifstream fin("input.txt",ios::in);
	ofstream fout("output.txt",ios::out);

	int i,j,k,l;
	char tmpCombine = '!';
	bool isFirst = true;

	char tmp[4];

	fin >> numCase;

	for(i=0; i<numCase; i++)
	{

		fin >> numCombine;
		for(j=0; j<numCombine; j++)
		{
			fin >> tmp;
			c1[j] = tmp[0];
			c2[j] = tmp[1];
			c3[j] = tmp[2];
		}
		fin >> numOpposed;
		for(j=0; j<numOpposed; j++)
		{
			fin >> tmp;
			d1[j] = tmp[0];
			d2[j] = tmp[1];
		}
		fin >> numInvoke;
		fin >> n;
		for(j=1; j<numInvoke; j++)
		{
			tmpCombine = isCombine(n[j],n[j-1]);
			if(tmpCombine != '!')
			{
				n[j-1] = '!';
				n[j] = tmpCombine;
			}
			for(k=0; k<j; k++)
			{
				if(isOpposed(n[k],n[j]))
				{
					for(l=0; l<=j; l++)
					{
						n[l] = '!';
					}
				}
			}
		}

		fout << "Case #" << i+1 << ": [" ;
		for(j=0; j<numInvoke; j++)
		{
			if(n[j] != '!')
			{
				if(isFirst)
				{
					isFirst = false;
					fout << n[j];
				}
				else
				{
					fout << ", " << n[j];
				}
			}
		}
		isFirst = true;
		fout << "]" << endl;
	}

}

bool isOpposed(char a, char b)
{
	for(int i=0; i<numOpposed; i++)
	{
		if(d1[i] == a)
			if(d2[i] == b)
				return true;
		if(d2[i] == a)
			if(d1[i] == b)
				return true;
	}
	return false;
}

char isCombine(char a, char b)
{
	for(int i=0; i<numCombine; i++)
	{
		if(c1[i] == a)
			if(c2[i] == b)
				return c3[i];
		if(c2[i] == a)
			if(c1[i] == b)
				return c3[i];
	}
	return '!';
}