#include <set>
#include <cstdio>
#include <cstring>

using namespace std;

int L;
int D;
int N;
char cur[5555*26];
char s[5555][55];

int go2(char* cur,char* pattern)
{
	int pos=0;
	int len=strlen(cur);
	for(int i=0;i<len;){
		if(cur[i]=='('){
			set<char> dic;
			int j;
			for(j=i+1;cur[j]!=')';++j){
				dic.insert(cur[j]);
			}
			i=j+1;
			if(dic.find(pattern[pos])==dic.end()){
				return 0;
			}
			else{
				++pos;
			}
		}
		else{
			if(cur[i]!=pattern[pos]){
				return 0;
			}
			else{
				++pos;
			}
			++i;
		}
	}
	return pos==L?1:0;
}

int go()
{
	int ret=0;
	for(int i=0;i<D;++i){
		ret+=go2(cur,s[i]);
	}
	return ret;
}

int main()
{
	//freopen("A-small.in","r",stdin);
	//freopen("A-small.out","w",stdout);
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d%d%d",&L,&D,&N);
	
	for(int i=0;i<D;++i){
		scanf("%s",s[i]);
	}
	
	for(int i=1;i<=N;++i){
		scanf("%s",cur);
		printf("Case #%d: %d\n",i,go());
	}
}
