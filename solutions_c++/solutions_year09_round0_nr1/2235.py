#include <stdio.h>
char word[10000][20];

void parse(char st[], int len, int a[]) {
	int p=0;
	int i=0;
	while(st[p]!=0) {
		a[i]=0;
		if (st[p]=='(') {
			p++;
			while(st[p]!=')') {
				a[i] |= (1<<(st[p]-'a'));
				p++;
			}
			p++;
		}
		else {
			a[i] |= (1<<(st[p]-'a'));
			p++;
		}
		i++;
	}
	return;
}

int main() {
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int i,j,k;
	int a[20];
	char st[2000];
	int L,D,N;

	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;i++) {
		scanf("%s", word[i]);
	}
	for(i=0;i<N;i++) {
		scanf("%s",&st);
		parse(st,L,a);
		int ans=0;
		for(j=0;j<D;j++) {
			bool flag=true;
			for(k=0;k<L;k++) {
				if (a[k]&(1<<(word[j][k]-'a'))) {
				}
				else {
					flag=false;
					break;
				}
			}
			if (flag) ans++;
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
