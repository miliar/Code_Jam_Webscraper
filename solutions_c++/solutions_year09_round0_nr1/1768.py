#include "stdio.h"
#include "string"
using namespace std;
char name[5001][16];
char str[999999];
bool hash[26][16];
bool match(char a[]) {
	for(int i = 0 ; a[i] ; i ++) {
		if(!hash[a[i]-'a'][i]) {
			return false;
		}
	}
	return true;
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	int L,D,N;
	while(scanf("%d%d%d",&L,&D,&N) == 3) {
		for(int i = 0 ; i < D ; i ++) {
			scanf("%s",name[i]);
		}
		for(int cas = 1; cas <= N ; cas ++) {
			memset(hash,false,sizeof(hash));
			int ret = 0;
			scanf("%s",str);
			int i = 0 ;
			int k = 0;
			while(str[i]) {
				if(str[i] == '(') {
					i ++;
					while(str[i] != ')') {
						hash[str[i]-'a'][k] = true;
						i ++;
					}
				} else {
					hash[str[i]-'a'][k] = true;
				}
				i ++;
				k ++;
			}
			for(int i = 0 ; i < D ; i ++) {
				if(match(name[i])) {
					ret ++;
				}
			}
			printf("Case #%d: %d\n",cas,ret);
		}
	}
	return 0;
}