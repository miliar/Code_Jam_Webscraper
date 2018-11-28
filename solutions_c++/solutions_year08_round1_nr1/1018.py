// Permute.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
//#include<conio.h>
//#include<iomanip.h>
using namespace std;
void perm(int);

long long n,r,k,t,i;                //i:index no of permutations
long long arr1[2000], arr2[2000];
long long a[2000];
long long sum;
int testCases;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin;
	fin.open("c:\\Codejam\\Prob1.txt");
	fin>>testCases;
	ofstream fout;
	fout.open("c:\\Codejam\\Prob1.out");
	for(int i=0;i<testCases;i++)
	{
		fin>>n;
		r = n;
		for(int j = 1;j<=n;j++)
		{
			fin>>arr1[j];
		}

		for(int j = 1;j<=n;j++)
		{
			fin>>arr2[j];
		}

		for(k=1;k<=n;k++)
		{
			a[k] = k;
		}
		sum = 9223372036854775807;
		k=1;
		perm(k);
		fout<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	fin.close();
	fout.close();
}

void perm(int k)
{
	long long j,l,temp;
	for(j=k;j<=n;j++)
	{
		temp=a[k];
		a[k]=a[j];
		a[j]=temp;
		{
			if(k<r)
				perm(k+1);
			else
			{

				//for(l=1;l<=r;l++)
				//	cout<<a[l];

				long long tSum = 0;
				for(int m = 1;m<=r;m++)
				{
					tSum = tSum+ (arr1[a[m]] * arr2[m]);
				}
				if (tSum < sum)
				{
					sum = tSum;
				}
				//for(int m = 0;
				//		  getche();               //to  view the permutations one by
				// one
			}
			temp=a[k];
			a[k]=a[j];
			a[j]=temp;

		}
	}
}

