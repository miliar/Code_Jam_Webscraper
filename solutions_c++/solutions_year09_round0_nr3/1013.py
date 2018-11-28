#include <cstdio>
#include <cstring>
using namespace std;

const char S[]="welcome to code jam";
const int Sn=sizeof(S)-1;

const int maxn=512;
const int MOD=10000;
int f[maxn][Sn];
char s[maxn];

int main(){
	int T;
	scanf("%d",&T);
	getchar();
	for(int t=1;t<=T;++t){
		gets(s);
		memset(f,0,sizeof(f));
		f[0][0]=(s[0]==S[0]);
		int n=strlen(s);
		for(int i=1;i<n;++i){
			for(int j=0;j<Sn;++j){
				f[i][j]=f[i-1][j];
				if(s[i]==S[j]){
					if(j==0)
						++f[i][j];
					else
						f[i][j]+=f[i-1][j-1];
				}
				f[i][j]%=MOD;
			}
		}
		printf("Case #%d: %.4d\n",t,f[n-1][Sn-1]);
	}
}
