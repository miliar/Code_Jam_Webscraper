#include <cstdio>
#include <algorithm>

using namespace std;

int cases, combs, oppos, len, alen;

char comb[40][4];
char oppo[30][3];

char invoke[110];
char ans[110];

char combine(char a, char b){
	if(a>b) return combine(b,a);
	for(int i=0; i<combs; ++i){
		if(a==comb[i][0] && b==comb[i][1]){
			return comb[i][2];
		}
	}
	return (char)0;
}


bool opposites(){
	char tofind;
	for(int i=0; i<oppos; ++i){
		if(oppo[i][0]==ans[alen]){
			tofind=oppo[i][1];
		}else if(oppo[i][1]==ans[alen]){
			tofind=oppo[i][0];
		}else{
			continue;
		}
		for(int j=0; j<alen; ++j){
			if(ans[j]==tofind) return true;
		}
	}
	return false;
}



int main(){
	scanf("%d",&cases);
	for(int c=1; c<=cases; ++c){
		scanf("%d",&combs);
		for(int i=0; i<combs; ++i){
			scanf("%s",comb[i]);
			sort(comb[i],comb[i]+2);
		}
		scanf("%d",&oppos);
		for(int i=0; i<oppos; ++i){
			scanf("%s",oppo[i]);
		}
		scanf("%d %s",&len,invoke);
		alen=1;
		ans[0]=invoke[0];
		for(int i=1; i<len; ++i){
			ans[alen]=invoke[i];
			if(alen>0){
				char combination=combine(ans[alen],ans[alen-1]);
				if(combination!=0){
					ans[alen-1]=combination;
				}else{
					if(opposites()){
						alen=0;
					}else{
						++alen;
					}
				}
			}else{
				++alen;
			}
		}
		ans[alen]='\0';
		printf("Case #%d: [",c);
		for(int i=0; i<alen; ++i){
			printf("%c",ans[i]);
			if(i!=alen-1){
				printf(", ");
			}
		}
		printf("]\n");
	}

	return 0;
}

