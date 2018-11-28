#define ONLINE_JUDGE
//#define GenerateTest

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <deque>
#include <cmath>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <string>
#include <stack>
#include <list>
#include <sstream>
#include <hash_set>
#include <hash_map>

//#include "BigInteger\cbignum.h"

using namespace std;
#pragma comment(linker, "/STACK:64777216")

typedef long long LL;
const int mode = 10000;
void print(int res)
{
	vector<int> r;
	for(int j = 0;j < 4;++j,res /= 10) r.push_back(res % 10);
	for(int i = r.size() - 1;i >= 0;--i)
		cout << r[i];
	cout << endl;
}
void Solve()
{
	int T;
	cin >> T;
	string str;
	char s[10000];
	gets(s);
	for(int t = 0;t < T;++t)
	{
		gets(s);
		str = s;
		string a = "welcome to code jam";
		a = " " + a;
		str = " " + str;
		vector<vector<vector<int> > > d(str.size(),vector<vector<int> >(a.size(),vector<int>(a.size(),0)));
		for(int i = 0;i < str.size();++i)
			for(int j = 0;j < a.size();++j)		
			d[i][j][0] = 1;
		for(int k = 1;k < a.size();++k)
			for(int i = 1;i < str.size();++i)
				for(int j = 1;j < a.size();++j)
				{
					if(str[i] == a[j])
						d[i][j][k] = (d[i][j][k] + d[i - 1][j - 1][k - 1]) % mode;
					d[i][j][k] = (d[i][j][k] + d[i - 1][j][k] + d[i][j - 1][k]) % mode;
				}
		cout << "Case #" << t + 1 << ": ";
		print(d[str.size() - 1][a.size() - 1][a.size() - 1]);
	}
}

int main()
{
#ifdef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);

	freopen("output.txt", "wt", stdout);
#endif

#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
//	freopen("output.txt", "wt", stdout);
	
#ifdef GenerateTest
	
	freopen("output.txt", "wt", stdout);

#endif

	clock_t start = clock();
#endif

	Solve();	

#ifndef ONLINE_JUDGE 
	clock_t end = clock();
	cout <<"\n\nTime: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
#endif
	return 0;
}