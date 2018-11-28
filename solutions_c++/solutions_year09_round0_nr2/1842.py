#include <algorithm>
#include <deque>
#include <iostream>
#include <functional>
#include <string>
#include <math.h>
#include <ctype.h>

using namespace std;

char MAP[100][100];
int INPUT[100][100];
int H,W;
int charset[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
int charcount;

void initMAPS(){
	int i,j;
	for(i=0;i<H;i++)
		for(j=0;j<W;j++)
			MAP[i][j] = '\0';
}

void check(int x,int y){
	
	int max = 0;
	char d = 'X';
	int tmp;
	
	if(y > 0){
		tmp = INPUT[y][x] - INPUT[y-1][x];
		if(max < tmp){
			max = tmp;
			d = 'N';
		}
	}
	
	if(x > 0){
		tmp = INPUT[y][x] - INPUT[y][x-1];
		if(max < tmp){
			max = tmp;
			d = 'W';
		}
	}

	if(x < W - 1){
		tmp = INPUT[y][x] - INPUT[y][x+1];
		if(max < tmp){
			max = tmp;
			d = 'E';
		}
	}

	if(y < H - 1){
		tmp = INPUT[y][x] - INPUT[y+1][x];
		if(max < tmp){
			d = 'S';
		}
	}

	MAP[y][x] = d;
}

void makeResult(int x,int y,char D){
	
	if(y > 0){
		if(MAP[y-1][x] == 'S'){
			MAP[y-1][x] = D;
			makeResult(x,y-1,D);
		}
	}
	
	if(x > 0){
		if(MAP[y][x-1] == 'E'){
			MAP[y][x-1] = D;
			makeResult(x-1,y,D);
		}
	}
	
	if(x < W - 1){
		if(MAP[y][x+1] == 'W'){
			MAP[y][x+1] = D;
			makeResult(x+1,y,D);
		}
	}
	
	if(y < H - 1){
		if(MAP[y+1][x] == 'N'){
			MAP[y+1][x] = D;
			makeResult(x,y+1,D);
		}
	}
	
	switch(MAP[y][x]){
		case 'S':
			makeResult(x,y+1,D);
			break;
		case 'E':
			makeResult(x+1,y,D);
			break;
		case 'W':
			makeResult(x-1,y,D);
			break;
		case 'N':
			makeResult(x,y-1,D);
			break;
		default:
			break;
	}
	
	MAP[y][x] = D;
	
}
	
void calc(){

	int i,j;
	
	for(i=0;i<H;i++)
		for(j=0;j<W;j++)
			check(j,i);
		/*
		for(i=0;i<H;i++){
			for(j=0;j<W;j++)
				cout << MAP[i][j] << " ";
			cout << endl;
		}
		*/

	for(i=0;i<H;i++)
		for(j=0;j<W;j++)
			if(isupper(MAP[i][j])){
				makeResult(j,i,charset[charcount]);
				charcount++;
			}

}


int main(int argc, char* argv[]){
	
	int loop;
	int count = 0;
	int i,j;

	cin >> loop;

	while(loop--){
	
		cin >> H >> W;

		charcount = 0;

		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				cin >> INPUT[i][j];
		/*
		for(i=0;i<H;i++){
			for(j=0;j<W;j++)
				cout << INPUT[i][j] << " ";
			cout << endl;
		}
		*/

		calc();

		//out
		count++;
		cout << "Case #" << count << ": " << endl;
		for(i=0;i<H;i++){
			for(j=0;j<W;j++)
				cout << MAP[i][j] << " ";
			cout << endl;
		}

	}

	return 0;
	
}