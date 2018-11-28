#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int strToInt(string a)
{
	return (a[0] - '0') * 600 + (a[1] - '0') * 60 + (a[3] - '0') * 10 + (a[4] - '0');
}

void storeArray(int a[][2], int n, int w)
{
	int i, j, t;
	for (i=0;i<n-1;i++)
	{
		for (j=i+1;j<n;j++)
		{
			if (a[i][w] > a[j][w])
			{
				t = a[i][w];
				a[i][w] = a[j][w];
				a[j][w] = t;
				t = a[i][1-w];
				a[i][1-w] = a[j][1-w];
				a[j][1-w] = t;
			}
		}
	}
}

void storeAB(int a[][2], int b[][2], int na, int nb, int w)
{	
	storeArray(a, na, w);
	storeArray(b, nb, 1-w);
}

void process(int a[][2], int b[][2], int na, int nb, int *anum, int *bnum)
{
	int *fa = new int[na];
	int *fb = new int[nb];
	int i, j;
	*anum=0;
	*bnum=0;
	for (i=0;i<na;i++)
		fa[i] = 0;
	for (i=0;i<nb;i++)
		fb[i] = 0;

	storeAB(a, b, na, nb, 0);
	for (j=0;j<nb;j++)
	{
		for (i=0;i<na;i++)
		{
			if (b[j][1] <= a[i][0] && fa[i] == 0)
			{
				fa[i] = 1;
				break;
			}
		}
	}

	storeAB(a, b, na, nb, 1);
	for (i=0;i<na;i++)
	{
		for (j=0;j<nb;j++)
		{
			if (a[i][1] <= b[j][0] && fb[j] == 0)
			{
				fb[j] = 1;
				break;
			}
		}
	}	

	for (i=0;i<na;i++)
	{
		if (fa[i] == 0)
			*anum = *anum + 1;
	}
	for (j=0;j<nb;j++)
	{
		if (fb[j] == 0)
			*bnum = *bnum + 1;
	}

	delete [] fa;
	delete [] fb;
}

int main()
{
	int A[100][2] = {0};
	int B[100][2] = {0};
	int N, NA, NB, T;
	int i, j;
	int am=0, bm=0;
	string st;
	ifstream infile("B-large.in");
	ofstream ofile("B-large.out");
	infile>>N;
	for (i=0;i<N;i++)
	{
		infile>>T;
		infile>>NA>>NB;
		for (j=0;j<NA;j++)
		{
			infile>>st;
			A[j][0] = strToInt(st);
			infile>>st;
			A[j][1] = strToInt(st) + T;
		}
		for (j=0;j<NB;j++)
		{
			infile>>st;
			B[j][0] = strToInt(st);
			infile>>st;
			B[j][1] = strToInt(st) + T;
		}
		ofile<<"Case #"<<i+1<<": ";
		if (NA == 0 || NB == 0)
		{
			ofile<<NA<<" "<<NB<<endl;
			continue;
		}
		process(A, B, NA, NB, &am, &bm);
		ofile<<am<<" "<<bm<<endl;
	}
	infile.close();
	ofile.close();

	return 0;
}