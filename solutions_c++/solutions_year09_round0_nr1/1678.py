#include <cstdio>
#include <cstring>
char word[5010][20],s[1000];
bool pat[20][26];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int L,D,N;
	scanf("%d %d %d",&L,&D,&N);
	for(int i=0;i<D;++i) scanf("%s",word[i]);
	for(int cas=1;cas<=N;++cas){
		scanf("%s",s);
		memset(pat,0,sizeof(pat));
		for(int i=0,j=0;i<L;++i,++j){
			if(s[j]=='('){
				for(++j;s[j]!=')';++j) pat[i][s[j]-'a']=true;
			}
			else pat[i][s[j]-'a']=true;
		}
		int cnt=0;
		for(int i=0;i<D;++i){
			bool ok=true;
			for(int j=0;j<L&&ok;++j)
				if(!pat[j][word[i][j]-'a']) ok=false;
			cnt+=ok;
		}
		printf("Case #%d: %d\n",cas,cnt);
	}
	return 0;
}
