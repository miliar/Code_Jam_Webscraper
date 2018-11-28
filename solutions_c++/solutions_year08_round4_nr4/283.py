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

int rle(const string &s)
{
	char cur = s[0];
	int out = 1;
	for(int i=1;i<s.size();++i)
	{
		if(cur != s[i]){cur = s[i];++out;}
	}
	return out;
}


int main(void)
{
	int CASES;
	cin >> CASES;
	for(int _cn = 1;_cn <= CASES;++_cn)
	{
		int k;string S;
		cin >> k >> S;
		int out = 1000000;
		vector<int> v(k,0);
		for(int i=0;i<k;++i)
		{v[i] = i;}
		sort(Vall(v));
		do
		{
			string q = S;
			for(int i=0;i<S.size()/k;++i)
			{
				for(int j=0;j<k;++j)
				{
					q[k*i + j] = S[k*i + v[j]];
				}
			}
			out <?= rle(q);
		}
		while(next_permutation(Vall(v)));

		cout << "Case #" << _cn << ": " << out << endl;
		cerr << "Case #" << _cn << ": " << out << endl;
	}
	return 0;
}

