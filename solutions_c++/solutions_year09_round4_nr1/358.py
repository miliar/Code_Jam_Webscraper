#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>

using namespace std;

typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

vector<int> rows;
int n;

int main(){
	int abc; cin >> abc;
	for (int zzz = 1; zzz <= abc; zzz++){
		cin >> n;
		string s;
		rows.clear();
		for (int i = 0; i < n; i++){
			cin >> s; int pos = -1;
			for (int j = 0; j < n; j++)
				if (s[j] == '1') pos = j;
			rows.push_back(pos);
		}
		int cnt = 0;
		for (int i = 0; i < n - 1; i++){
			int minpos = -1;
			for (int j = i; j < n; j++){
				if (rows[j] <= i){
					minpos = j;
					break;
				}
			}
			//cout << minpos << endl;
			for (int j = minpos-1; j >= i; j--){
				swap(rows[j],rows[j+1]);
				cnt++;
			}
		}
		
		cout << "Case #" << zzz << ": " << cnt << endl;
	}
	return 0;
}
