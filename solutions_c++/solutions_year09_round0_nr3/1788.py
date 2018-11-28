#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

string a="welcome to code jam";
string s;

int v[30][510];
int calc()
{
	int n=a.size();
	int m=s.size();
	int i, j;
	memset(v,0,sizeof(v));
	for (j=0;j<m;j++)
	{
		if (a[0]==s[j])
			v[0][j]=1;
		for (i=1;i<n;i++)
		{
			if (a[i]==s[j])
			{
				for (int k=0;k<j;k++)
					v[i][j]=(v[i][j]+v[i-1][k])%1000;
			}
		}
	}
	int res=0;
	for (i=0;i<m;i++)
		res=(res+v[n-1][i])%1000;
	return res;
}


int main()
{
	int i, j, k, n, m, l, d, res;
	char ch[10000];
	ifstream fin("c.in");
	ofstream fout("c.out");
	fin>>n;
	fin.getline(ch,600);
	for (i=0;i<n;i++)
	{
		fin.getline(ch,600);
		s=ch;
		m=calc();
		string s="0000";
		s[3]=m%10+'0';
		s[2]=(m%100)/10+'0';
		s[1]=(m%1000)/100+'0';
		s[0]=m/1000+'0';
		fout<<"Case #"<<i+1<<": "<<s<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
