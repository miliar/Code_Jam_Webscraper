#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	char grid[101][101], next[101][101];
	memset(grid, 0, sizeof(grid));
	int r, x1, x2, y1, y2;
	cin>>r;
	for(int i=0; i<r; i++){
		cin>>x1>>y1>>x2>>y2;
		for(int x=x1; x<=x2; x++)
		for(int y=y1; y<=y2; y++)
			grid[y][x]=1;
	}
	int time=0;
	int any;
	do{
		any=0;
		memset(next, 0, sizeof(next));
		for(int x=1; x<=100; x++)
		for(int y=1; y<=100; y++){
			if(grid[y][x] && (grid[y-1][x] || grid[y][x-1])){
				next[y][x]=1;
				any=1;
			}
			if(grid[y-1][x] && grid[y][x-1]){
				next[y][x]=1;
				any=1;
			}
		}
		memcpy(grid, next, sizeof(grid));
		time++;
	}while(any);
	cout<<time<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
