#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef stringstream sst;
#define fri(a,i) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fr(i,n) for(int i=0; i<(int)(n); i++)
#define zer(a) memset((a),0,sizeof(a));
#define all(a) (a).begin(), (a).end()
#define pb push_back

int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
		int P,K,L;
	    cin>>P>>K>>L;
		vi a(L);
		for(int i=0; i<L; i++)
		  cin>>a[i];
		long long ret=0;
		sort(all(a));
		reverse(all(a));
		for (int i=0; i<L; i++){
			ret+=(i/K+1)*a[i];
		}
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
