#include <iostream>
#include <fstream>

using namespace std;

int gcd(int a,int b)
{
	if (b==0)
		return a;
	else
		return gcd(b,a%b);
}

bool check(int a,int b)
{
	if (b==1&&a==1)
		return false;
	if (b==0||b==1)
		return true;
	//if (b==1)
	//	return true;
	if (!check(b,a%b))
		return true;
	if (a>=b*2)
		return true;
	return false;
    /*if (b==0||b==1)
        return true;
    if (check(b,a%b)==false)
        return true;
    if (a>b*2)
        return true;
    return false;*/
}

int main()
{
	ofstream fout("C-small.out");
	ifstream fin("C-small.in");
	int test,i,j,k,d,b1,b2,a1,a2,n,m;
	fin >> test;
	for (i=0;i<test;i++)
	{
		fin >> a1 >> a2 >> b1 >> b2;
		d=0;
		for (j=a1;j<=a2;j++)
			for (k=b1;k<=b2;k++)
			{
				n=j;
				m=k;
				if (n<m)
					swap(n,m);
				if (check(n,m))
					d++;
			}
		fout << "Case #" << i+1 << ": " << d << endl;
	}
	return 0;
}