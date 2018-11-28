#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <climits>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define clr(x) memset(x,0,sizeof(x)) 

const int N = 1000;

bool cmp(int a, int b) {
	return a > b;
}

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int cases;
	int cnt = 1;
	cin >> cases;

	vector<int>num;

	while(cases--) {
		printf("Case #%d: ", cnt++);
		string n;
		int tmp;
		num.clear();
		cin >> n;
		for(int i = n.size() - 1; i >= 0; i--)
			num.push_back(n[i] - '0');

		bool flag = false;
		for(int i = 1; i < num.size(); i++) {
			int ming = NIL, u = -1;
			for(int j = i - 1; j >= 0; j--) {
				if(num[j] > num[i]) {
					if(num[j] < ming)ming = num[j], u = j;
				}
			}
			if(u != -1) {
				swap(num[u], num[i]);
				sort(num.begin(), num.begin() + i, cmp);
				flag = true;
			}
			if(flag)break;
		}
		if(!flag) {
			int min = NIL, u;
			for(int i = 0; i < num.size(); i++) {
				if(num[i] != 0 && num[i] < min)
					min = num[i], u = i;
			}
			swap(num[u], num[num.size()-1]);
			sort(num.begin(), num.end() - 1, cmp);
			tmp = num[num.size() - 1];
			num[num.size() - 1] = 0;
			num.push_back(tmp);
		}
		for(int i = num.size() - 1; i >= 0; i--)
			printf("%d", num[i]);
		printf("\n");
	}

	return 0;
}

/*Powered By Lynn-Beta1*/