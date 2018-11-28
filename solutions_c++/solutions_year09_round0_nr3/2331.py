#include <iostream>
#include <string>
using namespace std;

const char* s="welcome to code jam";
const int sLen=strlen(s);

char a[501];
int aLen;

int f[500][501];

bool Input(){
	gets(a);
    return 1;
}

void Solve(int cn){
	int i,j,k;
	aLen=strlen(a);
	memset(f,0,sizeof(f));
	f[0][0]=1;
	for(i=1;i<=aLen;++i){
		for(j=0;j<=sLen&&j<=i;++j){
			f[i][j]=f[i-1][j];
			if(j>0&&(a[i-1]==s[j-1])){
				f[i][j]+=f[i-1][j-1];
			}
			f[i][j]%=10000;
		}
	}
	printf("Case #%d: %04d\n",cn,f[aLen][sLen]);
    return;
}

int main() {
	freopen("C-small.in","r",stdin);
	//freopen("C-small.in","r",stdin);
	freopen("out.txt","w",stdout);
	int N;
	scanf("%d",&N);
	gets(a);
	int i;
	for(i=1;i<=N;++i){
		Input();
		Solve(i);
	}
    return 0;
}
