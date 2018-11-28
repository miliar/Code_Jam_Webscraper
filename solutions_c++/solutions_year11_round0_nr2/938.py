//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define PB push_back
#define SZ(x) ((int)x.size())

using namespace std;

vector<string> cmb, dst;

int main(){
	int t;
	scanf("%d", &t);
	FOR(testCase, t){
		cmb.clear();
		dst.clear();
		int c, d, n;
		scanf("%d", &c);
		FOR(i, c){
			string str;
			cin>>str;
			if(str[0] > str[1])
				swap(str[0], str[1]);
			cmb.PB(str);
		}
		scanf("%d", &d);
		FOR(i, d){
			string str;
			cin>>str;
			if(str[0] > str[1])
				swap(str[0], str[1]);
			dst.PB(str);
		}
		vector<char> list;
		scanf("%d", &n);
		FOR(i, n){
			char c;
			scanf(" %c", &c);
			list.PB(c);
			bool replaced = false;
			while(SZ(list) >= 2){
				char a = list.back();
				char b = list[SZ(list) - 2];
				if(a > b)
					swap(a, b);
				char next = -1;
				FOR(i, SZ(cmb))
					if(a == cmb[i][0] && b == cmb[i][1])
						next = cmb[i][2];
				if(next != -1){
					list.pop_back();
					list.pop_back();
					list.PB(next);
					replaced = true;
				}else	break;
			}
			if(!replaced)
				FOR(i, SZ(dst))
					FOR(j, SZ(list))
						if((dst[i][0] == list[j] && dst[i][1] == list.back()) || (dst[i][1] == list[j] && dst[i][0] == list.back())){
							list.clear();
							break;
						}
		}
		printf("Case #%d: [", testCase + 1);
		FOR(i, SZ(list)){
			printf("%c", list[i]);
			if(i + 1 != SZ(list))
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}

