#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <stdlib.h>

using namespace std;

int main(){ 
	freopen("a-small.in" , "rt" , stdin);
	freopen("a-small.out" , "wt" , stdout);
	//freopen("a-large.in" , "rt" , stdin);
	//freopen("a-large.out" , "wt" , stdout);

	char str[100];
	int tst , i , j , ln , st[100] , id[100] , kase = 1 , k;
	scanf("%d" , &tst);
	gets(str);
	while(tst--){
		gets(str);
		ln = strlen(str);
		memset(st , -1 , sizeof(st));
		memset(id , -1 , sizeof(id));
		st[0] = 1;
		id[str[0]-'0'] = 1;
		j = 0;
		for(i = 1;i<ln;i++){
			if(id[str[i]-'0'] == -1){
				id[str[i]-'0'] = j;
				st[i] = j;
				j++;
			}
			else st[i] = id[str[i]-'0'];
			if(j == 1) j++;
		}
		if(j == 0) j = 2;
		unsigned __int64 ret = 0;
		k = 1;
		for(i = ln-1;i>=0;i--){
			ret += (k*st[i]);
			k *= j;
		}
		printf("Case #%d: %I64u\n", kase++ , ret);
	}
	return 0;
}

