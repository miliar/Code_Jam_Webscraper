# include <stdio.h>
# include <string.h>
# include <queue>
# define INF 0x3f3f3f3f
# define MAX 128
using namespace std;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
queue<int> fila;
int n, w, h;
char label[MAX][MAX];
int tab[MAX][MAX];
char atual;
void rotula(int X, int Y){
	//printf("%d %d\n", X, Y);
	int i, j,i1,j1, menor, k, cx, cy;
	i = X;
	j = Y;
	fila.push(i);
	fila.push(j);
	while(1){
		//printf("%d %d\n",i , j);
		menor = tab[i][j];
		for(k=0;k<4;k++){
			i1 = i+dx[k];
			 j1 = j+dy[k];
			if(tab[i1][j1] < menor){
				menor = tab[i1][j1];
				cx = i1;
				cy = j1;
			}
		}
		if(menor == tab[i][j]) break;
		fila.push(cx);
		fila.push(cy);
		i = cx;
		j = cy;
	}
	if(label[i][j] == 'A'){
		//printf("|%d %d|\n", i, j);
		label[i][j] = atual++;
	}
	while(!fila.empty()){
		i1 = fila.front();
		fila.pop();
		j1 = fila.front();
		fila.pop();
		label[i1][j1] = label[i][j];
	}
	
}

int main (void){
	int i, j, k;
	int teste = 1;
	scanf("%d", &n);
	while(n--){
		scanf("%d%d", &w, &h);
		memset(tab, INF, sizeof(tab));
		memset(label, 'A', sizeof(label));
		for(i=1;i<=w;i++){
			for(j=1;j<=h;j++){
				scanf("%d", &tab[i][j]);
			}
		}
		atual = 'a';
		for(i=1;i<=w;i++){
			for(j=1;j<=h;j++){
				rotula(i,j);
				//puts("saí");
			}
		}
		printf("Case #%d:\n", teste++);
		for(i=1;i<=w;i++){
			for(j=1;j<=h;j++){
				if(j==1)
				printf("%c", label[i][j]);
				else printf(" %c", label[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}