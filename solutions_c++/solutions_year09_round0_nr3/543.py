#include <stdio.h>

char s[100]=" welcome to code jam";
int v[505][50];

int main(void)
{
	int n, i, cs=0, j;
	char z[1000];
	scanf("%d",&n);
	gets(z);
	while(n--){
		gets(z+1);
		for(j=0;j<=19;j++)
			v[0][j]=0;
		v[0][0] = 1;
		for(i=1;z[i];i++){
			v[i][0] = 1;
			for(j=1;j<=19;j++)
				if(s[j]==z[i])
					v[i][j] = (v[i-1][j]+v[i][j-1])%10000;
				else
					v[i][j] = v[i-1][j];
		}
		printf("Case #%d: %04d\n",++cs,v[i-1][19]);
	}
	return 0;
}
