#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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

string inName;
string outName;

#define cin fin
#define cout fout

char buff[501];
int m[500][19];
char* wtcj = "welcome to code jam";

int main()
{
//	inName = "C-small.in";
	inName = "C-large.in";
//	outName = "C-small.out";
	outName = "C-large.out";

	int tc;
	ifstream fin(inName.c_str());
	ofstream fout(outName.c_str());
	cin>>tc;
	cin.getline(buff, 501);
	for(int Case = 0; Case < tc; Case++)
	{
		cin.getline(buff, 501);
		int n = strlen(buff);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < 19; j++)
				m[i][j] = 0;

		if(buff[0] == 'w')
			m[0][0] = 1;
		for(int i = 1; i < n; i++)
		{
			m[i][0] = m[i-1][0];
			if(buff[i] == 'w')
				m[i][0] = m[i-1][0]+1;
			for(int j = 1; j < 19; j++)
			{
				m[i][j] = m[i-1][j];
				if(buff[i] == wtcj[j])
					m[i][j] = (m[i][j] + m[i-1][j-1])%10000;
			}
		}
		cout<<"Case #"<<Case+1<<": ";
		if(m[n-1][18] < 1000)
			cout<< '0';
		if(m[n-1][18] < 100)
			cout<< '0';
		if(m[n-1][18] < 10)
			cout<< '0';
		cout<< m[n-1][18] << endl;
	}
	fout.close();
	fin.close();

	return 0;
}