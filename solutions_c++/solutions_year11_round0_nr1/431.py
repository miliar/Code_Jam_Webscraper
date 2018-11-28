#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iterator>
#include <functional>
#include <utility>
#include <algorithm>
#include <numeric>
#include <typeinfo>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

typedef pair<char,int> pci;

int signum(int n)
{
	return n==0?0:n/abs(n);
}

void solve()
{
	int n; cin>>n;
	vector<pci> tests(n);
	vi blue,orange;
	rep(i,n){
		cin>>tests[i].first>>tests[i].second;
		if(tests[i].first=='B')
			blue.push_back(tests[i].second);
		else
			orange.push_back(tests[i].second);
	}
	int bp=1,op=1;
	for(int t=0,i=0,bi=0,oi=0;;t++){
		if(i==tests.size()){
			cout<<t<<endl;
			break;
		}
		else if(tests[i].first=='B' && bp==tests[i].second){
			i++;
			bi++;
			if(oi<orange.size())
				op+=signum(orange[oi]-op);
		}
		else if(tests[i].first=='O' && op==tests[i].second){
			i++;
			oi++;
			if(bi<blue.size())
				bp+=signum(blue[bi]-bp);
		}
		else{
			if(bi<blue.size())
				bp+=signum(blue[bi]-bp);
			if(oi<orange.size())
				op+=signum(orange[oi]-op);
		}
	}
}

int main()
{
	int cases; scanf("%d ",&cases);
	rep(i,cases){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
