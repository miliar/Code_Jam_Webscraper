#include<stdio.h>

#define MAXN 100
#define MAXQ 10000

FILE *fs = fopen("input.txt","rt");
FILE *fp = fopen("output.txt","wt");

int T;
int n,m;

int data[MAXN+1][MAXN+1];
int check[MAXN+1][MAXN+1];
int sink[MAXN+1][MAXN+1][2];
int queue[MAXQ+1][2],head,tail;

char sinkname[MAXN+1][MAXN+1];

int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

void bfs(int x,int y)
{
	int k;
	int px,py,min,mink;
	int sx,sy;

	head = tail = 0;
	if(check[x][y]) return;
	queue[tail][0] = x;
	queue[tail][1] = y;
	check[x][y] = 1;
	tail++;

	while(head != tail){
		px = queue[head][0];
		py = queue[head][1];

		min = data[px][py];
		for(k=0;k<4;k++){
			if(1<=px+move[k][0]  && px+move[k][0]<=n){
				if(1<=py+move[k][1] && py+move[k][1]<=m){
					if(min > data[px+move[k][0]][py+move[k][1]]){
						min = data[px+move[k][0]][py+move[k][1]];
						mink = k;						
					}
				}
			}
		}
		k = mink;
		if(min == data[px][py]){
			sx = px;
			sy = py;
			break;
		}
		if(!check[px+move[k][0]][py+move[k][1]]){
			queue[tail][0] = px+move[k][0];
			queue[tail][1] = py+move[k][1];
			tail++;
			check[px+move[k][0]][py+move[k][1]];
		}
		else{
			sx = sink[px+move[k][0]][py+move[k][1]][0];
			sy = sink[px+move[k][0]][py+move[k][1]][1];
		}
		
		head++;		
	}

	for(k=0;k<tail;k++){
		sink[queue[k][0]][queue[k][1]][0] = sx;
		sink[queue[k][0]][queue[k][1]][1] = sy;
	}
}


int main()
{
	int i,j,k;
	char t;

	fscanf(fs,"%d",&T);
	for(i=1;i<=T;i++){
		fscanf(fs,"%d %d",&n,&m);
		for(j=1;j<=n;j++){
			for(k=1;k<=m;k++){
				fscanf(fs,"%d",&data[j][k]);
				check[j][k] = 0;
				sink[j][k][0] = sink[j][k][1] = 0;
				sinkname[j][k] = 0;
			}
		}		

		for(j=1;j<=n;j++){
			for(k=1;k<=m;k++){
				bfs(j,k);
			}
		}

		fprintf(fp,"Case #%d:\n",i);
		t = 'a';
		for(j=1;j<=n;j++){
			for(k=1;k<=m;k++){
				if(!sinkname[sink[j][k][0]][sink[j][k][1]]){
					sinkname[sink[j][k][0]][sink[j][k][1]] = t++;
				}
				fprintf(fp,"%c ",sinkname[sink[j][k][0]][sink[j][k][1]]);
			}
			fprintf(fp,"\n");
		}
	}
	
	return 0;
}

