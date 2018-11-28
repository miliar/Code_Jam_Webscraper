#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define debug(n) cout<<__FILE__<<","<<__LINE__<<": #"<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define tr(c,i) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

bool win(int a,int b,int p)
{
	if(a==b)
		return p!=0;
	if(a==1 || b==1)
		return p==0;
	if(max(a,b)/min(a,b)>=2)
		return p==0;
	return win(min(a,b),max(a,b)-min(a,b),!p);
}

int main()
{
	int t;
	cin>>t;
	rep(ti,t){
		int a1,a2,b1,b2;
		cin>>a1>>a2>>b1>>b2;
		int counter=0;
		repi(i,a1,a2+1){
			repi(j,b1,b2+1){
				counter+=win(i,j,0);
			}
		}
		printf("Case #%d: %d\n",ti+1,counter);
	}
	
	return 0;
}
