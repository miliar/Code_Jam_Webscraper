#include<cstdio>
#include<string>
#include<cstring>

using namespace std;

const string Str = "welcome to code jam";

int F[600][25];
char Buff[600];

int main() {
	freopen("C.txt","r",stdin);
	freopen("C.out","w",stdout);
	
	int T;
	scanf("%d\n",&T);
	for(int t = 0 ; t < T ; t++) {
		gets(Buff);
		memset(F,0,sizeof(F));
		int Len = strlen(Buff);
		if (Buff[0] == Str[0]) {
			F[0][0] = 1;
		}
		for(int i = 1 ; i < Len; i++) {
			if (Buff[i] == Str[0]) {
				F[i][0] = F[i - 1][0] + 1;
			}
			else {
				F[i][0] = F[i - 1][0];
			}
		}
		for(int i = 1 ; i < Len; i++) {
			for(int j = 1 ; j < Str.length(); j++) {
				if (Buff[i] == Str[j]) {
					F[i][j] = F[i - 1][j] + F[i - 1][j - 1];
				}
				else {
					F[i][j] = F[i - 1][j];
				}
				F[i][j] = F[i][j] % 10000;
			//	printf("%04d ",F[i][j]);
			}
		//	printf("\n");
		}
		printf("Case #%d: %04d\n", t + 1,F[Len - 1][Str.length() - 1]);
	}
	
//	while(1);
	return 0;
}
