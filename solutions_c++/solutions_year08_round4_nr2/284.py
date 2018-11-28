//some code in here may be from Abdenego's library
//at http://shygypsy.com/tools/
//(you will see a comment near the relevant code if that's
//the case!)
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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#define V(type) vector< type >
#define Vall(t) t.begin(),t.end()
#define llint long long
#define forV(var, vec) for(int var=0;var<vec.size();var++)
#define for0(var, lim) for(int var=0;var<lim;var++)
#define for1(var,lim) for(int var=1;var<lim;var++)
#define btw(x,a,b) ((x) >= (a) && (x) <= (b))
#define permute(vec) next_permutation( vec.begin(),vec.end())
#define MP(a,b) make_pair((a),(b))
#define dpExp MP(a,b)

using namespace std;


string format(const vector<pair<int,int> > &v)
{
	ostringstream oss;oss.clear();
	forV(i,v)
	{
		oss << v[i].first << " " << v[i].second << " ";
	}
	string s = oss.str();
	return s.substr(0,s.size()-1);
}

int main(void)
{
	int CASES;
	cin >> CASES;
	for(int _cn = 1;_cn <= CASES;++_cn)
	{
		long long N,M,A;
		cin >> N >> M >> A;
		bool found = false;
		vector<pair<int,int> > x(3,MP(0,0));
		for(llint i=0;i<=N && !found;++i)
		{
			for(llint j=0;j<=M  && !found;++j)
			{
				for(llint k=0;k<=N  && !found;++k)
				{
					for(llint el=0;el<=M  && !found;++el)
					{
						if(i*el - j*k == A || i*el - k*j == -A)
						{
							x[1] = MP(i,j);
							x[2] = MP(k,el);

							found = true;
						}


					}
				}
			}
		}
		if(!found)
		{
		cout << "Case #" << _cn << ": IMPOSSIBLE" <<endl;
		cerr << "Case #" << _cn << ": IMPOSSIBLE" <<endl;

		}
		else
		{
		cout << "Case #" << _cn << ": " << format(x) << endl;
		cerr << "Case #" << _cn << ": " << format(x) << endl;
		}
	}
	return 0;
}

