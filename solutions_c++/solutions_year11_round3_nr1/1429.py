#include <cstdio>
#include <algorithm>
#include <vector>


using namespace std;



int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d:\n", t);
		
        int R,C; scanf("%d %d\n", &R, &C);
        
        vector< vector<char> > tiles(R, vector<char>(C));
        
        for (int i=0; i<R; i++) scanf("%s", &tiles[i][0]);

        bool possible=true;
        
        int i,j;
        for (i=0; i<R; i++){
            for(j=0; j<C; j++)

                if(tiles[i][j]=='#' && i<R-1 && j<C-1 && tiles[i][j+1]=='#' && tiles[i+1][j]=='#' && tiles[i+1][j+1]=='#'){
                    tiles[i][j]='/';
                    tiles[i][j+1]='\\';
                    tiles[i+1][j]='\\';
                    tiles[i+1][j+1]='/';
                
                }else if(tiles[i][j]=='#'){
                    possible=false;
                    break;break;
                }
            
        }
                    
        if(!possible){
            printf("Impossible\n");
        }else{
            for (i=0; i<R; i++){
                for(j=0; j<C; j++) printf("%c",tiles[i][j]);
                printf("\n");
            }
        }
        
    }
            
	return 0;
}
