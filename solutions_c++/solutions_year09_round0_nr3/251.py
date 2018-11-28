#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T,TT;
char linha[512];
char quero[]="welcome to code jam";
int PD[32][512];

int main(void) {
	scanf("%d",&TT);
	for(T=1;T<=TT;T++) {
		scanf(" %[^\n]",linha);
		int nlinha=strlen(linha);
		int tam=strlen(quero);
		memset(PD,0,sizeof(PD));
		for(int i=0;i<=nlinha;i++)
			PD[tam][i]=1;

		for(int letra=tam-1;letra>=0;letra--)
			for(int i=nlinha-1;i>=0;i--)
				PD[letra][i]=(PD[letra][i+1]+(linha[i]==quero[letra]?PD[letra+1][i+1]:0))%10000;
		printf("Case #%d: %04d\n",T,PD[0][0]);
	}
	return 0;
}
