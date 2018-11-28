#include<cstdio>
int Z,z,H,W,a[105][105],i,j;
char c[105][105],q;

char D(int x,int y){
	if (c[x][y]!='!') return c[x][y];
	
	int low=a[x][y],f=0;
	
	if (x-1>=1 && a[x-1][y]<low){
		low = a[x-1][y];
		f = 1;
	}
	
	if (y-1>=1 && a[x][y-1]<low){
		low = a[x][y-1];
		f = 2;
	}
	if (y+1<=W && a[x][y+1]<low){
		low = a[x][y+1];
		f = 3;
	}
	if (x+1<=H && a[x+1][y]<low){
		low = a[x+1][y];
		f = 4;
	}
	if (f==0){
		c[x][y] = q;
		++q;
		return c[x][y];
	}else if (f==1) return c[x][y]=D(x-1,y);
	else if (f==2) return c[x][y]=D(x,y-1);
	else if (f==3) return c[x][y]=D(x,y+1);
	else if (f==4) return c[x][y]=D(x+1,y);
	
}


int main(){
	scanf("%d",&Z);
	for (z=1;z<=Z;++z){
		scanf("%d%d",&H,&W);
		
		q = 'a';
		
		for (i=1;i<=H;++i){
			for (j=1;j<=W;++j){
				scanf("%d",&a[i][j]);
				c[i][j] = '!';
			}
		}
		printf("Case #%d:\n",z);
		for (i=1;i<=H;++i){
			for (j=1;j<=W;++j){
				D(i,j);
				printf("%c",c[i][j]);
				if (j!=W) printf(" ");
				else printf("\n");
			}
		}
		
		
	}

	return 0;
}
