#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> PII;
typedef unsigned long long ULL;


void solution(int tstNum){
	int p;
	int m[1 << 10] = {0};
	int pr[1 << 10] = {0};
	

	scanf("%d", &p);
	int com = (1 << p);
	for (int i = 0; i < com; i++){
		scanf("%d", &m[i]);
		m[i] = p - m[i];
	}
	for (int i = 0; i < com - 1; i++){
		scanf("%d", &pr[i]);
	}

	int ans = 0;

	for (int j = p; j >= 0; j--){
		bool alwas = false;
		for (int k = 0; ((1 << j)) * k < com; k++){
			int st = (1 << j) * k;
			int en = st + (1 << j);
			bool was = false;
			for (int s = st; s < en; s++){
				was |= m[s] > 0;
			}
			if (was){
				++ans;
				alwas = true;
				for (int s = st; s < en; s++){
					m[s]--;
				}
			}

		}
		if (!alwas){
			break;
		}
	}
	

	printf("Case #%d: %d\n", tstNum + 1, ans);
}

int main(){

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	freopen("B-small.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}