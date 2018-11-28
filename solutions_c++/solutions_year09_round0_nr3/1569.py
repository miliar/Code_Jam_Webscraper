#include "iostream"
using namespace std;

char word[] = "welcome to code jam";
char str[1024];
int a[512][26];

int solve()
{
	int i,j,len,n;
	memset(a,0,sizeof(a));
	len=strlen(str);
	n=strlen(word);
	a[0][0]=1;
	for(i=1;i<=len;++i)a[i][0]=1;
	//for(j=1;j<=n;++j)a[0][j]=1;
	for(i=1;i<=len;++i){
		for(j=1;j<=n;++j){
			if(str[i-1]==word[j-1]){
				a[i][j]=(a[i-1][j-1]+a[i-1][j])%1000;
			}else{
				a[i][j]=a[i-1][j];
			}
		}
	}
	return a[len][n];
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	gets(str);
	for(i=1;i<=T;++i){
		gets(str);
		printf("Case #%d: %.4d\n",i, solve());
	}
	return 0;	
}