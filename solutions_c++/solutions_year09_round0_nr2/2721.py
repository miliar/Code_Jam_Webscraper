#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef unsigned long long uint64;

int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
int H,W;
int M[102][102] = {20000};
char Label[102][102] = {0};

void findBasin(int y, int x, char l, int&by, int &bx){
	int index = -1;
	int v;
	v = M[y][x];
	for(int i =0; i < 4; i++)
		if (!Label[y+dy[i]][x+dx[i]] && v > M[y+dy[i]][x+dx[i]]){
			v = M[y+dy[i]][x+dx[i]];
			index = i;
		}

	if (index!=-1){
		Label[y+dy[index]][x+dx[index]]=l;
		findBasin(y+dy[index], x+dx[index], l, by, bx);
	}
	else{
		by = y;
		bx = x;
	}	
}

void printLabel(){
	for (int y=1;y<=H;y++){
		for (int x=1;x<=W;x++)
			cout<<Label[y][x]<<" ";
			cout<< endl;
	}
}

void lableFromBasin(int by, int bx, char l){

	int tx, ty;
	int index, v;
	for(int d=0; d<4; d++){
		tx = bx+dx[d];
		ty = by+dy[d];
		if (!Label[ty][tx] || Label[ty][tx]==l){
			index = -1;
			v = M[ty][tx];
			for(int i =0; i < 4; i++)
				if (v > M[ty+dy[i]][tx+dx[i]]){
					v = M[ty+dy[i]][tx+dx[i]];
					index = i;
				}
		
			if(index != -1 && dx[index]==-1*dx[d] && dy[index] == -1*dy[d]){
				Label[ty][tx] = l;
				lableFromBasin(ty, tx, l);
			}
		}
	}
}


int main() {

	int T,x,y,c;		
	int bx, by;
	char l;


	cin>>T;	
	for (c=1; c<=T; c++){

		memset((int*)M, 20000,102*102);
		memset((char*)Label, 0, 102*102);

		cin>>H>>W;		
		for (y=1;y<=H;y++)
			for (x=1;x<=W;x++)
				cin>>M[y][x];

		l = 'a';
		for (y=1;y<=H;y++)
			for (x=1;x<=W;x++){
				if (!Label[y][x]){
					Label[y][x]=l;
					//printLabel();
					findBasin(y,x,l, by, bx);
					//printLabel();
					lableFromBasin(by,bx,l);
					//printLabel();
					l++;
				}
			}


		cout <<"Case #"<<c<<":"<<endl;
		printLabel();
	}		
	
	return 0;
}
