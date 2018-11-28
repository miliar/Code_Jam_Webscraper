#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <iostream>


using namespace std;

/*
double c[2000][2000];
double d[2000];

double getFact(int n)
{
	double res = 1.0;
	for (int i=1;i<=n;i++)
		res *= i;
	return res;
}

void fillC()
{
	for (int i=0;i<2000;i++)
		c[i][0] = 1;
	for (int j=1;j<2000;j++)
		c[0][j] = 0;
	for (int i=1;i<2000;i++)
		for (int j=1;j<2000;j++)
			c[i][j] = c[i-1][j] + c[i-1][j-1];
}
double getD(int n)
{
	double sign = 1.0;
	double f = getFact(n);
	double res = 0;
	for (int i=0;i<=n;i++)
	{
		if (i)
			f /= i;
		res += f * sign;
		sign = -sign;
	}
	return res;
}
void fillD()
{
	for (int i=0;i<2000;i++)
		d[i] = getD(i);
}

double ans[2000];

void fillAns()
{
	ans[0] = 0;
	for (int i=2;i<2000;i++)
	{
		double p[2000];
		double f = getFact(i);
		for (int j=0;j<=i;j++)
			p[i-j] = c[i][j] * d[i-j] / f;
		
		double m = 1.0 / (1 - p[i]);
		double res = 0;
		for (int j=0;j<i;j++)
			res += p[j] * ans[j];
		res += 1;
		res *= m;
		ans[i] = res;

	}
}*/


int main()
{
/*	fillC();
	fillD();
	fillAns();*/

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int t;
	cin>>t;
	for (int aaa=0;aaa<t;aaa++)
	{
		int n;
		cin>>n;
		vector<int> v(n);
		int cnt = 0;
		for (int i=0;i<n;i++)
		{
			cin>>v[i];
			--v[i];
			if (v[i] != i)
				++cnt;
		}
		
		cout<<"Case #"<<aaa+1<<": ";
		cout<<cnt<<".000000000"<<endl;
	}
	
    return 0;
}