#include <iostream>

using namespace std;

bool a[1000][1000];

int main(){
	int t;
	scanf("%d",&t);
	int size = 300;
	for(int f=1;f<=t;f++){
		for(int i=0;i<=size;i++)
			for(int j=0;j<=size;j++)
				a[i][j] = false;
		int r;
		scanf("%d",&r);
		int x1,x2,y1,y2;
		for(int k=0;k<r;k++){
			scanf("%d%d%d%d",&x1,&y1, &x2, &y2);
			int tmp;
			if(x1>x2){tmp = x1; x1 = x2; x2= tmp;}
			if(y1>y2){tmp = y1; y1 = y2; y2 = tmp;}
			for(int i=x1;i<=x2;i++)
				for(int j=y1;j<=y2;j++)
					a[i][j] = true;
		}
		int k=0;
		//printf("!!!%d\n",r);
		bool b = (r!=0);
		for(;r!=0;){
			k++;
			r=0;
			for(int x=size;x>0;x--)
				for( int y=size;y>0;y--){
					if(a[x-1][y] && a[x][y-1]) a[x][y] = true;
					if(!(a[x-1][y] || a[x][y-1])) a[x][y] = false;
					if(a[x][y]) r++;
				}
		}
		printf("Case #%d: %d\n",f,k);
	}
	return 0;
}
