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
long long L, t, N, C;
vector<long long> dist;
vector<long long> dstcnt;
vector<long long> dstcnt2;
vector<long long> dsts;
//vector<int> bst;

bool cmp(pair<long long, long long> a, pair<long long, long long> b)
{
	return (a.first>b.first);
}

int main()
{
    fstream fin("B-large.in",ifstream::in);
    fstream fout("B-large.out",ofstream::out);
    fin >> T;
    for(int tcase=1;tcase<=T;tcase++)
    {
        cout << tcase << "\n";
		dist.clear();
		//bst.clear();
		fin >> L >> t >> N >> C;
		dist.resize(N);
		dstcnt.resize(C);
		dsts.resize(C);
		long long tmpd;
		rep(i, C)
		{
			fin >> tmpd;
			dsts[i] = tmpd;
			dstcnt[i] = 0;
			for(int k=0;;k++)
			{
				if (k*C+i>=N) break;
				dist[k*C+i] = tmpd;
				dstcnt[i]++;
			}
		}
		dstcnt2 = dstcnt;
		long long re = 0;
		long long st = 0;
		long long tre = 0;
		rep(i, N)
		{
			if (tre<=t && tre+2*dist[i]>t)
			{
				st = i;
				break;
			}
			tre += 2*dist[i];
		}
		if (L==0)
		{
			re  = 0;
			rep(i, N) re += dist[i]*2;
		}
		else
		{
			long long trest = 0;
			re = 1000000000000000000ll;
			tre = 0;
			rep(i, st) trest += 2*dist[i];
			for(int i=st;i<=st+C && i<N;++i)
			{
				tre = trest;
				for(int j=st;j<i;++j)
					tre += 2*dist[j];
				dstcnt2 = dstcnt;
				rep(k, dstcnt2.size())
				{
					dstcnt2[k] -= i / C;
					//cout << i%C << "\n";
					if ((i%C)>=k) dstcnt2[k]--;
				}
				vector< pair<long long, long long> > dstsr(0);
				rep(k, dstcnt2.size()) dstsr.push_back(make_pair(dsts[k], dstcnt2[k]));
				sort(dstsr.begin(), dstsr.end(), cmp);
				if (t>tre) tre += (t-tre) + (dist[i] - (t-tre)/2);
				else tre += dist[i];
				long long prc = L-1;
				while (1)
				{
					int sti = 0;
					while (sti<dstsr.size() && dstsr[sti].second==0) sti++;
					if (sti==dstsr.size()) break;
					if (prc>=dstsr[sti].second)
					{
						tre += dstsr[sti].second * dstsr[sti].first;
						prc -= dstsr[sti].second;
						dstsr[sti].second = 0;
					}
					else
					{
						tre += prc * dstsr[sti].first;
						tre += (dstsr[sti].second-prc) * 2 * dstsr[sti].first;
						prc = 0;
						dstsr[sti].second = 0;
					}
				}
				re = min(re, tre);
			}
		}
		cout << re << "\n";
		fout << "Case #" << tcase << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
