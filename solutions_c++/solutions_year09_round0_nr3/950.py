#include<iostream>
#include<cstring>
using namespace std;

char s[1000];
const char st[20] = "welcome to code jam" ;
int z,zz,n;
int f[1000][100];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&zz);
	for (int z=1;z<=zz;z++) {
		gets(s);
		int l=strlen(s);
		f[0][0]=0;
		for (int i=0;i<l;i++) {
			if (i > 0) f[i][0]=f[i-1][0];
			if (s[i]==st[0]) f[i][0]=(f[i][0]+1)% 10000;

			for (int j=1;j<19;j++) {
				f[i][j]=f[i-1][j];
			    if (s[i] == st[j])
					f[i][j]=(f[i-1][j-1]+f[i][j])% 10000;
			}
		}
		printf("Case #%d: ",z);
		if (f[l-1][18]>999) printf("%d\n",f[l-1][18]); else
		if (f[l-1][18]>99) printf("0%d\n",f[l-1][18]); else
		if (f[l-1][18]>9) printf("00%d\n",f[l-1][18]); else
		printf("000%d\n",f[l-1][18]);
	}
}

					
