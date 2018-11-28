#include<cstdio>

int map[110][110];
int temp[110][110];
int n;

int process(){
	int cnt = 0;
	int i,j;
	int flag;
	while(true){
		for(i=1;i<=100;i++){
			for(j=1;j<=100;j++){
				temp[i][j] = map[i][j];
				if(i==1 && j==1) temp[i][j] = 0;
				else if(i==1){
					if(map[i][j] == 1 && map[i][j-1] == 0) temp[i][j] = 0;
				}
				else if(j==1){
					if(map[i][j] == 1 && map[i-1][j] == 0) temp[i][j] = 0;
				}
				else{
					if(map[i][j] == 1 && map[i-1][j] == 0 && map[i][j-1] == 0) temp[i][j] = 0;
					else if(map[i][j] == 0 && map[i-1][j] == 1 && map[i][j-1] == 1) temp[i][j] = 1;
				}
			}
		}
		flag = 0;
		for(i=1;i<=100;i++){
			for(j=1;j<=100;j++){
				map[i][j] = temp[i][j];
				if(temp[i][j] == 1) flag++;
			}
		}
		cnt++;
		if(flag == 0) break;
	}
	return cnt;
}

int main(void){
	int j,i,T;
	int ans;
	int x1,x2,y1,y2;
	int x,y;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++){
		fscanf(fin,"%d",&n);
		for(x=1;x<=100;x++){
			for(y=1;y<=100;y++){
				map[x][y] = 0;
			}
		}
		for(j=0;j<n;j++){
			fscanf(fin,"%d %d %d %d",&x1,&y1,&x2,&y2);
			for(x=x1;x<=x2;x++){
				for(y=y1;y<=y2;y++){
					map[x][y] = 1;
				}
			}
		}
		ans = process();
		fprintf(fout,"Case #%d: %d\n",i,ans);
	}
	fcloseall();
}