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

#define MAX 202
#define NINF -2000000000000000LL

int C;
long long D;
int cant[MAX];
long long pos[MAX];

bool can(long long m) {
	long long p=NINF;
	for (int i=0;i<C;i++) {
		for (int j=0;j<cant[i];j++) {
			if (pos[i] >= p + D) {
				long long dif = min(pos[i]-(p+D), m);
				p = pos[i]-dif;
			} else {
				long long dif = p+D-pos[i];
				if (dif>m) return false;
				p = pos[i]+dif;
			}
		}
	}
	return true;
}

int main(){
	int casos,cc;
	cin>>casos;
	
	for (cc=0;cc<casos;cc++) {
		cout<<"Case #"<<cc+1<<": ";
		cin>>C>>D; D*=2;
		
		for (int i=0;i<C;i++) {
			cin>>pos[i]>>cant[i];
			pos[i]*=2;
		}
		long long le=0,ri=5000000000000LL;
		
		if (can(le)) {
			cout<<le/2<<endl;
			continue;
		}
		while (le+1<ri) {
			long long med=(le+ri)/2;
			
			if (can(med)) ri=med;
			else le=med;
		}
		cout<<ri/2;
		if (ri%2==1) cout<<".5";
		cout<<endl;
	}
	return 0;
}
