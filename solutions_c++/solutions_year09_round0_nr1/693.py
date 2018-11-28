#include <stdio.h>

const int size=5010;
const int len=20;

char s[size][len];

int main(){
	int L,D,N;
	scanf("%d%d%d",&L,&D,&N);
	for(int i=0; i<D; i++)
		scanf("%s",s[i]);
	for(int cs=1; cs<=N; cs++){
		char t[1000];
		scanf("%s",t);
		int c=0;
		for(int i=0; i<D; i++){
			int j,p=0;
			for(j=0; j<L; j++){
				if(t[p]=='('){
					for(p++; t[p]!=')'; p++)
						if(t[p]==s[i][j]) break;
					if(t[p]==')') break;
					for(p++; t[p]!=')'; p++);
					p++;
				}else{
					if(t[p]!=s[i][j]) break;
					p++;
				}
			}
			if(j>=L) c++;
		}
		printf("Case #%d: %d\n",cs,c);
	}
	return 0;
}
