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
#include <cstdlib>
#include <ctime>
 

using namespace std;

int main() {
	int t,n,k;
	string ans;
	cin >> t;
	for(int cases=1; cases <= t; cases++) {
		cin>>n>>k;
		int states = 1<<n;
		k %= states;
		ans = ((states == k+1) ? "ON" : "OFF");
		cout<<"Case #"<<cases<<": "<<ans<<endl;
	}	
	return 0;
}
