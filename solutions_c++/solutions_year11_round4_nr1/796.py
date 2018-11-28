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
int X, S, R, t, N;
int B, E, W;
vector<int> vel;
vector< pair<double, int> > diff;

bool cmp(pair<double, int> a, pair<double, int> b)
{
	return a.first < b.first;
}

int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> T;
    for(int tcase=1;tcase<=T;tcase++)
    {
		double re = 0.;
		fin >> X >> S >> R >> t >> N;
		vel.resize(X);
		rep(i, X) vel[i] = 0;
		diff.resize(X);
		rep(i, N)
		{
			fin >> B >> E >> W;
			for(int j=B;j<E;++j)
				vel[j] = W;
		}
		rep(i, X) diff[i] = make_pair(1./(S+vel[i]) - 1./(R+vel[i]), i);
		sort(diff.begin(), diff.end());
		reverse(diff.begin(), diff.end());
		//rep(i, X) re += 1./(S+vel[i]);
		
		double tt = t;
		rep(i, X)
		{
			//if (i<X) re -= diff[i];
			if (tt>1./(R+vel[diff[i].second]))
			{
				re += 1./(R+vel[diff[i].second]);
				tt -= 1./(R+vel[diff[i].second]);
			}
			else if (tt>1e-11)
			{
				double tdist = (R+vel[diff[i].second])*tt;
				re += tdist/(R+vel[diff[i].second]) + (1.-tdist)/(S+vel[diff[i].second]);
				tt = 0.;
			}
			else
			{
				re += 1./(S+vel[diff[i].second]);
			}
		}
		fout.precision(20);
		fout << "Case #" << tcase << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << "\n";
    system("PAUSE");
    return 0;
}
