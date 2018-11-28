//BISMILLAHHIRRAHMANIRRAHIM

#include <iostream>
#include <cstring>
using namespace std;

const char w[]="welcome to code jam";
char query[550];

int r[510][100];

int dp(int q,int k) {
	if(r[q][k]) return r[q][k];
	if(!w[k]) {
		//cout<<q<<' '<<k<<'\n';
		return r[q][k]=1;
	}
	else if(!query[q]) return r[q][k]=0;
	for(int i=q;query[i];i++) if(query[i]==w[k]) {
		
		r[q][k]=(r[q][k]+dp(i+1,k+1))%10000;
		//cout<<query[q]<<' '<<w[k]<<' '<<q<<' '<<k<<' '<<r[q][k]<<'\n';
	}
	return r[q][k];
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t,I=1;
	for(scanf("%d",&t),fgetc(stdin);I<=t;I++) {
		gets(query);
		memset(r,0,sizeof(r));
		printf("Case #%d: %.4d\n",I,dp(0,0));
	}
	return 0;
}
