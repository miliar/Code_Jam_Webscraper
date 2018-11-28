#include "iostream"
using namespace std;

const int maxS = 16;
const int maxD = 5000;
int word[maxD][maxS];
char pat[1024];
int p[maxS];
int L,D,N;

int solve()
{
	int i,j,cot=0;
	int len=strlen(pat);
	int k=0;
	memset(p,0,sizeof(p));
	for(i=0;i<len;++i){
		if(pat[i]=='('){
			for(j=i+1;pat[j]!=')';++j){
				p[k]|=(1<<(pat[j] - 'a'));
			}
			i=j;
			++k;
		}else{
			p[k]|=(1<<(pat[i] - 'a'));
			++k;
		}
	}

	for(i=0;i<D;++i){
		int* w = word[i];
		for(j=0;j<L;++j){
			if(!(p[j] & w[j])){
				break;
			}
		}
		if(j>=L) cot++;
	}
	return cot;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	int i,j;
	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;++i){
		scanf("%s",&pat);
		for(j=0;j<L;++j){
			word[i][j]=(1<<(pat[j]-'a'));
		}
	}
	for(i=0;i<N;++i){
		scanf("%s",&pat);
		printf("Case #%d: %d\n", i+1, solve());
	}
	return 0;
}