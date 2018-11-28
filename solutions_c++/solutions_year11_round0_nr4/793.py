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
		int br = 0;
		for (int j=0;j<n;++j){
			cin >> a[j];
			if (a[j] != j + 1){
				br++;
			}
		}
		cout<<"Case #"<<it<<": ";
		printf("%.9llf\n", (ld)br);
	}
	return 0;
}
