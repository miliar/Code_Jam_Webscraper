// BEGIN CUT HERE

// END CUT HERE
#line 5 "TheJackpotDivOne.cpp"
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

char s[60][60];

int main(){
	int i, j, k, m, n;
	int cas, ri, flag;
	freopen("A-large (2).in", "r", stdin);
	freopen("w.txt", "w", stdout);
	scanf("%d", &cas);
	for(int ri = 1; ri <= cas; ri++){
		printf("Case #%d:\n", ri);
		scanf("%d%d", &n, &m);
		memset(s, 0, sizeof(s));
		for(i = 0; i < n; i++)
			scanf("%s", s[i]);
		while(1){
			flag = 0;
			for(i = 0; i < n; i++)
				for(j = 0; j < m; j++)
					if(s[i][j] == '#'){
						if(s[i+1][j] != '#'||s[i][j+1] != '#'||s[i+1][j+1] != '#')
							flag = 2;
						else{
							flag = 1;
							s[i+1][j] = s[i][j+1] = '\\';
							s[i][j] = s[i+1][j+1] = '/';
						}
						j = m;
						i = n;
					}
			//printf("%d %d\n",i, flag);
			if(flag != 1) break;
		}
		if(flag == 2)
			puts("Impossible");
		else
			for(i = 0; i < n; i++) puts(s[i]);
	}
}
