#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define Fe(it,v)for(__typeof__((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(x) (x).begin(),(x).end()
using namespace std;
int main(){
	int test=1;
	int N;
	cin>>N;
	long long a[1000];
	long long b[1000];
	while(N--){
		long long ret=0;
		int n;
		cin>>n;
		F(i,0,n){
			cin>>a[i];
		}
		F(i,0,n){
			cin>>b[i];
		}
		sort(a,a+n,greater<int>());
		sort(b,b+n);
		F(i,0,n)ret+=a[i]*b[i];
		cout<<"Case #"<<test++<<": "<<ret<<endl;
	}
}
