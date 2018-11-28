#include <iostream>
#include <string>
using namespace std;

int L,D,N;
char dic[5000][16];
char pat[10000];

int pLen;
int id[5000],cnt;
bool v[26];

bool Input(){
	if(scanf("%d%d%d",&L,&D,&N)==EOF){
		return 0;
	}
	int i,j,k;
	for(i=0;i<D;++i){
		scanf("%s",&dic[i]);
	}
    return 1;
}

void Proc(int cn){
	int i,j,k;
	cnt=D;
	for(i=0;i<D;++i){
		id[i]=i;
	}
	for(j=0,i=0;i<L&&cnt>0;++i){
		memset(v,0,sizeof(v));
		if(pat[j]=='('){
			++j;
			while(j<pLen&&pat[j]!=')'){
				v[pat[j]-'a']=1;
				++j;
			}
			++j;
		}else{
			v[pat[j]-'a']=1;
			++j;
		}
		int c=0;
		for(k=0,c=0;k<cnt;++k){
			if(v[dic[id[k]][i]-'a']){
				id[c++]=id[k];
			}
		}
		cnt=c;
	}
	printf("Case #%d: %d\n",cn,cnt);
	return;
}

void Solve(){
	int i;
	for(i=1;i<=N;++i){
		scanf("%s",&pat);
		pLen=strlen(pat);
		Proc(i);
	}
    return;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    while(Input()){
        Solve();
    }
    return 0;
}
