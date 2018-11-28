#include <iostream>
using namespace std;

int dh[] = {0,-1, 0,0,1};
int dw[] = {0,0,-1,1,0};
char dir[] = {'.', 'n', 'w','e','s'};

int main(){
	int n;
	cin >> n;
	for(int f=1;f<=n;f++){
		int h,w;
		cin >> h >> w;
		int a[105][105], c[105][105],e[105][105];
		for(int i=0;i<105;i++) for(int j=0;j<105;j++) {a[i][j] = 999999; c[i][j]=-1;}
		for(int x = 1;x<=h;x++)
			for(int y=1;y<=w;y++)
				cin >> a[x][y];
		for(int x=1;x<=h;x++)
			for(int y = 1;y<=w ; y++){
				e[x][y]=0;
				for(int z = 1;z<5;z++){
					if(a[x+dh[e[x][y]]][y+dw[e[x][y]]] > a[x+dh[z]][y+dw[z]])
						e[x][y]=z;
				}
			}
		/*
		for(int x=1;x<=h;x++){
			for(int y=1;y<=h;y++)
				cout << dir[e[x][y]] << " ";
			cout<<endl;
		}
		*/
		int com = -1;
		for(int x=1;x<=h;x++)
			for(int y=1;y<=w;y++)
				if(c[x][y]==-1){
					//cout<<x <<" " << y<<endl;
					int q[10005][2];
					int st,en;
					st=en=0;
					q[0][0] = x;
					q[0][1] = y;
					com++;
					c[x][y] = com;
					en++;
					while(st<en){
						int hh,ww;
						hh = q[st][0];
						ww = q[st][1];
						if(e[hh][ww] >0 && c[hh+dh[e[hh][ww]]][ww+dw[e[hh][ww]]]==-1){
							q[en][0] = hh+dh[e[hh][ww]];
							q[en][1]= ww+dw[e[hh][ww]];
							c[q[en][0]][q[en][1]] = com;
							en++;
						}
						for(int k=1;k<5;k++){
							if(e[hh+dh[k]][ww+dw[k]] == 5-k){
								q[en][0] = hh+dh[k];
								q[en][1] = ww+dw[k];
								c[q[en][0]][q[en][1]] = com;
								en++;								
							}
						}
						st++;
					}
				}
		printf("Case #%d:\n",f);
		
		for(int x=1;x<=h;x++){
			printf("%c",'a'+c[x][1]);
			for(int y=2;y<=w;y++)
				printf(" %c",'a'+c[x][y]);
			printf("\n");
		}
	}
	return 0;
}
