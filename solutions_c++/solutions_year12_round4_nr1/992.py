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
#include <cstring>

using namespace std;

#define FOR(i,a,b) for(int i = (a) ; i < (b) ; i ++)
#define forn(i,n) FOR(i, 0, n)
#define all(a) (a).begin(),(a).end()
#define sz(a) ((int)(a).size())
#define pb push_back

//string strfile = "test.txt";
//string strfile = "A-small-attempt0.in"; 
string strfile = "A-large.in";
ofstream fout;
ifstream fin;

int dist;
int n;
int di[10001];
int ii[10001];
int ret[10001];

void func()
{
	int flag = 0;
	fin>>n;

	for (int i = 0; i < n ; i++)
	{
		fin>>di[i]>>ii[i];
	}
	fin>>dist;
	memset(ret, 0, sizeof(ret));
	ret[0] = di[0];
	for (int i = 0; i < n ; i++)
	{
		if (ret[i]+di[i] >= dist)
		{
			flag = 1;
			break;
		}
		int j = i+1;
		int tmp;
		while(ret[i]+di[i] >= di[j])
		{
			tmp = di[j] - di[i];
			if (tmp > ii[j])
			{
				tmp = ii[j];
			}
			if (tmp > ret[j])
			{
				ret[j] = tmp;
			}
			j++;
		}
	}

	if (flag == 0)
	{
		fout<<" NO";
	} 
	else
	{
		fout<<" YES";
	}
	return ;
}

int main()
{
	int n;
	fin.open(strfile.c_str());
	fout.open("out.txt");
	fin>>n;
	forn(i,n)
	{
		fout<<"Case #"<<i+1<<":";

		func();

		fout<<endl;
	}
	fin.close();
	fout.close();
	return 0;

}