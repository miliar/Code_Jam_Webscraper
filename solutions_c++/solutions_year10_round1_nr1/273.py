#include<cstdio>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

int n,k;
char map[50][50];
char rot[50][50];
int mov[2][8] = {	{-1,-1,-1,0,1,1,1,0},
					{-1,0,1,1,1,0,-1,-1}};

bool back(char color,int x,int y){
	int i,j;
	for(j=0;j<8;j++){
		int dx = mov[0][j] * (k-1), dy = mov[1][j] * (k-1);
		if(x + dx >= 0 && x + dx < n && y + dy >= 0 && y + dy < n){
			for(i=0;i<k;i++){
				if(rot[x+i*mov[0][j]][y+i*mov[1][j]] != color) break;
			}
			if(i == k) return true;
		}
	}
	return false;
}

int process(){
	int i,j,cnt;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			rot[i][j] = map[n-1-j][i];
		}
	}
	for(j=0;j<n;j++){
		cnt = n-1;
		for(i=n-1;i>=0;i--){
			if(rot[i][j] != '.'){
				rot[cnt][j] = rot[i][j];
				if(i != cnt) rot[i][j] = '.';
				cnt--;
			}
			if(cnt < 0) break;
		}
	}
	bool blue=false,red=false;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			if(rot[i][j] != '.'){
				if(back(rot[i][j],i,j)){
					if(rot[i][j] == 'B') blue = true;
					else if(rot[i][j] == 'R') red = true;
				}
			}
		}
	}
	if(blue && red) return 0;
	else if(blue) return 1;
	else if(red) return 2;
	else return 3;
}

int main(void){
	int i,j,T;
	int ans;
	string temp;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++){
		fscanf(fin,"%d%d",&n,&k);
		for(j=0;j<n;j++){
			fscanf(fin,"%s",map[j]);
		}
		ans = process();
		if(ans == 0) fprintf(fout,"Case #%d: Both\n",i);
		else if(ans == 1) fprintf(fout,"Case #%d: Blue\n",i);
		else if(ans == 2) fprintf(fout,"Case #%d: Red\n",i);
		else fprintf(fout,"Case #%d: Neither\n",i);
	}
	fcloseall();
	return 0;
}