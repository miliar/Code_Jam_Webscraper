#include<cstdio>
#include<cstring>
#include<string>

#include<map>
#include<algorithm>

using namespace std;

int na;

struct TT{
	string si;
	TT* c[122];
	TT(){memset(c,0,sizeof(c));}
	int walk(char* s);
};

TT a[20007];
char ks[1111];

	int TT::walk(char* s){
		if(!*s)return 0;
		char ts[122];
		//printf(" walk : %s for %s\n", si.c_str(), s);
		int i, j;
		for(j=0; s[j]!='/'; j++){
			ts[j]=s[j];
		}
		ts[j]=0;
		string st(ts);
		for(i=0; c[i]; i++)if(st==c[i]->si){
			break;
		}
		if(!c[i]){
			c[i] = &a[na++];
			*c[i] = TT();
			c[i]->si = st;
			return c[i]->walk(s+j+1)+1;
		}
			return c[i]->walk(s+j+1);
	}
	
int main(){
	int tt,n,m;
	scanf("%d", &tt);
	for(int ii=0;ii<tt;ii++){
		na=1;
		a[0]=TT();
		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++){
			scanf("%s", ks);
			int tl = strlen(ks);
			ks[tl]='/';
			ks[tl+1]=0;
			a[0].walk(ks+1);
		}
		int ans=0;
		for(int i=0;i<m;i++){
			scanf("%s", ks);
			int tl = strlen(ks);
			ks[tl]='/';
			ks[tl+1]=0;
			ans+=a[0].walk(ks+1);
		}
		printf("Case #%d: %d\n", ii+1, ans);
	}
		
	return 0;
}
