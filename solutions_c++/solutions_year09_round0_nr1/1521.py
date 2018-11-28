#include <string>
using namespace std;
int words[5000][16];
int L, D, N;

inline bool matches(int pattern[], int index){
	for(int i=0;i<L;++i){
		if(!(words[index][i]&pattern[i])){
			return false;
		}
	}
	return true;
}

int countMatches(int pattern[]){
	int count=0;
	for(int i=0;i<D;++i)
		count+=matches(pattern, i);
	return count;
}

int main(int argc, char *argv[]){
	char buffer[1000];
	scanf("%d%d%d", &L, &D, &N);
	for(int i=0;i<D;++i){
		scanf("%s", buffer);
		for(int j=0;j<L;++j){
			words[i][j]=1<<(buffer[j]-'a');
		}
	}
	for(int caseNum=1;caseNum<=N;++caseNum){
		int pattern[16];
		scanf("%s", buffer);
		for(int i=0, pos=0;i<L;++i, ++pos){
			pattern[i]=0;
			if(buffer[pos]=='('){
				++pos;
				while(buffer[pos]!=')'){
					pattern[i]|=1<<(buffer[pos]-'a');
					++pos;
				}
			}else{
				pattern[i]=1<<(buffer[pos]-'a');
			}
		}

		int sol=countMatches(pattern);

		printf("Case #%d: %d\n", caseNum, sol);
	}


	return 0;
}