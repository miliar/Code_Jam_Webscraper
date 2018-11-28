#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>

using namespace std;
typedef long long ll;
const int MAXN = 20000;
int aryd[MAXN], aryst[MAXN], aryed[MAXN];
int aryl[MAXN];

int main()
{
	int T, n, pos;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>n;
		for(int i = 0; i < n; ++i){
			cin>>aryd[i]>>aryl[i];
		}
		cin>>pos;
		aryst[0] = aryd[0];
		aryed[0] = 2 * aryd[0];
		int p = 0, ped = 1;
		bool flag = true;
		for(int i = 1; i < n; ++i){
			while(p < ped && aryed[p] < aryd[i])++p;
			if(p == ped){
				flag = false; break;
			}
			aryst[ped] = aryd[i];
			aryed[ped] = aryd[i] + min(aryl[i], aryd[i] - aryst[p]);
			if(aryed[ped] > aryed[ped - 1])++ped;
		}
		if(aryed[ped - 1] >= pos) flag = true;
		else flag = false;
		cout<<"Case #"<<tt<<": ";
		if(flag)cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}

	return 0;
}
