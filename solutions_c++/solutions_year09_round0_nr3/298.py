#include<stdio.h>
#include<string.h>


const int N=603;
const int M=10000;
const int kl=18;

char key[20]={"welcome to code jam"};	//0-18


int f[N][30];
char s[N];
int m;


int dp(int a,int b){
	if(f[a][b]!=-1) return f[a][b];
	f[a][b]=dp(a-1,b);
	if(s[a-1]==key[b-1]) f[a][b]=(f[a][b]+dp(a-1,b-1))%M;
	
	return f[a][b];
}


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca=0;
	int n;
	int i,j,k,t,ans,x,y,ft,cnn;
	scanf("%d",&n); gets(s);
	while(n--){
		gets(s);
		memset(f,-1,sizeof(f));
		m=strlen(s);
		for(i=0;i<m;i++) f[i][0]=1;

		printf("Case #%d: %04d\n",++ca,dp(m,19));
	}
	return 0;
}