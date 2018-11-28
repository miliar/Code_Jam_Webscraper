#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <queue>

using namespace std;

typedef long long LL;
#define PB push_back
#define all(v) (v).begin(),(v).end()
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define pii pair<int,int>
#define INF 200000000
LL gcd(LL m,LL n){LL tmp;while(n!=0){tmp=m%n;m=n;n=tmp;}return m;}   
LL lcm(LL m,LL n){return (m*n)/gcd(m,n);}
string i2s(LL n){stringstream ss;ss<<n;return ss.str();}
LL s2i(string s){stringstream ss;ss<<s;LL n;ss>>n;return n;}


int main(){
	int T,N;
	cin>>T;
	for(int kase=1;kase<=T;kase++){
		cin>>N;
		vi a(N),b(N);
		for(int i=0;i<N;i++){
			cin>>a[i]>>b[i];
		}
		int res=0;
		for(int i=0;i<N;i++){
			for(int j=i+1;j<N;j++){
				int da=a[i]-a[j];
				int db=b[i]-b[j];
				if(da*db<0) res++;
			}
		}
		printf("Case #%d: %d\n",kase,res);
	}
}