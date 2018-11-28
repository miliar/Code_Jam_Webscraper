#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#define maxn 60
using namespace std;

typedef long long ll;

int p1[100],p2[100];
int zhan[1010000];
char s[1010000];
int c[30][30];
int show[30];

void solve(){
	int n1,n2,n,i,j,top;
	scanf("%d",&n1);
	for(i=1;i<=26;++i)
		for(j=1;j<=26;++j)c[i][j]=-1;
	for(i=1;i<=n1;++i){
		scanf("%s",s);
		c[s[0]-'A'+1][s[1]-'A'+1]=s[2]-'A'+1;
		c[s[1]-'A'+1][s[0]-'A'+1]=s[2]-'A'+1;
	}
	scanf("%d",&n2);
	for(i=1;i<=n2;++i){
		scanf("%s",s);
		p1[i]=s[0]-'A'+1;
		p2[i]=s[1]-'A'+1;
	}
	scanf("%d%s",&n,s+1);
	for(i=1;i<=26;++i)show[i]=0;
	top=0;
	for(i=1;i<=n;++i){
		zhan[++top]=s[i]-'A'+1;
		++show[zhan[top]];
		while(top>=2 && c[zhan[top-1]][zhan[top]]!=-1){
			--show[zhan[top]];
			--show[zhan[top-1]];
			zhan[top-1]=c[zhan[top-1]][zhan[top]];
			--top;
			++show[zhan[top]];
		}
		for(j=1;j<=n2;++j)if(show[p1[j]]>0 && show[p2[j]]>0)break;
		if(j<=n2){
			//cout<<p1[j]<<" "<<p2[j]<<endl;
			while(top>0)--show[zhan[top--]];
		//cout<<top<<endl;
		}
	}
	printf("[");
	for(i=1;i<=top;++i)if(i<top)printf("%c, ",zhan[i]-1+'A');else printf("%c",zhan[i]-1+'A');
	printf("]\n");
}

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
}

