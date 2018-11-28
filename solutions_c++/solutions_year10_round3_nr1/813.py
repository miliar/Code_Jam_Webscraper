#include <iostream>
#include <fstream>

using namespace std;

struct Point
{
	int x,y;
};

int test,n,i,j;
int a[1010],b[1010];

int main()
{
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");
	int result,k;
	fin >> test;
	for (i=0;i<test;i++)
	{
		fin >> n;
		result=0;
		for (j=0;j<n;j++)
			fin >> a[j] >> b[j];
		for (j=0;j<n-1;j++)
			for (k=j+1;k<n;k++)
				if ((a[j]>a[k]&&b[j]<b[k])||(a[j]<a[k]&&b[j]>b[k]))
					result++;
		fout << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}