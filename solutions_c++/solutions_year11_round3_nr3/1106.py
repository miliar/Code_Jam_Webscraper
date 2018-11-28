#include <cstring>
#include <stdio.h>
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
#include <climits>
#include <cctype>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define pb push_back

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int compFloats(const double &a, const double &b) {
  if (fabs(a - b) < eps)
    return 0;
  return a > b ? 1 : -1;
}


int main()
{
	freopen("csmall.in","r",stdin);
	freopen("csmall.out","w",stdout);
	vector<int>nums;
	nums.resize(100);
	int tc,n,l,h,dummy;
	cin>>tc;
	bool flag;
	for (int i = 1; i <= tc; ++i) {
		cout<<"Case #"<<i<<": ";
		nums.clear();
		cin>>n>>l>>h;
		for (int j = 0; j < n; ++j) {
			cin>>dummy;
			nums.push_back(dummy);
		}
		while(l<=h)
		{
			flag = true;
			for (int j = 0; j < n; ++j) {
				if(l%nums[j]!=0 && nums[j]%l!=0)
				{
					flag = false;
					break;
				}
			}
			if(flag)
			{
				break;
			}
			l++;
		}
		if(flag)
			cout<<l<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}
