#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int main() {
	int TC;
	int i,j;
	char dig[100];
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	scanf("%d",&TC);
	for(int T=1;T<=TC;T++) {
		scanf("%s",dig);
		int len=strlen(dig);
		for(i=len-1;i>=0;i--) {
			int min='9';
			int mini=-1;
			for(j=i+1;j<len;j++) {
				if (dig[j]>dig[i] && dig[j]<=min) {
					min=dig[j];
					mini=j;
				}
			}
			if (mini!=-1) {
				swap(dig[i],dig[mini]);
				sort(dig+i+1,dig+len);
				break;
			}
		}
		printf("Case #%d: ", T);
		if (i<0) {
			char min='9';
			int mini=-1;
			for(i=0;i<len;i++) {
				if (dig[i]<=min && dig[i]>'0') {
					mini=i;
					min=dig[i];
				}
			}
			dig[mini]=dig[0];
			sort(dig+1,dig+len);
			printf("%c0%s\n",min,dig+1);
		}
		else {
			printf("%s\n",dig);
		}
	}
	return 0;
}