// 2_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
using namespace std;

#define INFILE "A-large.in"
#define OUTFILE "A-large.out"

char a[100][100];
int l[100];

int _tmain(int argc, _TCHAR* argv[])
{
	//ofstream outfile1("A-large.in");
	//outfile1<<"60"<<endl;
	//for (int i=0; i<60; i++)
	//{
	//	outfile1<<"40"<<endl;
	//	for (int j=0; j<40; j++)
	//	{
	//		for (int k=0; k<40; k++)
	//		{
	//			if (k<40-j)
	//				outfile1<<"1";
	//			else
	//				outfile1<<"0";
	//		}
	//		outfile1<<endl;
	//	}

	//}
	//outfile1.close();
		
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	int t;
	int n;
	infile>>t;
	char ct[10];
	for (int i=0; i<t; i++)
	{
		infile>>n;
		infile.getline(ct,10);
		int maxtmp=-1;
		for (int i=0; i<n; i++)
		{
			maxtmp=-1;
			for (int j=0; j<n; j++)
			{
				infile>>a[i][j];
				if (a[i][j]=='1')
					if (maxtmp<j)
						maxtmp=j;
			}
			l[i]=maxtmp;
			infile.getline(ct,10);
		}
		int count =0;
		for (int h=0; h<n; h++)
		{
			if (l[h]>h)
			{
				for (int j=h+1; j<n; j++)
					if (l[j]<=h)
					{
						for (int k=j-1; k>=h; k--)
						{
							count++;
							int tmp=l[k];
							l[k]=l[k+1];
							l[k+1]=tmp;
						}
						break;
					}
			}
			//while (l[i]>i)
			//{
			//	int tmp=l[i];
			//	l[i]=
			//}
		}

		outfile<<"Case #"<<i+1<<": "<<count<<endl;
		//for (int i=0; i<n; i++)
		//	for (int j=i; j<(n-1); j++)
		//	{
		//		if (
		//	}
	}

	
	
	infile.close();
	outfile.close();
	return 0;
}

