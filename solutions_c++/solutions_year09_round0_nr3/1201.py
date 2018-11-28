#include <cstdio>
#include <iostream>
#include <fstream>
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
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int n;
string wc;
string f;
long long dp[20][511];
long long re = 0;

long long go(int s1, int s2)
{
	if (s1==wc.length()) return 1;
	if (s2==f.length()) return 0;
	if (dp[s1][s2]!=-1) return dp[s1][s2];
	long long ret = 0;
	int k = s2;
	while (k<f.length())
	{
		while (k<f.length() && f[k]!=wc[s1]) k++;
		if (k<f.length()) { ret += go(s1+1,k+1); ret %= 10000; k++; }
	}
	return dp[s1][s2]=ret;
}

int main()
{
    wc = "welcome to code jam";
	fstream fin("C-large.in",ifstream::in);
    fstream fout("C-large.out",ofstream::out);
    fin >> n;
	getline(fin,f);
    for(int j=1;j<=n;j++)
    {
		getline(fin,f);
		cout << f << "\n";
		memset(dp,-1,sizeof(dp));
		re = go(0,0);
		string t;
		if (re<10) t="000";
		else if (re<100) t="00";
		else if (re<1000) t="0";
		else t="";
        fout << "Case #" << j << ": " << t << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
