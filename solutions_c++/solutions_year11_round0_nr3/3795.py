#include <iostream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define SZ(v) (int)v.size()

#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;

const int oo = (int) 1e9;
const double PI = 3.141592653589793;
const double eps = 1e-11;

int  N;
vector<int>v;

int calc(int ind, int l, int r, int ll, int rr)
{

	if(ind >= N)
		{
//		/if(l == r && ll != 0 && rr != 0)
		//cout <<"ll & rr -> "<< ll <<" " << rr <<endl << "l & r =>" <<l << " "<<r<<endl;
		return (l == r && ll != 0 && rr != 0 ? max(ll,rr) : 0);

		}

//	pii ret;
//	if((ret = calc(ind + 1, l ^ v[ind], r)).first != -1)
//		{
//		cout<<"first " <<ret. first << " " << ret.second <<endl;
//			return mp(ret.first + v[ind],ret.second);
//		}
//
//	if((ret = calc(ind + 1, l, r ^ v[ind])).first != -1);
//	{
//		cout<<"sec " <<ret. first << " " << ret.second <<endl;
//		return mp( ret.first , ret.second + v[ind]);
//
//	}
		return max(calc(ind + 1, l ^ v[ind], r,ll + v[ind],rr),calc(ind + 1, l, r ^ v[ind],ll,rr + v[ind]));
	//return (ret != -1 ? ret + v[ind] : -1);
		//return mp(-1,-1);
}
#define _small_
//#define _large_
int main() {

#ifdef _small_
	freopen("C-small.in", "rt", stdin);
#endif
#ifdef _large_
	freopen("C-large.in", "rt", stdin);
#endif
	freopen("C.out", "wt", stdout);

	//-----------------------


	int T;
	cin >> T;

	for (int tt = 1; tt <= T; ++tt) {
		cin>>N;
		v.resize(N);
		for (int i = 0; i < N; ++i) {
			cin >> v[i];
		}
		sort(rall(v));

		int res = calc(0,0,0,0,0);
		if(res)
			printf ("Case #%d: %d\n",tt,res);
		else
			printf ("Case #%d: NO\n",tt);
	}

	return 0;
}
