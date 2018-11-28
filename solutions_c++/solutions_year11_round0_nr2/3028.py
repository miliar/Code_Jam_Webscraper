#include <cstdio>
#include <string>
int c,d,n;
int oppose[26][26];
int react[26][26];
char realstr[110];
char epsilon[110];
int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int T,Ti;
	scanf("%d",&T);
	for(Ti=0;Ti<T;Ti++) {
		scanf("%d ",&c);
		int i;
		for(i=0;i<c;i++) {
			scanf("%s",epsilon);
			react[epsilon[0]-'A'][epsilon[1]-'A']=react[epsilon[1]-'A'][epsilon[0]-'A']=(int)epsilon[2];
		}
		scanf("%d ",&d);
		for(i=0;i<d;i++) {
			scanf("%s",epsilon);
			oppose[epsilon[0]-'A'][epsilon[1]-'A']=oppose[epsilon[1]-'A'][epsilon[0]-'A']=1;
		}
		scanf("%d ",&n);
		scanf("%s",epsilon);
		int dep=0;
		realstr[dep++]=epsilon[0];
		int j,k;
		for(i=1;i<n;i++) {
			realstr[dep]=epsilon[i];
			if(dep>0) {
				if(react[realstr[dep-1]-'A'][realstr[dep]-'A']!=0) {
					realstr[dep-1]=(char)react[realstr[dep-1]-'A'][realstr[dep]-'A'];
					realstr[dep]=0;
				} else {
					int pujo=0;
					for(j=dep-1;j>=0;j--) {
						if(oppose[realstr[j]-'A'][realstr[dep]-'A']) {
							for(k=0;k<=dep;k++) realstr[k]=0;
							dep=0;
							pujo=1;
							break;
						}
					}
					if(!pujo) dep++;
				}
			} else dep++;
		}
		printf("Case #%d: [",Ti+1);
		for(i=0;i<dep-1;i++) {
			printf("%c, ",realstr[i]);
		}
		if(dep>0) printf("%c",realstr[i]);
		printf("]\n");
		for(i=0;i<26;i++) {
			for(j=0;j<26;j++) {
				oppose[i][j]=react[i][j]=0;
			}
		}
		for(i=0;i<100;i++) realstr[i]=epsilon[i]=0;
		dep=0;
	}
	return 0;
}