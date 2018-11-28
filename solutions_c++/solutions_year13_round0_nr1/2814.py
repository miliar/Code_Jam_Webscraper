#include <cstdio>
#include <vector>

using namespace std;

const int N=4;

char grille[N][N+1];

void pb(){
	for (int i=0;i<N;i++)
		scanf("%s",grille[i]);
	for (int i=0;i<N;i++){
		char cur=grille[i][0];
		if (cur=='.')
			continue;
		bool ok=true;
		for (int j=0;j<N;j++)
			if (cur=='T')
				cur=grille[i][j];
			else if (grille[i][j]!='T' && grille[i][j]!=cur)
				ok=false;
		if (ok && cur!='.'){
			printf("%c won\n",cur);
			return;
		}
	}
	for (int i=0;i<N;i++){
		char cur=grille[0][i];
		if (cur=='.')
			continue;
		bool ok=true;
		for (int j=0;j<N;j++)
			if (cur=='T')
				cur=grille[j][i];
			else if (grille[j][i]!='T' && grille[j][i]!=cur)
				ok=false;
		if (ok && cur!='.'){
			printf("%c won\n",cur);
			return;
		}
	}
	char cur=grille[0][0];
	if (cur!='.'){
		bool ok=true;
		for (int j=0;j<N;j++)
			if (cur=='T')
				cur=grille[j][j];
			else if (grille[j][j]!='T' && grille[j][j]!=cur)
				ok=false;
		if (ok && cur!='.'){
			printf("%c won\n",cur);
			return;
		}
	}
	cur=grille[N-1][0];
	if (cur!='.'){
		bool ok=true;
		for (int j=0;j<N;j++)
			if (cur=='T')
				cur=grille[N-1-j][j];
			else if (grille[N-1-j][j]!='T' && grille[N-1-j][j]!=cur)
				ok=false;
		if (ok && cur!='.'){
			printf("%c won\n",cur);
			return;
		}
	}
	for (int i=0;i<N;i++)
	for (int j=0;j<N;j++)
		if (grille[i][j]=='.'){
			printf("Game has not completed\n");
			return;
		}
	puts("Draw");
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		pb();
	}
	return 0;
}
