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

int L,D,N;
int re;
vector<string> wrds;
char w[20][26];

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> L >> D >> N;
	string t;
	char tt;
	wrds.resize(0);
	rep(i,D) { fin >> t; wrds.push_back(t); }
    for(int j=1;j<=N;j++)
    {
		memset(w,0,sizeof(w));
		re = 0;
		fin >> t;
		int st = 0,cn = 0;
		while (cn<L) 
		{
			if (t[st]!='(') { w[cn][t[st]-'a'] = 1; cn++; st++; }
			else 
			{
				st++;
				while (t[st]!=')') { w[cn][t[st]-'a'] = 1; st++; }
				st++;
				cn++;
			}
		}
		bool fl = 0;
		rep(i,D)
		{
			fl = 1;
			rep(k,wrds[i].length())
			{
				if (w[k][wrds[i][k]-'a']==0) { fl = 0; break; }
			}
			if (fl) re++;
		}
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
