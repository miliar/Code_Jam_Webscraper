#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

#define MAX 1000005

bool primo[MAX];
vector<long long> primos;
long long n;


int main(){
	memset(primo,1,sizeof(primo));
	primo[0]=primo[1]=false;
	for (int i=2;i*i<MAX;i++) if (primo[i]) {
		primos.push_back(i);
		for (int j=2*i;j<MAX;j+=i) primo[j]=false;
	}
	int tam=primos.size();
	
	int casos,cc;
	cin>>casos;
	
	for (cc=0;cc<casos;cc++) {
		cout<<"Case #"<<cc+1<<": ";
		cin>>n;
		
		if (n==1) {
			cout<<0<<endl;
			continue;
		}
		int ans=0;
		for (int i=0;i<tam;i++) {
			long long p=primos[i];
			if (p*p>n) break;
			long long m=n/p;
			while (m>=p) {
				m/=p;
				ans++;
			}
		}
		cout<<ans+1<<endl;
	}
	return 0;
}
