// GCodeJam_QR^Watersheds.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define H_MAX 100
#define W_MAX 100
#define F_MAX 10000

int map[H_MAX+2][W_MAX+2];
char flowmap[H_MAX+2][W_MAX+2];

struct Point{
	int x;
	int y;
};

//North, West, East, South
void flowCheck(vector<Point>& sinks, int h, int w){
	memset(flowmap, 0, sizeof(char)*(H_MAX+2)*(W_MAX+2));
	char dir;
	int min;
	int flag = 0;
	for(int i=1;i<=h;i++)
		for(int j=1;j<=w;j++){
			dir = 'N';
			min = map[i-1][j];
			if(map[i][j-1] < min ){
				min = map[i][j-1];
				dir = 'W';
			}
			if(map[i][j+1] < min){
				min = map[i][j+1];
				dir = 'E';
			}
			if(map[i+1][j] < min){
				min = map[i+1][j];
				dir = 'S';
			}
			if( map[i][j] > min)
				flowmap[i][j] = dir;
			else{
				flowmap[i][j] = flag;
				flag ++;
				Point sink;
				sink.x = i;
				sink.y = j;
				sinks.push_back(sink);
			}
		}
}

void flow(int i, int j){
	//if(flowmap[i][j] >= 'a' && flowmap[i][j] <= 'z')
	//	return;
	if(flowmap[i-1][j] == 'S'){
		flowmap[i-1][j] = flowmap[i][j];
		flow(i-1, j);
	}
	if(flowmap[i][j-1] == 'E'){
		flowmap[i][j-1] = flowmap[i][j];
		flow(i, j-1);
	}
	if(flowmap[i][j+1] == 'W'){
		flowmap[i][j+1] = flowmap[i][j];
		flow(i, j+1);
	}
	if(flowmap[i+1][j] == 'N'){
		flowmap[i+1][j] = flowmap[i][j];
		flow(i+1, j);
	}
}

void divide(const vector<Point>& sinks){
	for(vector<Point>::const_iterator iter = sinks.begin();
		iter != sinks.end(); ++iter){
			flow(iter->x, iter->y);
	}
}

void output(int t, int h, int w){
	ofstream fout("output.txt", ios::app);
	fout<<"Case #"<<t<<":"<<endl;
	for(int i=1;i<=h;i++){
		for(int j=1;j<=w;j++){
			fout<<flowmap[i][j]<<" ";
		}
		fout<<endl;
	}
}

void flagRefresh(int h, int w){
	char flowNum[26];
	memset(flowNum, 0, sizeof(char)*26);
	int flag=0;
	for(int i=1;i<=h;i++)
		for(int j=1;j<=w;j++){
			if( flowNum[flowmap[i][j]] == 0){
				flowNum[flowmap[i][j]] = 'a' + flag;
				flag++;
			}
			flowmap[i][j] = flowNum[flowmap[i][j]];
		}
}

int main()
{
	ifstream fin("B-large.in");
	int T, H, W;

	fin>>T;
	for(int i=1;i<=T;i++){
		memset(map, F_MAX, sizeof(int)*(H_MAX+2)*(W_MAX+2)); 
		fin>>H>>W;
		for(int j=1;j<=H;j++)
			for(int k=1;k<=W;k++)
				fin>>map[j][k];
			
		vector<Point> sinks;
		flowCheck(sinks, H, W);
		divide(sinks);
		flagRefresh(H, W);
		output(i, H, W);
	}

	return 0;
}

