#include <stdio.h>
#include <memory.h>
#include <string.h>

char dat[5001][20], ddd[1000001];
bool rock[15][26];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int L, D, N;
	scanf("%d %d %d",&L,&D,&N);
	int i, len, j, th, k, sol;
	for(i=0;i<D;i++){
		scanf("%s",dat[i]);
	}
	for(i=1;i<=N;i++){
		memset(rock, 0, sizeof(rock));
		scanf("%s",ddd);
		len = strlen(ddd);
		th = 0;
		sol = 0;
		for(j=0;j<len;j++){
			if(ddd[j] == '('){
				for(j++;j<len;j++){
					if(ddd[j] == ')'){
						break;
					}
					else{
						rock[th][ddd[j]-'a'] = true;
					}
				}
				th ++;
			}
			else{
				rock[th][ddd[j]-'a'] = true;
				th ++;
			}
		}
		for(j=0;j<D;j++){
			for(k=0;k<L;k++){
				if(!rock[k][ dat[j][k]-'a' ]) break;
			}
			if(k == L) sol++;
		}
		printf("Case #%d: %d\n", i, sol);
	}
	return 0;
}