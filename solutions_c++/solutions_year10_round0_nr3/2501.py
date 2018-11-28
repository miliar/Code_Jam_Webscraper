#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

const double pi = acos(-1.0);

int main(){
	freopen("C-small-attempt0.in" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);

	int t;
	cin>>t;
	for(int c = 1 ; c <= t ; c++){
		int r,cap,n;
		cin>>r>>cap>>n;
		list<int> q;
		while(n--){
			int g;
			cin>>g;
			q.push_back(g);
		}
		int ans = 0;
		while(r--){
			int k = cap;
			int sz = q.size();
			while( (q.front()) <= k && sz--){
				int f = q.front();
				ans += f;
				k -= f;
				q.pop_front();
				q.push_back(f);
			}
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}