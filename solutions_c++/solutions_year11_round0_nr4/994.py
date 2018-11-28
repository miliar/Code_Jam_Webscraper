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
	int casos,cc,n,tmp;
	cin>>casos;
	
	for (cc=0;cc<casos;cc++) {
		cin>>n;
		int dif=0;
		
		for (int i=1;i<=n;i++) {
			cin>>tmp;
			if (tmp!=i) dif++;
		}
		
		cout<<"Case #"<<cc+1<<": "<<dif<<endl;
	}
	return 0;
}
