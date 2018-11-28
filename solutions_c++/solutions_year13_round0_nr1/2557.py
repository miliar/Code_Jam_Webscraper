#include<cstdio>
#include<cstring>

using namespace std;

char G[4][5];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		printf("Case #%d: ",t);
		for(int i=0;i<4;++i)
			scanf("%s\n",G[i]);
		char kto='n';
		int ok;
		for(int i=0;i<4;++i){
			ok=1;
			for(int j=1;j<4;++j){
				if (G[i][j-1]!=G[i][j]&&G[i][j-1]!='T'&&G[i][j]!='T'){
					ok=0;
					break;
				}
				else if (G[i][j]!='T') kto=G[i][j];
			}
			if (ok&&kto!='.') goto vyhral;
			ok=1;
			for(int j=1;j<4;++j){
				if (G[j-1][i]!=G[j][i]&&G[j-1][i]!='T'&&G[j][i]!='T'){
					ok=0;
					break;
				}
				else if (G[j][i]!='T') kto=G[j][i];
			}
			if (ok&&kto!='.') goto vyhral;
		}
		ok=1;
		for(int i=1;i<4;++i){
			if (G[i-1][i-1]!=G[i][i]&&G[i-1][i-1]!='T'&&G[i][i]!='T'){
				ok=0;
				break;
			}
			else if (G[i][i]!='T') kto=G[i][i];
		}
		if (ok&&kto!='.') goto vyhral;
		ok=1;
		for(int i=1;i<4;++i){
			if (G[i-1][4-i]!=G[i][4-i-1]&&G[i-1][4-i]!='T'&&G[i][4-i-1]!='T'){
				ok=0;
				break;
			}
			else if (G[i][4-i-1]!='T') kto=G[i][4-i-1];
		}
		if (kto=='.') ok=0;
vyhral:;
		if (!ok){
			ok=0;
			for(int i=0;i<4;++i)
				if (strchr(G[i],'.')!=NULL){
					ok=1;
					puts("Game has not completed");
					break;
				}
			if (!ok)
				puts("Draw");
		}
		else
			printf("%c won\n",kto);
	}
	return 0;
}
