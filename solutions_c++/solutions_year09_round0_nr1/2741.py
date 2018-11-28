#include<cstdio>
#include<set>

using namespace std;

char dict[6000][50];
char lang[6000];
set<char> poss[50];

int main(){
	int L,D,N;
	int nWord,isWord;
	int i,j,k,cases=1;
	scanf("%d %d %d\n",&L,&D,&N);
	for(i=0;i<D;i++){
		scanf("%s\n",dict[i]);
	}
	for(i=0;i<N;i++){
		scanf("%s\n",lang);
		nWord = 0;
		for(j=0;j<L;j++){
			poss[j].clear();
		}
		j=0;
		k=0;
		while(lang[j]!='\0'){
			if(lang[j]=='('){
				j++;
				//printf("inserting a group (%d)\n",k);
				for(;lang[j]!=')';j++){
					poss[k].insert(lang[j]);
					//printf("%c ",lang[j]);
				}
				//printf("\n");
				k++;
				j++;
			}else{
				//printf("inserting letter %c (%d)\n",lang[j],k);
				poss[k++].insert(lang[j]);
				j++;
			}
		}
		for(j=0;j<D;j++){
			isWord = 1;
			for(k=0; isWord && k<L;k++){
				if(!poss[k].count(dict[j][k])){
					isWord = 0;
				}
			}
			nWord+=isWord;
		}
		printf("Case #%d: %d\n",cases++,nWord);
	}
	
}
