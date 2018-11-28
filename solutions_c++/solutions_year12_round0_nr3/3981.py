#include<iostream>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<set>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert> 
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;


#define debug(x) cout << #x << " = " << x << "\n";
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)
#define mem(a, n) memset(a, n, sizeof(a))
typedef vector<int> VI;

int getLength(int n) {
	int len = 0;
	while(n) {
		n /= 10;
		len++;
	}
	return len;
}
int power(int n) {
	if(n==0)
		return 1;
	int x = power(n / 2);
	x *= x;
	if(n & 1)
		x *= 10;
	return x;
		
}
int main() {
	int t;
	scanf("%d", &t);
	int n, m;
	for(int k=1;k<=t;k++) {
		long long int cnt = 0;
		scanf("%d %d", &n, &m);
		for(int i=n;i<=m;i++) {
			int len = getLength(i);
			int mod = 10;
			int cur = i;
			do {
				cur = (cur % 10) * power(len - 1) + cur / 10;
				cnt += cur > i && cur <=m; 	 
			} while(cur!=i);
		}	
		

		printf("Case #%d: %lld\n", k, cnt);
	}
}
