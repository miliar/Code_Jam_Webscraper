#include <cstdio>
#include <cstring>

const int MAXN = 55;

int n,k;
char tab[MAXN][MAXN];

int dx[] = {-1,0,1,0,1,1,-1,-1};
int dy[] = {0,1,0,-1,1,-1,1,-1};

bool check(char c){
    for(int i=0;i<n;++i){
	for(int j=0;j<n;++j){
	    if(tab[i][j] != c){
		continue;
	    }
	    for(int d=0;d<8;++d){
		int x = i;
		int y = j;
		
		int h;
		for(h=0;h<k;++h){
		    if(x < 0 || x >= n) break;
		    if(y < 0 || y >= n) break;
		    if(tab[x][y] != c){
			break;
		    }
		    x += dx[d];
		    y += dy[d];
		}
		
		if(h == k){
		    return true;
		}
	    }
	}
    }
    
    return false;
}

int main(){
    int t;
    scanf("%d",&t);
    
    for(int lp=1;lp<=t;++lp){
	scanf("%d %d",&n,&k);
	for(int i=0;i<n;++i){
	    scanf("%s",tab[i]);
	}
	
	for(int i=0;i<n;++i){
	    int p = n-1;
	    for(int j=n-1;j>=0;--j){
		if(tab[i][j] != '.'){
		    if(j != p){
			tab[i][p] = tab[i][j];
			tab[i][j] = '.';
		    }
		    --p;
		}
	    }
	    //printf("%s\n",tab[i]);
	}
	
	
	bool b = check('B');
	bool r = check('R');
	
	printf("Case #%d: ",lp);
	
	if(b && r){
	    printf("Both\n");
	}
	else if(b){
	    printf("Blue\n");
	}
	else if(r){
	    printf("Red\n");
	}
	else{
	    printf("Neither\n");
	}
	
    }
    
    return 0;
}