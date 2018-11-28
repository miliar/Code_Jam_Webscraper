#include <stdio.h>
#include <queue>
#include <memory.h>

using namespace std;

typedef struct Point 
{
	int x,y;
}Point;
int n,m;
int my[4] = {0,-1,1,0};
int mx[4] = {-1,0,0,1};
int k;
int map[100][100];
int res[100][100];

bool check( int x, int y, int j )
{
	if ( x<0 || y<0 || x>=m || y>=n ) return false;
	int min=map[x][y],w=5;
	for ( int i=0; i<4; i++ ){
		if ( x+mx[i]>=0 && x+mx[i]<m && y+my[i]>=0 && y+my[i]<n ){
			if ( map[x+mx[i]][y+my[i]]<min ){
				w=i;
				min = map[x+mx[i]][y+my[i]];
			}
		}
	}
	if ( w == j) return true;
	return false;
}


bool check2( int x, int y, int j ){
	if ( x<0 || y<0 || x>=m || y>=n ) return false;
	if ( map[x+mx[j]][y+my[j]]>map[x][y] ) return true;
	return false;
}

int main () {
    FILE *fin  = fopen ("test.in", "r");
    FILE *fout = fopen ("test.out", "w");

//	freopen("test.in","r",stdin);
	int t,i,j;
    fscanf(fin,"%d",&t);
    for ( k=1; k<=t; k++ ){
    	
    	int state = 0;
    	fscanf(fin,"%d%d",&m,&n);
    	for ( i=0; i<m; i++ ){
    		for ( j=0; j<n; j++ ){
    			fscanf(fin,"%d",&map[i][j] );
    		}
    	}
   		memset( res, 0 ,sizeof(res) );
    	for ( i=0; i<m; i++ ){
    		for ( j=0; j<n; j++){
    			
				if ( res[i][j] ) continue;
				state++;
				queue<Point> q;			
				Point p,temp;
   			 	int x,y;
				p.x = i;
				p.y = j; 
				q.push(p); 
		 		res[i][j] = state;
   			 	while( q.size() ){
    				temp = q.front();
    				q.pop();
    				x = temp.x;
    				y = temp.y;
    				for ( int ii=0; ii<4; ii++ ){
    					if ( check( x+mx[ii],y+my[ii],3-ii )  ){
    						if ( res[x+mx[ii]][y+my[ii]] ) continue;
    						p.x = x+mx[ii];
    						p.y = y+my[ii];
    						q.push(p);
    						res[p.x][p.y] = state;
    					}
    				}
    				int min=1100000,w=5;
    				for ( int ii=0; ii<4; ii++ ){
    					if ( check2( x+mx[ii],y+my[ii],3-ii )  ){
    						if ( map[x+mx[ii]][y+my[ii]]<min ){
    							min = map[x+mx[ii]][y+my[ii]];
    							w = ii;
    						}
    					}
    				}
    				if ( w==5 ) continue;
    				if ( res[x+mx[w]][y+my[w]] ) continue;
   					p.x = x+mx[w];
   					p.y = y+my[w];
   					q.push(p);
   					res[p.x][p.y] = state;
   			 	}
   			 	
   			 	
    		}
    	}
    	fprintf(fout,"Case #%d:\n",k);
    	for ( i=0; i<m; i++ ){
    		for ( j=0; j<n-1; j++ ){
				fprintf(fout,"%c ",'a'+res[i][j]-1);
    		}
    		fprintf(fout,"%c\n",'a'+res[i][j]-1);
    	}
    }

   	return 0;
}

