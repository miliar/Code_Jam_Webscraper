#include<stdio.h>

bool f[100][100],t[100][100];

bool at(int x, int y){
	if(x>=0&&y>=0&&x<100&&y<100)return f[x][y];
	return 0;
}

int main()
{
	int c;
	scanf("%d",&c);
	for(int cc=1;cc<=c;cc++){
		for(int i=0;i<100;i++)
			for(int j=0;j<100;j++)
				f[i][j]=0;
		int r;
		scanf("%d",&r);
		for(int i=0;i<r;i++){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int j=x1-1;j<=x2-1;j++)
				for(int k=y1-1;k<=y2-1;k++)
					f[j][k]=1;
		}
		int count=1;
		bool find;
		do{
			find=0;
			for(int i=0;i<100;i++)
				for(int j=0;j<100;j++)
					t[i][j]=0;
			for(int i=0;i<100;i++)
				for(int j=0;j<100;j++){
					if(at(i,j)&&(at(i-1,j)||at(i,j-1))){
						t[i][j]=1;find=1;
					}
					if(!at(i,j)&&at(i-1,j)&&at(i,j-1)){
						t[i][j]=1;find=1;
					}
				}
			for(int i=0;i<100;i++)
				for(int j=0;j<100;j++)
					f[i][j]=t[i][j];
			if(find)count++;
		}while(find);
		printf("Case #%d: %d\n",cc, count);
	}
	return 0;
}
