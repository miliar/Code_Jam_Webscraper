#include <cstdio>
#include <string>
using namespace std;

const int maxD=6000,maxL=16;
char S[maxD][maxL];
int L,D,N;

int main(){
	scanf("%d%d%d\n",&L,&D,&N);
	for(int i=0;i<D;++i){
		gets(S[i]);
	}
	for(int i=1;i<=N;++i){
		char buf[1024];
		gets(buf);
		string s[maxL];
		for(int j=0,cur=0;j<L;++j){
			if(buf[cur++]!='('){
				s[j]+=buf[cur-1];
				continue;
			}
			while(buf[cur++]!=')'){
				s[j]+=buf[cur-1];
			}
		}
		int count=0;
		for(int j=0;j<D;++j){
			int k;
			for(k=0;k<L;++k){
				if(s[k].find(S[j][k])==string::npos)
					break;
			}
			if(k==L)
				++count;
		}
		printf("Case #%d: %d\n",i,count);
	}
}
