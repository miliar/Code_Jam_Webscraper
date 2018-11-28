
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
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int n,p;
		n = 100;
		cin  >> p;
		int last[2] = {0,0};
		int pos[2] = {1,1};
		string temp;
		int tt;
		int cur = 0;
		for (int i=0;i<p;++i){
			cin >> temp >> tt;
			int idx;
			if (temp[0] == 'O'){
				idx = 0;
			} else {
				idx = 1;
			}
			int diff = pos[idx] - tt;
			if (diff < 0) {
				diff = -diff;
			}
			int req = max(cur, last[idx] + diff);
			cur = req + 1;
			last[idx] = cur;
			pos[idx] = tt;
		}
		cout<<"Case #"<<it<<": "<< cur <<endl;
	}
	return 0;
}
