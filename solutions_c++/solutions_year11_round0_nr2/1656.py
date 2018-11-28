#include<iostream>
#include<cstring>
#include<stdlib.h>
#include<algorithm>

using namespace std;

#define MAX 900

int trans(char a, char b){
	return ((a-'A'+1)*27+b-'A'+1);
}
int thash[MAX];
bool chash[MAX];
char temp[105], str[105];
int main(void){
	int cas, c, d, n, cnt, cur;
	bool sign;
	freopen("B4.in", "r", stdin);
	freopen("test.out", "w", stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++){
		memset(thash, 0, sizeof(thash));
		memset(chash, 0, sizeof(chash));
		scanf("%d", &c);
		for (int i = 0; i < c; i++){
			scanf("%s", &temp);
			thash[trans(temp[0], temp[1])] = temp[2];
			thash[trans(temp[1], temp[0])] = temp[2];
		}
		scanf("%d", &d);
		for (int i = 0; i < d; i++){
			scanf("%s", &temp);
			chash[trans(temp[0], temp[1])] = true;
			chash[trans(temp[1], temp[0])] = true;
		}
		scanf("%d", &n);
		scanf("%s", &temp);
		cnt = 0;
		for (int i = 0; i < n; i++){
			sign = false;
			if (cnt == 0)	str[cnt++] = temp[i];
			else{
				if (cur = thash[trans(temp[i], str[cnt-1])])
					str[cnt-1] = cur;
//				else if (chash[trans(temp[i], str[cnt-1])] || chash[trans(str[cnt-1], temp[i])])
//					cnt--;
				else{
					for (int j = 0; j < cnt; j++)
						if (chash[trans(temp[i], str[j])]){
							cnt = 0; sign = true;break;
						}
					if (sign) continue;
					str[cnt++] = temp[i];
				}
			}
		}
		printf("Case #%d: [", t);
		if (cnt == 0){
			printf("]\n");continue;
		}
		for (int i = 0; i < cnt-1; i++)
			printf("%c, ", str[i]);
		printf("%c]\n", str[cnt-1]);
	}
	return 0;
}