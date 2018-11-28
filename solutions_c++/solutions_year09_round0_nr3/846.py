#include<cstdio>
#include<cstring>
using namespace std;

const char welcome[]=" welcome to code jam";

int main() {
	int welcomelen=strlen(welcome),testow;
	scanf("%d\n",&testow);
	for(int z=1;z<=testow;++z) {
		int t[505][22]={{1}};
		char tekst[505];
		fgets(tekst+1,504,stdin);
		int tekstlen=strlen(tekst+1);
		for(int i=1;i<=tekstlen;++i)
			for(int j=1;j<welcomelen;++j) {
				if(tekst[i]==welcome[j]) {
					for(int k=0;k<i;++k)
						t[i][j]=(t[i][j]+t[k][j-1])%10000;
				}
			}
		int wynik=0;
		for(int i=1;i<=tekstlen;++i)
			wynik=(wynik+t[i][welcomelen-1])%10000;
		printf("Case #%d: %04d\n",z,wynik);
	}
}
