#include <iostream>
#include <fstream>
using namespace std;

bool checkC(int x, int y)
{
	int *a = new int[16];
	int *b = new int[8];
	bool flag;
	int r=0, sum1=0, sum2=0;

	while (x!=0)
	{
		a[r] = x%10;
		++r;
		x=x/10;
	}

	r=0;
	while (y!=0)
	{
		b[r] = y%10;
		++r;
		y=y/10;
	}

	for (int i=0; i<r; i++)
	{
		sum1 += a[i];
		sum2 += b[i];
	}
	if (sum1 != sum2) {delete[] a; delete[] b; return false;}

	for (int i=0; i<r/2; i++)
	{
		swap(a[i],a[r-i-1]);
		swap(b[i],b[r-i-1]);
	}

	for (int i=0; i<r; i++)
	{
		a[r+i] = a[i];
	}

	for (int i=1; i<r; i++)
	{
		flag = true;
		for (int j=0; flag && j<r; j++)
		{
			if (a[i+j] != b[j]) {flag = false;}
		}
		if (flag)
		{
			delete[] a;
			delete[] b;
			return true;
		}
	}

	delete[] a;
	delete[] b;
	return false;
}

int main()
{
    ofstream fout("output1.out");
    ifstream fin("C-small-attempt1.in");
    int A[52],B[52];
    int T;
    int count;
    fin>>T;
    for (int i=1;i<=T;i++) fin>>A[i]>>B[i];

    for (int r=1;r<=T;r++)
    {
        count = 0;
        for (int i=A[r]; i<B[r]; i++)
            for (int j=i+1; j<=B[r]; j++)
                if (checkC(i,j)) ++count;

        fout<<"Case #"<<r<<": "<<count<<"\n";
    }
    return 0;
}
