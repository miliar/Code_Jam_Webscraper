#include<cstdio>
#include<cstring>
int n;
int mc[2][600];
char gj[]="welcome to code jam";
int gjl;
int main() {
//	freopen("jam31.in","r",stdin);
//	freopen("jam31.out","w",stdout);
	int i,j,k;
	char str[600];
	int lstr;
	gjl = strlen(gj);
	scanf("%d ",&n);
	for(i=0;i<n;i++) {
		gets(str);
		lstr = strlen(str);
		mc[0][0]=(str[0]=='w');
		for(k=1;k<lstr;k++)
			mc[0][k]=mc[0][k-1]+(str[k]=='w');
		for(j=1;j<gjl;j++) {
			mc[j%2][0]=(str[0]==gj[j])?mc[!(j%2)][0]:0;
			for(k=1;k<lstr;k++)
				mc[j%2][k]=(  mc[j%2][k-1]+((str[k]==gj[j])?mc[!(j%2)][k]:0)  ) %1000;
		}
		printf("Case #%d: %04d\n",i+1,mc[!(j%2)][lstr-1]);
		
	}
}

