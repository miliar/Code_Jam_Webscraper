#include <vector>
#include <stdio.h>
#include <string>

using namespace std;

#define vs vector<string>
#define vvs vector<vs>
#define vc vector<char>
#define vvc vector<vc>
#define vi vector<int>
#define vvi vector<vi>

int dx[4] = {-1,0,0,1}, 
	dy[4] = {0,-1,1,0};

int altitudes[102][102];
bool chk[102][102];
char map[102][102];
char curbasin;
int H,W;
char drain(int x, int y, char dflt){
	char res;
	int i;
	if(chk[x][y]){
		return map[x][y]; 
	}
	int neighbours[5] = {altitudes[x][y],9999999,9999999,9999999,9999999};
	for(i=0; i<4;++i){
		int x1 = x+dx[i];
		int y1 = y+dy[i];
		if(x1>=0 && x1<H && y1>=0 && y1<W){//OK bonders
			neighbours[i+1] = altitudes[x1][y1];
		}
	}
	int min = 0;
	bool sink = true;
	for(i=0; i<4;++i){
		if(neighbours[min]>neighbours[i+1]){
			sink = false;
			break;
		}
	}
	if(sink){//new sink
		chk[x][y] = true;
		map[x][y] = dflt;
		return dflt;
	}
	for(i=4;i>0; i--){
		if(neighbours[min] >= neighbours[i]){
			min = i;
		}
	}
	min--;
	int x1 = x+dx[min];
	int y1 = y+dy[min];
	if(x1>=0 && x1<H && y1>=0 && y1<W){//OK bonders
		if(chk[x1][y1]){
			chk[x][y] = true;
			map[x][y] = map[x1][y1];
			return map[x1][y1];
		}else{
			char c = drain(x1, y1, dflt);
			chk[x][y] = true;
			map[x][y] = c;
			return c;
		}
	}
	return res;
}

int main(){
	int testnum = 0;
	FILE* in = fopen("B.in","r");
	FILE* out = fopen("B.out","w");
	int Answer;
	fscanf(in, "%d\n", &testnum);
//	int i;
	for(int test = 0; test< testnum; ++test){

		fprintf(out, "Case #%d:\n", test+1);
		fscanf(in,"%d %d\n", &H, &W);
		for(int X = 0; X < H; ++X){
			for(int Y = 0; Y < W; ++Y){
				fscanf(in,"%d", &altitudes[X][Y]);
				map[X][Y] = 0;
				chk[X][Y] = false;
			}
		}
		curbasin = 'a';
		for(int X = 0; X < H; ++X){
			for(int Y = 0; Y < W; ++Y){
				char c = drain(X,Y,curbasin);
				if(c==curbasin){
					curbasin++;
				}
			}
		}
		for(int X = 0; X < H; ++X){
			for(int Y = 0; Y < W; ++Y){
				fprintf(out, "%c ", map[X][Y]);
			}
			fprintf(out, "\n");
		}
	}
	return 0;
}