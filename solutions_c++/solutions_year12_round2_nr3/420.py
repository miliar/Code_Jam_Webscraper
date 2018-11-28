#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define debug 1
#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define Rep(it, a) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define pb push_back
#define mp make_pair
#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define cp(a) cerr << "(" << #a << "," << a << ") "
#define cen cerr << endl

typedef long long lint;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int inf = 0x7fffffff;

const int Size = 1000 * 1000 + 1;
char buffer[Size];

const int size = 20 * 1000 * 100;
vi sum[size];
int ar[20];


int solution(int nTest) {
	printf("Case #%d:\n", nTest + 1);
	int n;
	scanf("%d", &n);
	For(i, 0, n) {
		scanf("%d", &ar[i]);
	}
	For(i, 0, size) {
		sum[i].clear();
	}
	int flag = 0;
	For(i, 0, (1 << n)) {
		if(flag) {
			break;
		}
		int s = 0;
		For(j, 0, n) {
			if((1 << j) & i) {
				s += ar[j];
			}
		}
		For(k, 0, sz(sum[s])) {
			if(flag) {
				break;
			}
			if(sum[s][k] & i) {
				continue;
			}
			else {
				flag = 1;
				For(j, 0, n) {
					if((1 << j) & i) {
						printf("%d ", ar[j]);
					}
				}
				printf("\n");
				For(j, 0, n) {
					if((1 << j) & sum[s][k]) {
						printf("%d ", ar[j]);
					}
				}
				printf("\n");
			}
		}
		if(flag == 0) {
			sum[s].pb(i);
		}
	}


	if(flag == 0) {
		puts("Impossible");
	}



	return 1;
}

int main() {
	if(debug) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}


	int i = 0, n = 99999;
	scanf("%d", &n);
	while(i < n && solution(i)) {
		i++;
	}

	return 0;
}
