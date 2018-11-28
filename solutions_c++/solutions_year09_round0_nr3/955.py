#include <cstdio>
#include <string>

#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,a,b) for(i=a;i<=b;i++)

#define N 510
#define M 20
#define modul 10000

int n,m,i,j,test,t;
char ch;
char a[N];
char b[]="welcome to code jam";
int f[N][M];

inline int numdigits(int a)
{
	if(a==0)return 1;
	int ans=0;
	while(a>0){
		ans++;
		a/=10;
	}
	return ans;
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d%c",&test,&ch);
	m=strlen(b);
	FOR(t,1,test){
		gets(a);
		n=strlen(a);
		memset(f,0,sizeof(f));
		FOR(i,0,n)
			f[i][0]=1;
		FOR(i,1,n)
			FOR(j,1,m){
				if(a[i-1]==b[j-1])
					f[i][j]=f[i-1][j-1];
				f[i][j]=(f[i][j]+f[i-1][j])%modul;
			}
		printf("Case #%d: ",t);
		j=numdigits(f[n][m]);
		FOR(i,1,4-j)
			printf("0");
		printf("%d\n",f[n][m]);
	}
	return 0;
}
