#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int in[101][101];
char out[101][101];
const int S[2] = {0,1};
const int E[2] = {1,0};
const int W[2] = {-1,0};
const int N[2] = {0,-1};
char sink;

int height,width;

bool inside(int x, int y)
{
	return x>=0 and x < width and y>=0 and y<height;
}

void change(char a, char b)
{
	for(int y = 0; y < height; ++y){
		for(int x = 0; x < width; ++x){
			if(out[x][y]==a)
				out[x][y]=b;
		}
	}
}

void flow(int x, int y)
{
	if(out[x][y]!='0'){
		change('1',out[x][y]);
		return;
	}
		
	out[x][y]='1';
	int dir[2];
	int value = in[x][y];
	// South
	if(inside(x+S[0],y+S[1])){
		if(value >= in[x+S[0]][y+S[1]]){
			value = in[x+S[0]][y+S[1]];
			dir[0]=S[0];
			dir[1]=S[1];
		}
	}
	// East
	if(inside(x+E[0],y+E[1])){
		if(value >= in[x+E[0]][y+E[1]]){
			value = in[x+E[0]][y+E[1]];
			dir[0]=E[0];
			dir[1]=E[1];
		}
	}
	// West
	if(inside(x+W[0],y+W[1])){
		if(value >= in[x+W[0]][y+W[1]]){
			value = in[x+W[0]][y+W[1]];
			dir[0]=W[0];
			dir[1]=W[1];
		}
	}
	// North
	if(inside(x+N[0],y+N[1])){
		if(value >= in[x+N[0]][y+N[1]]){
			value = in[x+N[0]][y+N[1]];
			dir[0]=N[0];
			dir[1]=N[1];
		}
	}
	if(value==in[x][y]){
		change('1',sink);
		sink++;
		return;
	}
		
	flow(x+dir[0],y+dir[1]);
}

int main()
{
	int n;
	cin >> n;
	for(int i = 0; i < n; ++i){
		cin >> height >> width;
		for(int y = 0; y < height; ++y){
			for(int x = 0; x < width; ++x){
				out[x][y]='0';
				cin >> in[x][y];
			}
		}
		sink='a';
		for(int y = 0; y < height; ++y){
			for(int x = 0; x < width; ++x){
				flow(x,y);
			}
		}

		cout << "Case #" << i+1 << ":" << endl;
		for(int y = 0; y < height; ++y){
			for(int x = 0; x < width-1; ++x){
				cout << out[x][y] << " ";
			}
			cout << out[width-1][y] << endl;
		}
	}
}
