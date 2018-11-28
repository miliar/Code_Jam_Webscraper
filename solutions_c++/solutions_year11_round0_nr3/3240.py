#include <cstdio>
#include <iostream>
#include <fstream>
//#include <string>
#include <math.h>

using namespace std;


int share1[15];
int share2[15];
int values[15];
bool mask[15];

int sum(int *a, int n)
{
	int out = 0;
	for(int i=0; i<n; i++)
	{
		out += a[i];
	}
	return out;
}

int xor(int *a, int n)
{
	int out = 0;
	for(int i=0; i<n; i++)
	{
		out = a[i]^out;
	}
	return out;
}

void plus(bool *mask, int n)
{
	for(int i=0; i<n; i++)
	{
		if(mask[i])
		{
			mask[i] = !mask[i];
		}
		else
		{
			mask[i] = !mask[i];
			break;
		}
	}
}

bool findShare(int *values, int n, int &max)
{
	unsigned long int size = powf(2,n)-2;
	max = 0;

	for(int j=0; j<n; j++)
		mask[j] = false;
	mask[0] = true;

	for(unsigned long int i=0; i<size; i++)
	{
		int count = 0, count2 = 0;
		for(int j=0; j<n; j++)
		{
			if(mask[j])
				share1[count++] = values[j];	
			else
				share2[count2++] = values[j];
		}

		if((xor(share2,count2)) == xor(share1,count))
		{
			int sharecount = sum(share1,count);
			int valuecount = sum(share2,count2);
			if(sharecount > valuecount && sharecount > max)
				max = sharecount;
			else if(valuecount > sharecount && valuecount > max)
				max = valuecount;
		}
		plus(mask, n);
	}
	if(max > 0)
		return true;
	return false;
}


int main(int argc, char* argv[])
{
	ifstream fin ("C-small-attempt1.in");
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

		int candies;
		fin>>candies;

		for(int j=0; j<candies; j++)
		{
			fin>>values[j];
		}

		int share;

		if(candies == 2)
		{
			if(values[0] == values[1])
			{
				cout<<values[0];
				fout<<values[1];
			}
			else
			{
				cout<<"NO";
				fout<<"NO";
			}
		}
		else if(findShare(values, candies, share))
		{
			cout<<share;
			fout<<share;
		}
		else
		{
			cout<<"NO";
			fout<<"NO";
		}

		//delete values;
		cout <<endl;
		fout <<endl;
	}
	system("pause");
	return 0;
}