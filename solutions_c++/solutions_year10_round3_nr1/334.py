#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef unsigned long long ULL;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		int n;
		cin >> n;
		vector<pair<int,int> > a(n);
		for (int i = 0; i < n; i++){
			cin >> a[i].first >> a[i].second;
		}
		sort(a.begin(),a.end());
		int count = 0;
		for (int i = 0; i < n; i++){
			for (int j = i+1; j < n; j++){
				if (a[i].first <= a[j].first && a[i].second >= a[j].second)
					count++;
			}
		}
		printf("Case #%d: %d\n",test,count);
		
	}
	return 0;
}