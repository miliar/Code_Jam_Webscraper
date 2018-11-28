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
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		int res = 0;
		for (int i=0;i<n;++i){
			cin >> a[i];
			res ^= a[i];
		}
		if (res != 0){
			cout<<"Case #"<<it<<": " << "NO" <<endl;
		} else {
			int m = *min_element(all(a));
			int s = accumulate(all(a), 0);
			cout<<"Case #"<<it<<": "<< s - m<<endl;
		}
	}
	return 0;
}
