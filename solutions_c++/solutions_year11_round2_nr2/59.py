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
bool can(const vector<int>& a, int d, ld time){
	ld st = -1e50;
	int n = a.size();
	for (int i=0;i<n;++i){
		st = max(st, (ld)(a[i]) - time);
		if (st > (ld)(a[i]) + time + epsylon) {
			return false;
		}
		st += d;
	}
	return true;
}
int main()
{
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int n,d;
		cin >> n >>d;
		vector<int> a;
		for (int i=0;i<n;++i){
			int u,v;
			cin >> u >> v;
			for (int j=0;j<v;++j){
				a.push_back(u + 100000);
			}
		}
		ld beg = 0.0;
		ld end = 1e+15;
		for (int i=0;i<400;++i){
			ld mid = (end + beg)*0.5;
			if (can(a,d,mid)){
				end = mid;
			}else{
				beg = mid;
			}
		}
		cout<<"Case #"<<it<<": ";
		printf("%.1llf\n",beg);

	}
	return 0;
}
