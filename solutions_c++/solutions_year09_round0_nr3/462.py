#include <iostream>
using namespace std;
FILE *in = fopen("C-large.in","r");
FILE *out = fopen("C-large.out","w");

char pattern[] = "welcome to code jam";
char text[505];
int f[20][505];

int solve(){
	int i,j;
	int n = strlen(pattern);
	int m = strlen(text);
	if(m<n)return 0;
	
	memset(f,0,sizeof(f));

	for(j = 1; j <=m; j++){
		if(pattern[0] == text[j-1])
			f[1][j] = f[1][j-1]+1;
		else
			f[1][j] = f[1][j-1];
	}

	for(i = 2; i <= n; i++){
		for(j = i; j <= m; j ++)
		{
			if(pattern[i-1] == text[j-1])
				f[i][j] = f[i-1][j-1]+f[i][j-1];
			else 
				f[i][j] = f[i][j-1];

			f[i][j]%=10000;
		}
	}
// 	for(i = 1; i <= n; i++){
// 		for(j = 1; j<= m; j++)
// 			fprintf(out,"%d ",f[i][j]);
// 		fprintf(out,"\n");
// 	}
	return f[n][m];
}

int main(){
	//printf("%d\n",strlen(pattern));
	int n,t;
	fscanf(in,"%d",&n);
	fgetc(in);
	t = 0;
	while(n--){
		t++;
		fgets(text,505,in);
		text[strlen(text)-1] = '\0';
		//fgetc(in);
		int ans = solve();
		ans %= 10000;
		fprintf(out,"Case #%d: %04d\n",t,ans);
	}
	return 0;
}