#include "cstdio"
#include "queue"
#include "algorithm"
#include "vector"
#include "cstring"
#include "string"
#include "cstdlib"
using namespace std;
char str[99];
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T ; cas ++) {
		scanf("%s",str);
		printf("Case #%d: ",cas);
		bool flag = false;
		int key = -1;
		for(int i = strlen(str) - 2; i >= 0 ; i --) {
			char minans = '9' + 1;
			int idx;
			for(int j = i + 1; str[j] ; j ++) {
				if(str[i] < str[j]) {
					flag = true;
					if(minans > str[j]) {
						minans = str[j];
						idx = j;
					}
				}
			}
			if(flag) {
				swap(str[i],str[idx]);
				key = i;
				break;
			}
		}
		if(flag) {
			sort(str+key+1,str+strlen(str));
			puts(str);
		} else {
			int len = strlen(str);
			str[len] = '0';
			str[len+1] = 0;
			sort(str,str+strlen(str));
			int idx = 0;
			for(int i = 0 ; str[i] ; i ++) {
				if(str[i] != '0') {
					printf("%c",str[i]);
					idx = i;
					break;
				}
			}
			for(int i = 0 ; i < idx ; i ++) {
				printf("%c",str[i]);
			}
			for(int i = idx +1 ; str[i] ; i ++) {
				printf("%c",str[i]);
			}
			puts("");
		}
	}
	return 0;
}