#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;

int arr[15];
int largest;
int N;

void combination(int, int, int, int, int, int);
int main()
{
	int testcases;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0-out.in");
	
	fin>>testcases;
	for(int j=1;j<=testcases;j++)
	{
		largest = 0;
		fin>>N;
		for(int i=0;i<N;i++)
		{
			fin>>arr[i];
		}
	for(int i=0;i<N/2;i++)
	{
		combination(i,0,0,0,0,0);
		if(largest!=0)
		 break;
	}
	if(largest!=0)
		fout<<"Case #"<<j<<": "<<largest<<endl;
		else
		fout<<"Case #"<<j<<": "<<"NO"<<endl;
	}
	return 0;
}
void combination(int s, int sean, int patrick, int pos, int sum, int count)
{
	int tempsum, tempsean, temppatrick;
	for(int i=pos; i < N; i++)
	{
		tempsum = sum;
		tempsean = sean;
		temppatrick = patrick;
		tempsean ^= arr[i];
		for(int j=pos; j<i; j++)
		{
			temppatrick ^= arr[j];
			tempsum += arr[j];
		}
		if(s != count)
							combination(s, tempsean, temppatrick, i+1, tempsum, count+1);
		else
		{
			for(int j=i+1; j<N; j++)
			{
				temppatrick ^= arr[j];
				tempsum += arr[j];
				}
			if(temppatrick == tempsean && tempsum>largest && tempsean!=0 && temppatrick!=0)
					largest = tempsum;
		}
	}
}
	
