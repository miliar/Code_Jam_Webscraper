#include <cstdio>

char mat[15][15], mark[15][15];
int R,C;

int main(){
	
	int casos;
	int total;
	scanf("%d", &casos);
	
	for(int i = 1; i <= casos; i++){
		scanf("%d%d", &R, &C);
		
		for(int j = 0; j < R; j++)
			scanf("%s", mat[j]);
		
		total = 0;
		
		for(int j = 0; j < (1 << (R*C)); j++){
			for(int k = 0; k < R; k++){
				for(int l = 0; l < C; l++){
					mark[k][l] = 0;
				}
			}
			bool off =false;
			for(int k = 0; k < R; k++){
				for(int l = 0; l < C; l++){
					if(!mark[k][l]){
						int x,y;
						x = k;
						y = l;
						
						do{
							mark[x][y] = 1;
							if(mat[x][y] == '|'){
								if(	j&(1 << (x*C + y))){
									x--;
									if(x < 0)x += R;
								}else{
									x++;
									if(x == R)x = 0;
								}
							}else if(mat[x][y] == '-'){
								if(	j&(1 << (x*C + y))){
									y--;
									if(y < 0)y += C;
								}else{
									y++;
									if(y == C)y = 0;
								}
							}else if(mat[x][y] == '/'){
								if(	j&(1 << (x*C + y))){
									x--;
									if(x < 0)x += R;
									y++;
									if(y == C)y = 0;
								}else{
									x++;
									if(x == R)x = 0;
									y--;
									if(y < 0)y += C;
								}
							}else{
								if(	j&(1 << (x*C + y))){
									x--;
									if(x < 0)x += R;
									y--;
									if(y < 0)y += C;
								}else{
									x++;
									if(x == R)x = 0;
									y++;
									if(y == C)y = 0;
								}
							}
						}while(!mark[x][y]);
						if(x != k || y != l){
							off = true;
						}
					}
				}
			}
			if(!off){
				total++;
				total %= 1000003;
			}
		}
		printf("Case #%d: %d\n", i, total);
	}
	
	return 0;
}