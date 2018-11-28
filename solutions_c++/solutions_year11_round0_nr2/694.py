#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

char maz[1000][1000];
int is[1000][1000];
char ch[1000];
int main() {
	int T;
	scanf("%d", &T);
	int n, m;
	int i, j, k;
	int cas = 1;
	while (T--) {
		
		for (i = 0; i < 300; i++) {
			for (j = 0; j < 300; j++)
				maz[i][j] = 0, is[i][j] = 0;
		}
		
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s", ch);
			maz[ch[0]][ch[1]] = ch[2];
			maz[ch[1]][ch[0]] = ch[2];
			is[ch[0]][ch[1]] = 2;
			is[ch[1]][ch[0]] = 2;
		}
		scanf("%d", &m);
		for (i = 0; i < m; i++) {
			scanf("%s", ch);
			if (maz[ch[0]][ch[1]] != 0) {
				is[ch[0]][ch[1]] = 3;
				is[ch[1]][ch[0]] = 3;
			} else {
				is[ch[0]][ch[1]] = 1;
				is[ch[1]][ch[0]] = 1;
			}
		}
		int len;
		scanf("%d", &len);
		scanf("%s", ch);
		vector<char> vec;
		int top = 0;
		int size;
		
		for (i = 0; i < len; i++) {
			
			if (vec.empty()) {
				vec.push_back(ch[i]);
			} else {
				top = vec.size() - 1;
				if (is[vec[top]][ch[i]] >= 2) {
					char tmp = vec[top];
					vec.pop_back();
					vec.push_back(maz[tmp][ch[i]]);
					continue;
				}

				size = vec.size();
				for (j = 0; j != size; j++)  {
					if(is[vec[j]][ch[i]] == 1 || is[vec[j]][ch[i]] == 3)
						vec.clear();
				}

				if (vec.empty()) continue;
				vec.push_back(ch[i]);
				
				
			}
		}
		if (vec.empty()) {
			printf("Case #%d: []\n", cas++);
		}else{
			printf("Case #%d: [%c", cas++, vec[0]);
			for (i = 1; i != vec.size(); i++)
				printf(", %c", vec[i]);
			puts("]");
		}
		
	}
	
	return 0;
}
