#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char in[3][100]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
				"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
				"de kr kd eoya kw aej tysr re ujdr lkgc jv zq"};
char out[3][100]={"our language is impossible to understand",
				"there are twenty six factorial possibilities",
				"so it is okay if you want to just give up qz"};

char change[30];

char t[105];

int main(){

	for(int i = 0; i < 3; i ++){
		int len = strlen(in[i]);
		for(int j = 0; j < len; j ++){
			if(in[i][j] != ' '){
				change[in[i][j] - 'a'] = out[i][j];
			}
		}
	}
	
	int Case;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	scanf("%d",&Case);
	gets(t);
	
	for(int cas = 1; cas <= Case; cas ++){
		gets(t);
		printf("Case #%d: ",cas);
		int len = strlen(t);
		for(int i = 0; i < len; i ++){
			if(t[i] == ' ') {
				printf(" ");
				continue;
			}
			printf("%c",change[t[i] - 'a']);
		}
		putchar(10);
	}


	
	return 0;
}
