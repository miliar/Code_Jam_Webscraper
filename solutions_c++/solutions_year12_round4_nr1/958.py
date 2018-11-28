#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define bits(x) __builtin_popcount(x)
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

int pos[10100], len[10100];
int maxD[10100];

int main() {
	int n,N,D;
	cin>>n;
	for (int caso = 1; caso <= n; caso++) {
		cin>>N;
		
		for (int i=0;i<N;i++) {
			cin>>pos[i]>>len[i];
		}
		cin>>D;
		
		bool reach=false;
		memset(maxD, 0, sizeof(maxD));
		maxD[0]=pos[0];
		for (int i=0;i<N;i++) {
			if (pos[i]+maxD[i] >= D) {
				reach=true;
				break;
			}
			for (int j=i+1;j<N && pos[i]+maxD[i]>=pos[j];j++) {
				maxD[j]=max(maxD[j], min(pos[j]-pos[i], len[j]));
			}
		}
		
		cout<<"Case #"<<caso<<": ";
		if (reach) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}
