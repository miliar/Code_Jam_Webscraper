#include <iostream>
#include <queue>

using namespace std;

int z,x,y,st,zz;

int grid[110][110][5][110];
queue<pair<int, int> > kju;

void flood(int xx, int yy, int col){
  int s,t;
  kju.push(make_pair(xx,yy));
  
  grid[xx][yy][2][zz] = col;
  
  while(!kju.empty()){
    xx = kju.front().first;
    yy = kju.front().second;
    kju.pop();
    
    s = grid[xx][yy][1][zz];
    if(s > 0){
      if(s == 1){
	if(grid[xx][yy-1][2][zz] == 0){
	  kju.push(make_pair(xx,yy-1));
	  grid[xx][yy-1][2][zz] = col;
	}
      } else if(s == 2){
	if(grid[xx-1][yy][2][zz] == 0){
	  kju.push(make_pair(xx-1,yy));
	  grid[xx-1][yy][2][zz] = col;
	}
      } else if(s == 3){
	if(grid[xx+1][yy][2][zz] == 0){
	  kju.push(make_pair(xx+1,yy));
	  grid[xx+1][yy][2][zz] = col;
	}
      } else if(s == 4){
	if(grid[xx][yy+1][2][zz] == 0){
	  kju.push(make_pair(xx,yy+1));
	  grid[xx][yy+1][2][zz] = col;
	}
      }
    }
    
    if(yy-1 >= 0 && grid[xx][yy-1][1][zz]==4){
      if(grid[xx][yy-1][2][zz] == 0){
	  kju.push(make_pair(xx,yy-1));
	  grid[xx][yy-1][2][zz] = col;
	}
    }
    if(xx-1 >= 0 && grid[xx-1][yy][1][zz]==3){
      if(grid[xx-1][yy][2][zz] == 0){
	  kju.push(make_pair(xx-1,yy));
	  grid[xx-1][yy][2][zz] = col;
	}
    }
    if(xx+1 < x && grid[xx+1][yy][1][zz]==2){
      if(grid[xx+1][yy][2][zz] == 0){
	  kju.push(make_pair(xx+1,yy));
	  grid[xx+1][yy][2][zz] = col;
	}
    }
    if(yy+1 < y && grid[xx][yy+1][1][zz]==1){
      if(grid[xx][yy+1][2][zz] == 0){
	  kju.push(make_pair(xx,yy+1));
	  grid[xx][yy+1][2][zz] = col;
	}
    }
    
  }
  
}

int main(){
  
  scanf("%d", &z);
  for(zz=0;zz<z;zz++){
    
    scanf("%d %d", &y, &x);
    
    for(int j=0;j<y;j++)
      for(int i=0;i<x;i++){
	scanf("%d", &grid[i][j][0][zz]);
      }

      
    for(int j=0;j<y;j++)
      for(int i=0;i<x;i++){
	
	st = 10001;
	if(j-1 >= 0) st = min(st,grid[i][j-1][0][zz]);
	if(j+1 < y) st = min(st,grid[i][j+1][0][zz]);
	if(i-1 >= 0) st = min(st,grid[i-1][j][0][zz]);
	if(i+1 < x) st = min(st,grid[i+1][j][0][zz]);
	
	if(grid[i][j][0][zz]<=st) continue;
	
	


	
	if(j-1 >= 0 && grid[i][j-1][0][zz]==st){
	  grid[i][j][1][zz] = 1;
	} else if(i-1 >= 0 && grid[i-1][j][0][zz]==st){
	  grid[i][j][1][zz] = 2;
	} else if(i+1 < x && grid[i+1][j][0][zz]==st){
	  grid[i][j][1][zz] = 3;
	} else if(j+1 < y && grid[i][j+1][0][zz]==st){
	  grid[i][j][1][zz] = 4;
	}

      }
            
    //flood
    
    int color;
    char cou;
    
    color = 1;
    
    for(int j=0;j<y;j++)
      for(int i=0;i<x;i++){
	if(grid[i][j][2][zz] == 0) {
	  flood(i,j,color);
	  color++;
	}
      }
      
     
     printf("Case #%d:\n",zz+1);
      
     for(int j=0;j<y;j++){
       for(int i=0;i<x;i++){
// 	 cou = grid[i][j][2]+96;
	 printf("%c", grid[i][j][2][zz]+96);
	 if(i<x-1) printf(" ");
       }
       printf("\n");
     }
    
  }
  
  
  return 0;
}