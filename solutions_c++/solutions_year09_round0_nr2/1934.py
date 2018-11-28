//*******************************************
// Author: Samuel Jero
// Email: samuel.jero@gmail.com
// Date: 9/3/2009
//*******************************************
#include <string>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <limits>
using namespace std;


void load_map();
void process_map();
void find_path(int x, int y, char mark);

vector<vector<int> > map;
vector<vector<char> > table;
vector<vector<int> > design;
int height;
int width;


int main(){
	int testcases;

	cin>>testcases;
	for(int i=1; i <= testcases; i++){
		load_map();
		process_map();
		cout<<"Case #"<<i<<":"<<endl;
		for(int y=0; y < height; y++){
			for(int x=0; x < width; x++){
				cout<<table[y][x]<<" ";
			}
			cout<<endl;
		}
	}
return 0;
}



void load_map(){
	vector<int> tmp;
	vector<char>temp;
	int in;
	char t = '0';
	cin>>height;
	cin>>width;
	map.clear();
	design.clear();
	table.clear();
	for(int y=0; y < height; y++){
		map.push_back(tmp);
		table.push_back(temp);
		design.push_back(tmp);
		for(int x=0; x <width; x++){
			cin>>in;
			if(cin.fail()){
				exit(1);
			}
			map[y].push_back(in);
			table[y].push_back(t);
			design[y].push_back(0);
		}
	}
return;
}



void process_map(){
	int next_l= 0;
	int comp;
	int dir;

	for(int y=0; y < height; y++){
		for(int x=0; x < width; x++){
			comp=1000000;
			dir=0;
			if((y < height-1) &&(map[y+1][x] < map[y][x])){
				comp= map[y+1][x];
				dir=1;
			}
			if((x < width-1) && (map[y][x+1] < map[y][x])){
				if(map[y][x+1] <= comp){
					comp=map[y][x+1];
					dir=2;
				}
			}
			if((x > 0) && (map[y][x-1] < map[y][x])){
				if(map[y][x-1] <= comp){
					comp=map[y][x-1];
					dir=3;
				}
			}
			if((y > 0) &&(map[y-1][x]<map[y][x])){
				if(map[y-1][x] <= comp){
					comp=map[y-1][x];
					dir=4;
				}
			}
			design[y][x]=dir;
		}
	}

	for(int y=0; y < height; y++){
		for(int x=0; x <width; x++){
			if(table[y][x]=='0'){
				find_path(x,y, next_l + 'a');
				next_l++;
			}
		}
	}
return;
}



void find_path(int x, int y, char mark){
	if(table[y][x]=='0'){
		table[y][x]=mark;
		if(design[y][x]!=0){
			if(design[y][x]==1){
				find_path(x, y+1, mark);
			}else{
				if(design[y][x]==2){
					find_path(x+1, y, mark);
				}else{
					if(design[y][x]==3){
						find_path(x-1, y, mark);
					}else{//design[y][x]==4
						find_path(x, y-1, mark);
					}
				}
			}
		}
		if((y < height-1) &&(design[y+1][x]== 4)){
			find_path(x, y+1, mark);
		}
		if((y> 0)&&(design[y-1][x]== 1)){
			find_path(x, y-1,mark);
		}
		if((x < width-1)&&(design[y][x+1]== 3)){
			find_path(x+1, y, mark);
		}
		if((x > 0)&&(design[y][x-1]== 2)){
			find_path(x-1, y,mark);
		}
	}
return;
}
