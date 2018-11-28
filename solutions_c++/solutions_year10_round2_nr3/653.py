//////////////////////////
// Author:
// Date:
// Title:
// Function:
//////////////////////////
#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<conio.h>
using namespace std;

#define xin fin
#define xout fout
#define f(i,a,b) for (i=a;i<=b;i++)

int c(int a, int b)
{
	if (a < b)
	{
		return 0;
	}
	if (a < b)
	{
		swap(a,b);
	}
	if ((a == b) || (b == 0))
	{
		return 1;
	}
	return c(a-1,b-1)+c(a-1,b);
}
int main()
{
	const int max = 100003;
	ifstream fin("c.in");
	ofstream fout("c.out");
	int t,n;
	register int i,k,j,z;
	int f[501][500];
	int m;
	memset(f,0,sizeof(f));
	f[2][1] = 1;
	f[2][0] = 1;
	f(i,3,30)
	{
		f[i][1] = 1;
		f(k,2,i-1)
		{
			f(j,1,k-1)
			{
				m = f[k][j] * c(i-k-1,k-j-1);
				//if ((m > max) || (max < 0))
					//cout << i << ',' << k << ' ' << j << ' '<< m << endl;
				if (m > max)
				{
					m %= max;
				}
				f[i][k] += m;
				if (f[i][k] > max)
					f[i][k] -= max;
			}
		}
		f[i][0] = 0;
		f(k,1,i-1)
		{
			f[i][0] += f[i][k];
			if (f[i][0] > max)
				f[i][0] -= max;
		}
	}
	/*
	cout << "=============" << endl;
	while (getch() == '\0');
	cout << "vvvvvvvvvvvvvv" << endl;*/
	xin >> t;
	f(z,1,t)
	{
		xin >> n;
		xout << "Case #" << z << ": " << f[n][0] << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
