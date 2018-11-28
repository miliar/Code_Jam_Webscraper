#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

int n;
map<string,int> se;
vs iq;
int ans;
int S,Q;
char str[128];

bool swit(){
	map<string,int>::iterator it=se.begin();
	for(;it!=se.end();it++)
		if(it->second==0) return false;
	return true;
}
int main() {
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%d", &n);

	for(int test=1; test<=n; test++) {
		se.clear();
		iq.clear();
		ans=0;

		scanf("%d", &S);
		getchar();
		for(int i=0; i<S; i++) {
			cin.getline(str,sizeof str);
			se[string(str)]=0;
		}
		
		scanf("%d", &Q);
		getchar();
		int num=1;
		for(int i=0; i<Q; i++) {
			cin.getline(str,sizeof str);
			string s(str);

			if(se.find(s) == se.end()) continue;
			se[ s ]++;
			num++;
			if(num>=S && swit()){
				ans++;
				num=1;
				for(map<string,int>::iterator it=se.begin();it!=se.end();it++)
					it->second=0;
				se[ s ]++;
			}
		}
		
		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}
