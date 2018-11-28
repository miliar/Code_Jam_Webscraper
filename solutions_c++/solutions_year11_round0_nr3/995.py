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

int main(){
	int casos,cc,tmp;
	cin>>casos;
	
	for (cc=0;cc<casos;cc++) {
		int n,mini=1000000000,suma=0,tot=0;
		
		cin>>n;
		
		for (int i=0;i<n;i++) {
			cin>>tmp;
			mini=min(mini,tmp);
			suma^=tmp;
			tot+=tmp;
		}
		cout<<"Case #"<<cc+1<<": ";
		if (suma==0) {
			cout<<tot-mini<<endl;
		} else cout<<"NO"<<endl;
	}
	return 0;
}
