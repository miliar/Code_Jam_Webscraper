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

int T;
int A, B;

int main()
{
    fstream fin("C-large.in",ifstream::in);
    fstream fout("C-large.out",ofstream::out);
    fin >> T;
    for(int j=1;j<=T;j++)
    {
		fin >> A >> B;
		vector<int> nmbs;
		vector<int> vars;
		long long ret = 0;
		bool fl = 0;
		for(int i=A;i<=B;++i)
		{
			nmbs.resize(0);
			vars.resize(0);
			int tmp = i;
			while (tmp>0)
			{
				nmbs.push_back(tmp%10);
				tmp /= 10;
			}
			reverse(nmbs.begin(), nmbs.end());
			tmp = 0;
			for(int k=1;k<nmbs.size();++k)
			{
				tmp = 0;
				for(int s=0;s<nmbs.size();++s)
				{
					tmp = tmp*10 + nmbs[(s+k)%(nmbs.size())];
				}
				if (tmp<=i || tmp>B) continue;
				fl = 1;
				rep(s,vars.size())
					if (vars[s]==tmp)
					{
						fl = 0;
						break;
					}
				if (fl)
				{
					ret++;
					vars.push_back(tmp);
				}
			}
		}
        fout << "Case #" << j << ": " << ret << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
