#include<cstdio>
#include<iostream>
using namespace std;


int f(int a,int b,int c,int d){
	int sum = a + b+ c +d;
	if(sum == 3|| sum == 4)	return 1;
	if(sum == -3 || sum == -4)	return -1;
	return 0;
}
void process(){
	char map[5][5];
	int m[4][4];
	for(int i=0;i<4;i++)
		cin >> map[i];
	int sum = 0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++){
			if(map[i][j]=='T')
				m[i][j]=0;
			if(map[i][j]=='X')
				m[i][j] = 1;
			if(map[i][j]=='O')
				m[i][j] = -1;
			if(map[i][j] =='.'){
				m[i][j] = 100;
				sum++;
			}
		}
	int sw = 0;
	sw = f(m[0][0],m[1][1],m[2][2],m[3][3]);
	if(!sw) sw = f(m[0][3],m[1][2],m[2][1],m[3][0]);
	for(int i=0;i<4 && (!sw);i++)
		sw = f(m[i][0],m[i][1],m[i][2],m[i][3]);
	for(int i=0;i<4 && (!sw);i++)
		sw = f(m[0][i],m[1][i],m[2][i],m[3][i]);
	if(sw==1)
		printf("X won\n");
	else if(sw == -1)
		printf("O won\n");
	else{
		if(sum)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
}
int main(){
	int c;cin >> c;
	for(int i=1;i<=c;i++){
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}
