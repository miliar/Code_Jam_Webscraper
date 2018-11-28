#include <iostream>
using namespace std;

#define SIZE 100+10
#define INF 99999999

int T,H,W,map[SIZE][SIZE];
char label[SIZE][SIZE],letter[]="abcdefghijklmnopqrstuvwxyz";
int delx[]={-1,0,0,+1};
int dely[]={0,-1,+1,0};

void init(int h,int w)
{
    memset(label,0,sizeof(label));
	int i,j;
	for(i=0;i<=w+1;i++){
		map[0][i] = INF;
		label[0][i] = '*';
	}
	for(i=0;i<=w+1;i++){
		map[h+1][i] = INF;
		label[h+1][i] = '*';
	}
	for(i=0;i<=h+1;i++){
		map[i][0] = INF;
		label[i][0] = '*';
	}
	for(i=0;i<=h+1;i++){
		map[i][w+1] = INF;
		label[i][w+1] = '*';
	}
		
	
}

int findmin(int r,int c,int& tr,int& tc)
{
	int i,min=INF,cr,cc;
	for(i=0;i<4;i++)
	{
		cr = r+delx[i];
		cc = c+dely[i];
		if(map[cr][cc]<min){
			min = map[cr][cc];
			tr=cr;
			tc=cc;
		}
	}
	return min;
}

void makelabel(int r,int c)
{
	//printf("calling makelabel(%d,%d)...\n",r,c);
	int i,j,cr,cc,tr,tc,min;

	min = findmin(r,c,tr,tc);
	if(min < map[r][c])
	{
		if(label[tr][tc]!=label[r][c]){
			label[tr][tc] = label[r][c];
			//printf("inner min:%d\n",min);
			makelabel(tr,tc);
		}
	}
	for(i=0;i<4;i++)
	{
		cr = r+delx[i];
		cc = c+dely[i];
		//printf("label(%d,%d): %d\n",cr,cc,label[cr][cc]);
		if(label[cr][cc])
			continue;
		
		min=findmin(cr,cc,tr,tc);
		//printf("outer min:%d\n",min);
		if(min<map[cr][cc] && min==map[r][c] && min!=map[cr][cc] && r==tr && c==tc)
		{
			label[cr][cc] = label[r][c];
			//printf("label(%d,%d): %c\n",cr,cc,label[cr][cc]);
			makelabel(cr,cc);
		}
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,t,cl;
	//secure boundary
	for(i=0;i<SIZE;i++)
		map[0][i] = INF;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		//INPUT
		scanf("%d %d",&H,&W);
		init(H,W);
		
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
				scanf("%d",&map[i][j]);
		
		/*
		//debug-print the map
		printf("label: \n");
		for(i=0;i<=H+1;i++){
			for(j=0;j<=W+1;j++){
				if(j!=0)
					printf(" ");
				printf("%d",label[i][j]);
			}
			printf("\n");
		}
		*/
	
		//PROCESS
		cl=0;
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++)
				if(!label[i][j]){
					label[i][j]=letter[cl++];
					makelabel(i,j);
				}
		
		//OUTPUT
		printf("Case #%d:\n",t);
		//print the labeled-map
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				if(j!=1)
					printf(" ");
				printf("%c",label[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
