#include <cstdio>
#include <iostream>
#include <memory.h>
using namespace std;

int s[210], Hash1[30][30], Hash2[30][30];
int weight[200];
char str[200];

int main () {
	freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);
	int T, n, i, l, t, tt, j, Case=0;
	scanf("%d", &T);
	while(T--) {
		Case++;
		memset(Hash1, -1, sizeof(Hash1));
		memset(Hash2, -1, sizeof(Hash2));
		scanf("%d", &n);
		for(i=0;i<n;i++) {
			scanf("%s", str);
			Hash1[str[0]-'A'][str[1]-'A']=Hash1[str[1]-'A'][str[0]-'A']=str[2]-'A';
		}
		scanf("%d", &n);
		for(i=0;i<n;i++) {
			scanf("%s", str);
			Hash2[str[0]-'A'][str[1]-'A']=Hash2[str[1]-'A'][str[0]-'A']=1;
		}
		scanf("%d", &l);
		scanf("%s", str);
		int top=0;
		s[0]=-1;
		memset(weight, 0, sizeof(weight));
		for(i=0;i<l;i++) {
			s[++top]=str[i]-'A';
			weight[s[top]]++;
			while(top>1) {
				t=s[top-1];
				tt=s[top];
				if(Hash1[t][tt]!=-1) {
					weight[t]--;
					weight[tt]--;
					top--;
					s[top]=Hash1[t][tt];
					weight[s[top]]++;
				}
				else
					break;
			}
			for(j=0;j<26;j++) {
				if(weight[j]>0) {
					if(Hash2[j][s[top]]==1) {
						top=0;
						memset(weight, 0, sizeof(weight));
						break;
					}
				}
			}
		}
		printf("Case #%d: ", Case);
		if(!top) {
			printf("[]\n");
		}
		else {
			printf("[");
			for(i=1;i<top;i++)
				printf("%c, ", s[i]+'A');
			printf("%c]\n", s[i]+'A');
		}
	}
	return 0;
}