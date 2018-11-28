#include <stdio.h>

int blue=0;
char tiles[500][500];
bool solve(){
	int r,c,i,j;
	blue=0;
	scanf("%d %d", &r, &c);
	for(i=0;i<r;i++){
		scanf("%s", tiles[i]);
		for(j=0;j<c;j++)
			if(tiles[i][j] == '#')
				blue++;
	}
	if(blue%4!=0)
		return false;
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			if(tiles[i][j] == '#'){
				tiles[i][j] = '/';

				if(j+1 == c)			return false;
				if(tiles[i][j+1]!='#')	return false;
				tiles[i][j+1] = '\\';

				if(i+1 == r)			return false;
				if(tiles[i+1][j]!='#') 	return false;
				tiles[i+1][j] = '\\';

				if(tiles[i+1][j+1]!='#') return false;
				tiles[i+1][j+1] = '/';

				blue -= 4;
			}
		}
	}
	if(blue > 0)
		return false;
	for(i=0;i<r;i++)
		printf("%s\n", tiles[i]);
	return true;
}
int main(){
	int i, T;
	scanf("%d", &T);
	for(i=0;i<T;i++){
		printf("Case #%d: \n", i+1);
		if(!solve())
			printf("Impossible\n");
	}
	return 0;
}
