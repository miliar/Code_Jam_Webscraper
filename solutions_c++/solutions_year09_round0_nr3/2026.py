#include<cstdio>
#include<cstring>

#include<map>
#include<algorithm>

#define inb(a,b) (a>=0 && a<h && b>=0 && b<w)

using namespace std;

char r[20] = "welcome to code jam";
char s[1000],o[1000];
int dp[1000][21];

int main(){
	int nn;
	gets(s);
	sscanf(s,"%d",&nn);
	for(int ii=1;ii<=nn;ii++){
		//scanf("%s",s);
		gets(s);
		memset(dp,0,sizeof(dp));
		int i;
		dp[0][0] = 1;
		for(i=1;s[i-1]!='\0';i++)dp[i][0]=1;
			
		for(i=1;s[i-1]!='\0';i++){
			for(int j=1;j<=19;j++){
				dp[i][j] = dp[i-1][j];
				if(s[i-1]==r[j-1]){
					dp[i][j]= (dp[i][j]+dp[i-1][j-1])%1000;
				}
			}
		}
		
		/*for(int iii=0;iii<i;iii++){
			for(int jj=0;jj<=19;jj++)printf("%3d",dp[iii][jj]);
			printf("\n");
		}*/
		
		sprintf(o,"%4d",dp[i-1][19]);
		for(int j=0;j<4;j++)if(o[j]==' ')o[j]='0';
		printf("Case #%d: %s\n", ii,o);
	}
		
	return 0;
}
