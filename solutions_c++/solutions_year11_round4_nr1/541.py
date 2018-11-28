#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
ld x,s,r,t;
int n;
ld c;
ld res;
void modify(ld dist, ld w) {
	if (t < epsylon){
		res += (dist)/(w+s);
	} else if (t*(r+w) < dist + epsylon) {
		res += t + (dist - t*(r+w))/(w+s);
		t = 0;
	} else {
		ld tm =  dist/(w+r);
		t -= dist/(w+r);
		res += tm;
	}
	c += dist;
}
int main()
{
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		cin >> x >> s >> r >>t >> n;
		c = 0;
		res = 0;
		vector<pair<ld, ld > > bs;
		bs.push_back(mpair(0,0));
		for (int i=0;i<n;++i){
			ld b,e,w;
			cin >> b >> e >> w;
			if (c < b - epsylon) {
				bs[0].second+= b-c;
			}
			bs.push_back(mpair(w,e-b));
			c = e;
		}
		bs[0].second += x-c;
		sort(all(bs));
		for (int i=0;i<bs.size();++i){
			modify(bs[i].second, bs[i].first);
		}
		cout<<"Case #"<<it<<": ";
		printf("%.9llf\n",res);
	}
	return 0;
}
