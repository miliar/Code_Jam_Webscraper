#include <iostream>
#include <algorithm>

//accepted
using namespace std;
int main(){
	FILE *f = fopen("out.txt", "w");
	int T = 0, c = 0;
	cin >> T;
	while(c++ < T){
		int x = 0, y = 0;
		cin >> x >> y;
		char tile[x][y];
		for(int i = 0; i < x; i++)
			fill_n(tile[i], y, '.');
		for(int i = 0; i < x; i++)
			for(int j = 0; j < y; j++)
				cin >> tile[i][j];
		bool go = true;
		for(int i = 0; i < x && go; i++){
			for(int j = 0; j < y && go; j++){
				if(tile[i][j] == '#'){
					tile[i][j] = '/';
					if((j + 1) < y && tile[i][j+1] == '#')
						tile[i][j+1] = '\\';
					else
						go = false;
					if(go && (i+1) < x && tile[i+1][j] == '#')
						tile[i+1][j] = '\\';
					else
						go = false;
					if(go && tile[i+1][j+1] == '#')
						tile[i+1][j+1] = '/';
					else
						go = false;
				}
			}	
		}
		if(go){
			printf("Case #%d:\n", c);
			fprintf(f, "Case #%d:\n", c);
			for(int i = 0; i < x; i++){
				for(int j = 0; j < y; j++){
					printf("%c", tile[i][j]);
					fprintf(f, "%c", tile[i][j]);
				}
				printf("\n");
				fprintf(f, "\n");
			}
		}else{
			printf("Case #%d:\nImpossible\n", c);
			fprintf(f, "Case #%d:\nImpossible\n", c);
		}
	}
	return 0;
}