#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 110

int C;
int D;
int N;
map<char, int> m;

struct COM{
	char a, b, c;
}c[MAXN];
struct OPP{
	char a, b;
}d[MAXN];

char canCombine(char a, char b){
	for(int i = 0;i < C; i++){
		//cout<<a<<" "<<b<<endl;
		if( (c[i].a == a && c[i].b == b) ||
			(c[i].a == b && c[i].b == a)){
			return c[i].c;
		}
	}
	return 0;
}

bool canClear(){
	for(int i = 0;i < D; i++){
		if( m[d[i].a] > 0 &&
			m[d[i].b] > 0 ){
			return true;
		}
	}
	return false;
}

int main()
{
	char str[MAXN];
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		scanf("%d", &C);
		for(int i = 0;i < C; i++){
			scanf("%s", str);
			c[i].a = str[0];
			c[i].b = str[1];
			c[i].c = str[2];
		}
		scanf("%d", &D);
		for(int i = 0;i < D; i++){
			scanf("%s", str);
			d[i].a = str[0];
			d[i].b = str[1];
		}

		memset(str, 0, sizeof(str));
		scanf("%d", &N);
		scanf("%s", str);

		vector<char> list;
		list.clear();
		m.clear();
		int s;
		char result;
		for(int i = 0;i < N; i++){
			list.push_back(str[i]);
			m[str[i]]++;
			s = (int)list.size();
			if(s > 1){
				result = canCombine(list[s - 1], list[s - 2]);
				if(result != 0){
					m[list[s - 1]]--;
					m[list[s - 2]]--;
					list.pop_back();
					list.pop_back();
					list.push_back(result);
				}else if(canClear()){
					list.clear();
					m.clear();
				}
			}
		}

		printf("Case #%d: [", casenum++);
		for(int i = 0;i < (int)list.size(); i++){
			if(i)printf(", ");
			printf("%c", list[i]);
		}
		printf("]\n");
	}
	return 0;
}

