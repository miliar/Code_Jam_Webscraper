#include<cstdio>
#include<cstdlib>
#include<iostream>
using namespace std;

struct node {
	int x , y ; 
};
node temp[1000];
int Map[105][105];
int main(){
	freopen("G:\\C-small-attempt0.in","r",stdin);
	freopen("G:\\C-small-attempt0.out","w",stdout);
	int t ; 
	int cases = 1;
	scanf("%d",&t);
	while(t--){
		int R ; 
		scanf("%d",&R);
		memset(Map,0,sizeof(Map));
		int Minx =  -1 , Miny = -1;
		int res = 0 ;
		for(int i = 0 ; i<R;++i){
			int x1 , x2 ,y1 , y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			if( x1 > x2 ){int tx = x1 ; x1 =x2 ; x2=tx;}
			if( y1 > y2 ){int ty = y1;y1= y2;y2 = ty ;}

			if( Minx == -1 || Minx < x1 )Minx = x1;
			if( Miny == -1 || Miny <y1 )Miny = y1;
			if( Minx == -1 || Minx < x2 )Minx = x2;
			if( Miny == -1 || Miny <y2 )Miny = y2;
			for(int j = x1;j<=x2;++j)
				for(int k = y1;k<=y2;++k){
					if( Map[j][k] == 0 )
					{
						Map[j][k] = 1;
						res++;
					}
				}
		}
		int years =0 ;
		while(res> 0 ){
			years++ ;
			int cnt = 0 ;
			for(int i = 0 ; i<=Minx ; ++i)
				for(int j = 0 ; j<=Miny;++j){
					if( Map[i][j] == 1){
						int ty = j-1,tx = i-1;
						if( tx >=0 && ty >=0 && Map[i][ty] ==0 && Map[tx][j] ==0 ){
							temp[cnt].x = i ;temp[cnt++].y = j ;
						}
					}
					else if( Map[i][j] == 0 ){
						int ty = j-1,tx = i-1;
						if( tx >=0 && ty >=0 && Map[i][ty] ==1 && Map[tx][j] ==1 ){
							temp[cnt].x = i ;temp[cnt++].y = j ;
						}
					}
				}
				for(int i = 0 ; i<cnt;++i){
					int x = temp[i].x , y = temp[i].y ;
					if( Map[x][y] == 1 ){
						res--;
						Map[x][y] = 0 ;
					}
					else{
						res++;
						Map[x][y] = 1;
					}
				}
		}
		printf("Case #%d: %d\n",cases++,years);
	}
	return 0 ;
}