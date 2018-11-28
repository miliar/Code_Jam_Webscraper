/*
	Watersheds
*/
#include <fstream.h>
#define MAX 105
#define INF 1000000000
#define NORTH 0
#define WEST 1
#define EAST 2
#define SOUTH 3
int ntest,width,height;
int table[MAX][MAX];
int isfree[MAX][MAX];
char outtab[MAX][MAX];
int queue[MAX*MAX];
int bottom,top;
void push(int i, int j);
void pop(int &i,int &j);
int findmin(int a,int b,int &di,int &dj);
bool isempty();
ifstream fin("input");
ofstream fout("output");
main() {
	fin>>ntest;
	for (int count=1;count<=ntest;++count) {
		fin>>height>>width;
		for (int i=1;i<=height;++i) {
			for (int j=1;j<=width;++j) {
				fin>>table[i][j];
				isfree[i][j]=1;			
			}
		}
		//bfs
		char temp='a';		
		for (int i=1;i<=height;++i) {
			for (int j=1;j<=width;++j) {
				if (isfree[i][j]==1) {
					top=0;
					bottom=1;					
					push(i,j);
					isfree[i][j]=0;
					outtab[i][j]=temp;
					do {
						int a,b;
						int direction[4];
						if (isempty()) {
							break;
						}
						pop(a,b);
						//forward
						int di,dj;
						if (findmin(a,b,di,dj)<INF) {
							if (isfree[di][dj]==1
								&&table[di][dj]<table[a][b]) {
								push(di,dj);
								isfree[di][dj]=0;
								outtab[di][dj]=temp;							
							}
						}
						//backward
						if (a>1&&isfree[a-1][b]==1)
							if (findmin(a-1,b,di,dj)==table[a][b]
								&&di==a&&dj==b
								&&table[a][b]<table[a-1][b]) {
								push(a-1,b);
								isfree[a-1][b]=0;
								outtab[a-1][b]=temp;
							}
						if (a<height&&isfree[a+1][b]==1)
							if (findmin(a+1,b,di,dj)==table[a][b]
								&&di==a&&dj==b
								&&table[a][b]<table[a+1][b]) {
								push(a+1,b);
								isfree[a+1][b]=0;
								outtab[a+1][b]=temp;
							}
						if (b>1&&isfree[a][b-1]==1)
							if (findmin(a,b-1,di,dj)==table[a][b]
								&&di==a&&dj==b
								&&table[a][b]<table[a][b-1]) {
								push(a,b-1);
								isfree[a][b-1]=0;
								outtab[a][b-1]=temp;
							}
						if (b<width&&isfree[a][b+1]==1)
							if (findmin(a,b+1,di,dj)==table[a][b]
								&&di==a&&dj==b
								&&table[a][b]<table[a][b+1]) {
								push(a,b+1);
								isfree[a][b+1]=0;
								outtab[a][b+1]=temp;
							}
					}while(1);
					++temp;
				}
			}
		}
		fout<<"Case #"<<count<<":\n";
		for (int i=1;i<=height;++i) {
			for (int j=1;j<=width;++j) {
				fout<<outtab[i][j];
				if (j==width) fout<<"\n";
				else fout<<" ";
			}
		}
	}
	return 0;
}
void push(int i, int j) {
	queue[++top]=i;
	queue[++top]=j;
}
void pop(int &i,int &j) {
	i=queue[bottom++];
	j=queue[bottom++];
}
bool isempty() {
	if (bottom>=top)
		return true;
	else 
		return false;
}
int findmin(int a,int b,int &di,int &dj) {
	int direction[4];
	for (int i=0;i<4;++i) {
		direction[i]=INF;
	}
	if (a>1) direction[NORTH]=table[a-1][b];
	if (a<height) direction[SOUTH]=table[a+1][b];
	if (b>1) direction[WEST]=table[a][b-1];
	if (b<width) direction[EAST]=table[a][b+1];
	int min=INF;
	if (direction[NORTH]<min) {
		min=table[a-1][b];
		di=a-1;dj=b;
	}
	if (direction[WEST]<min) {
		min=table[a][b-1];
		di=a;dj=b-1;
	}
	if (direction[EAST]<min) {
		min=table[a][b+1];
		di=a;dj=b+1;
	}
	if (direction[SOUTH]<min) {
		min=table[a+1][b];
		di=a+1;dj=b;
	}
	return min;
}
