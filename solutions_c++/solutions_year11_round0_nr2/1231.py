#include <stdio.h>
#include <string.h>

char combine[256][256];
char opposed[256];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		memset(combine,0,sizeof(combine));
		memset(opposed,0,sizeof(opposed));
		int c,d;
		scanf("%d",&c);
		for(int i=0;i<c;++i) {
			char str[10];
			scanf("%s",str);
			combine[str[0]][str[1]]=str[2];
			combine[str[1]][str[0]]=str[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;++i) {
			char str[10];
			scanf("%s",str);
			opposed[str[0]]=str[1];
			opposed[str[1]]=str[0];
		}
		int n;
		char str[200];
		scanf("%d%s",&n,str);
		char res[200];
		int len=0;
		for(int i=0;i<n;++i) {
			res[len++]=str[i];
			for(;;) {
				if(len>1) {
					char t=combine[res[len-2]][res[len-1]];
					if(t) {
						res[len-2]=t;
						--len;
						continue;
					}
					t=opposed[res[len-1]];
					if(t) {
						for(int j=0;j<len-1;++j)
							if(res[j]==t) {
								len=0;
								break;
							}
					}
				}
				break;
			}
		}
		printf("Case #%d: [",test);
		for(int i=0;i<len;++i) {
			if(i>0) printf(", ");
			printf("%c",res[i]);
		}
		printf("]\n");
	}
	return 0;
}
