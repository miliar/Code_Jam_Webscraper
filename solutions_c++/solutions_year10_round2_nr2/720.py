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

int count(vi a){
	int ret=0;
	for(int i=a.size()-1;i>=0;i--){
		if(a[i]==0) return ret;
		ret++;
	}
	return ret;
}
void print(vi a){
	for(int i=0;i<a.size();i++) cout<<a[i];
	cout<<endl;
}
int main(){
	int C,N,K,B,T;
	cin>>C;
	for(int kase=1;kase<=C;kase++){
		cin>>N>>K>>B>>T;
		vector<pii> chick(N);
		for(int i=0;i<N;i++){
			cin>>chick[i].first;
		}
		for(int i=0;i<N;i++){
			cin>>chick[i].second;
		}
	
		vi a(N,1);
		for(int i=0;i<N;i++){
			if(chick[i].first+chick[i].second*T<B){
				a[i]=0;
			}
		}
		
		int res=0;
		while(1){
			if(count(a)>=K){
				break;
			}
			//print(a);
			bool ok=0;
			for(int i=N-1;i>=0;i--){
				if(a[i]==0){
					for(int j=i-1;j>=0;j--){
						if(a[j]==1){
							swap(a[i],a[j]);
							res+=i-j;
							ok=1;
							break;
						}
					}
				}
				if(ok) break;
			}
			if(!ok) break;
		}
		
		if(count(a)>=K){
			printf("Case #%d: %d\n",kase,res);
		} else {
			printf("Case #%d: IMPOSSIBLE\n",kase);
		}
	}
}