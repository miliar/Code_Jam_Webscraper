#include<cstdio>
#include<cstring>
using namespace std;
void cmax(int &a,int b){if(a<b)a=b;}
int gao(){
#define S(x) ((x)>1&&(x)<29)
#define SP(x)	(((x)+4)/3>=p)
#define USP(x)	(((x)+2)/3>=p)
	static int f[128][128],t[128],n,s,p;
	scanf("%d%d%d",&n,&s,&p);
	for(int i=0;i<n;++i)scanf("%d",t+i);
	memset(f,0,sizeof(f));
	for(int i=0;i<n;++i)
		for(int j=0;j<=i;++j){
			if(S(t[i])){
				cmax(f[i+1][j+1],f[i][j]+SP(t[i]));
			}
			cmax(f[i+1][j],f[i][j]+USP(t[i]));
		}
	return f[n][s];
}
int main(){
	int Tc;
	scanf("%d",&Tc);
	for(int tc=1;tc<=Tc;++tc)
		printf("Case #%d: %d\n",tc,gao());
	return 0;
}
