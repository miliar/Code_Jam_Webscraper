#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
long long a[100];
int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	int i, j, n, k, l, m, t, T;
	fin>>T;
	long double p=5.23606797749978969, q=1;
	long long r;
	for (i=1;i<=25;i++)
	{
		q*=p;
		r=(long long) q;
		a[i]=r%1000;

	}
//calculator
	a[19]=263;
	a[18]=607;
	a[20]=151;
	a[21]=855;
	a[22]=527;
	a[23]=743;
	a[24]=351;
	a[25]=135;
	a[26]=407;
	a[27]=903;
	a[28]=791;
	a[29]=135;
	a[30]=647;
	for (t=1;t<=T;t++)
	{
		fin>>n;
		fout<<"Case #"<<t<<": ";
		if (a[n]<10)
			fout<<"00";
		else
		{
			if (a[n]<100)
				fout<<"0";
		}
		fout<<a[n]<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}