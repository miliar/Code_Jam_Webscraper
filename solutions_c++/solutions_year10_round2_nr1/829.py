#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

char a[100001], ss[100001], temp[100002];
int m, t, n, cnt;
string s[12000];

int main(){
	scanf("%d", &t);
	for (int tt = 1; tt<=t; tt++){
		cnt = 0;
		scanf("%d%d", &n, &m);
		for (int i=0; i<n; i++){
			cin >> s[i];
		}
		for (int j=0; j<m; j++){
			scanf("%s", temp);
			s[n+cnt] = string(temp);
			cnt++;
		for (int i=1; temp[i]; ++i)
			if (temp[i]=='/'){
				temp[i] = 0;
				s[n+cnt] = string(temp);
				temp[i] = '/';
				cnt++;
			}
		}
		sort(s, s+n+cnt);
		printf("Case #%d: %d\n", tt, unique(s, s+n+cnt) - s - n);
	}
	return 0;
}
