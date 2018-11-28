#include<cstdio>

char words[5005][20];

int n,d,l;

char s[500000];

bool match[20][255];

int alg(){
	scanf("%s",s+1);
	int c = 1;
	for(int i=1;i<=l;i++) for(int j='a';j<='z';j++) match[i][j] = 0;
	for(int i=1;i<=l;i++){
		if(s[c] == '('){
			++c;
			while(s[c] != ')'){
				match[i][s[c]] = 1;
				++c;
			}
			++c;
		}else{
			match[i][s[c]] = 1;
			++c;
		}
	}
	int w = 0;
	for(int i=1;i<=d;i++){
		bool ok = 1;
		for(int j=1;j<=l;j++) if(!match[j][words[i][j]]){
			ok = 0;
			break;
		}
		if(ok) ++w;
	}
	return w;
}

int main(){
	scanf("%d%d%d",&l,&d,&n);
	for(int i=1;i<=d;i++)
		scanf("%s",words[i] + 1);
	for(int i=1;i<=n;i++)
		printf("Case #%d: %d\n",i,alg());
}
