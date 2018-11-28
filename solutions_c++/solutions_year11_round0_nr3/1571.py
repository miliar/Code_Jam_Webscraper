#include<iostream>
#include <fstream>


using namespace std;

ifstream fin("candy_large.in");
ofstream fout("candy_large.out");

const int SIZE = 1000;
int cas, index=1;
int n;
int arr[SIZE];
int result =0;

void read()
{
	fin >> n;

	for (int i=0; i < n; i ++)
	{
		fin >> arr[i];
	}

	result =0;
}

void candy()
{
	int small = 0x7fffffff;

	int psum = 0;

	for (int i=0; i<n; i ++)
	{
		if (arr[i] < small)
		{
			small = arr[i];
		}
		psum = psum ^ arr[i];
		result += arr[i];
	}

	if (psum == 0)
	{
		result -= small;
	}
	else
		result = 0;
}

void print()
{
	if (result == 0)
	{
		fout << "Case #" << index<<": NO"<<endl;
	}
	else
		fout <<"Case #"<<index<<": "<<result<<endl;	
}

int main()
{
	fin >> cas;

	while (index <= cas)
	{
		read();
		candy();
		print();
		index ++;
	}

	return 0;
}
