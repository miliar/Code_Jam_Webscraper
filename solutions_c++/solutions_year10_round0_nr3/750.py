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
long long R, k, N;
long long g[2000];
vector<long long> que;
vector<int> ind;
long long period;
long long stp;
long long re;

int main()
{
    fstream fin("C-large.in",ifstream::in);
    fstream fout("C-large.out",ofstream::out);
    fin >> T;
	long long tmp, tmp3;
	int tmp2;
    for(int j=1;j<=T;j++)
    {
		fin >> R >> k >> N;
		que.resize(0);
		ind.resize(0);
		re = 0;
		rep(i, N)
		{
			fin >> g[i];
			ind.push_back(i);
		}
		{
			que.push_back(ind[0]);
			bool fl = 1;
			while(fl)
			{
				tmp = 0;
				int cc = 0;
				while (tmp + g[ind[0]]<=k && cc<N)
				{
					tmp += g[ind[0]];
					tmp2 = ind[0];
					ind.erase(ind.begin());
					ind.push_back(tmp2);
					cc++;
				}
				//re += tmp;
				rep(i,que.size())
				{
					if (que[i]==ind[0])
					{
						period = que.size() - i;
						fl = 0;
						stp = i;
						break;
					}
				}
				que.push_back(ind[0]);
			}
			rep(i,N) ind[i] = i;
			if (R<stp)
			{
				rep(i,R)
				{
					tmp = 0;
					int cc = 0;
					while (tmp + g[ind[0]]<=k && cc<N)
					{
						tmp += g[ind[0]];
						tmp2 = ind[0];
						ind.erase(ind.begin());
						ind.push_back(tmp2);
						cc++;
					}
					re += tmp;
				}
				fout << "Case #" << j << ": " << re << "\n";
				continue;
			}

			rep(i, stp)
			{
				tmp = 0;
				int cc = 0;
				while (tmp + g[ind[0]]<=k && cc<N)
				{
					tmp += g[ind[0]];
					tmp2 = ind[0];
					ind.erase(ind.begin());
					ind.push_back(tmp2);
					cc++;
				}
				re += tmp;
			}
			tmp3 = 0;
			rep(i, period)
			{
				tmp = 0;
				int cc = 0;
				while (tmp + g[ind[0]]<=k && cc<N)
				{
					tmp += g[ind[0]];
					tmp2 = ind[0];
					ind.erase(ind.begin());
					ind.push_back(tmp2);
					cc++;
				}
				tmp3 += tmp;
			}
			if (R-stp>=period) re += ((R-stp)/period)*tmp3;
			rep(i, (R-stp)%period)
			{
				tmp = 0;
				int cc = 0;
				while (tmp + g[ind[0]]<=k && cc<N)
				{
					tmp += g[ind[0]];
					tmp2 = ind[0];
					ind.erase(ind.begin());
					ind.push_back(tmp2);
					cc++;
				}
				re += tmp;
			}
		}
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
