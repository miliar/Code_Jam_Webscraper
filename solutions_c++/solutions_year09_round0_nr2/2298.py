#include <iostream>
#include <string>

#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef struct _tagCell{
int alt; //altitude;
int flowfrom[4]; //whether the water is flow from 4 direction 1-from, 0-no water from -1 - to
				// index: 0-north, 1-west, 2 - east, 3- south
}Cell;
typedef struct _tagFlow{
int alt[4];
int flag[4]; //0- invalid direction
}Flow; 

void traceallcell(const vector<vector<Cell> >& mymap, int ch, int cw,char name,vector<vector<char> >& outputmap){
	outputmap[ch][cw] = name;
	if(mymap[ch][cw].flowfrom[0] == 1)
		traceallcell(mymap, ch-1, cw, name, outputmap);
	if(mymap[ch][cw].flowfrom[1] == 1)
		traceallcell(mymap, ch, cw - 1, name, outputmap);
	if(mymap[ch][cw].flowfrom[2] == 1)
		traceallcell(mymap, ch, cw + 1, name, outputmap);
	if(mymap[ch][cw].flowfrom[3] == 1)
		traceallcell(mymap, ch+1, cw, name, outputmap);
	return;
}
//Check if there is outflow; <0 means no output
int outflow(const Cell& cell){
	for(int x = 0; x< 4;x++){
		if(cell.flowfrom[x] == -1)
			return x;
	}
	return -1;
}
void onecase(int casenum){
int height, width;
	cin>>height;
	cin>>width;
	vector<vector<Cell> > mymap;
	mymap.resize(height);
	int h, w;
	for(h=0;h<height;h++){
		mymap[h].resize(width);
		for(w=0;w<width;w++){
			cin>>(mymap[h][w].alt);
			for(int x=0;x<4;x++)
				mymap[h][w].flowfrom[x] = 0;
		}
	}
	//Read the map in. Now caculate each water flow
	for(h=0;h<height;h++){
		for(w=0;w<width;w++){
			Flow flow;
			for(int x=0;x<4;x++){
				flow.flag[x] = 1; //init
			}
			if(h == 0) 
				flow.flag[0] = 0; //no north
			else
				flow.alt[0] = mymap[h - 1][w].alt; //north altitude
			if(w == 0) 
				flow.flag[1] = 0; //no west
			else
				flow.alt[1] = mymap[h][w - 1].alt; //west altitude
			if(h == (height - 1)) 
				flow.flag[3] = 0; //no south
			else
				flow.alt[3] = mymap[h + 1][w].alt; //south altitude
			if(w == (width - 1)) 
				flow.flag[2] = 0; //no east
			else
				flow.alt[2] = mymap[h][w + 1].alt; //north altitude
			//choose a direction
			//Pick the lowest in the order 0,1,2,3
			int lowest;
			int direct = 5; //inited as invalid direction
			for(int y=0;y<4;y++){
				if(flow.flag[y])
					if(direct == 5){
						//not inited, no compare
						direct = y;
						lowest = flow.alt[y];
					}else{
						if(flow.alt[y] < lowest){
							direct = y;
							lowest = flow.alt[y];
						}
					}
				}
			if(direct != 5){
				if(lowest < mymap[h][w].alt){
					mymap[h][w].flowfrom[direct] = -1;
					switch(direct){
					case 0: //north
						mymap[h-1][w].flowfrom[3] = 1;
						break;
					case 1: //west
						mymap[h][w-1].flowfrom[2] = 1;
						break;
					case 2://east
						mymap[h][w+1].flowfrom[1] = 1;
						break;
					case 3://south
						mymap[h+1][w].flowfrom[0] = 1;
						break;
					}
				}
			}
		}
	}
	//Now prepare the result
	vector<vector<char> > outputmap;
	outputmap.resize(height);
	for(h=0;h<height;h++){
		outputmap[h].resize(width);
		for(w=0;w<width;w++){
			outputmap[h][w] = 0;
		}
	}
	char name='a';
	for(h=0;h<height;h++){
		for(w=0;w<width;w++){
			if(outputmap[h][w] == 0){
				int fdir;
				int ch=h;
				int cw=w;
				while((fdir = outflow(mymap[ch][cw])) >= 0){
					outputmap[ch][cw]=name;
					switch(fdir){
					case 0: ch--;break;
					case 1: cw--;break;
					case 2: cw++;break;
					case 3: ch++;break;
					}
				}
				outputmap[ch][cw]=name;
				traceallcell(mymap, ch,cw,name,outputmap);
				name++;
			}
		}
	}
	cout<<"Case #"<<casenum<<":"<<endl;
	for(h=0;h<height;h++){
		for(w=0;w<width;w++){
			cout<<outputmap[h][w]<<" ";
		}
		cout<<endl;
	}
}

void allcases(void){
int mapnum;
	cin>>mapnum;
	for(int i=0;i<mapnum;i++){
		onecase(i+1);
	}
}

int main(int argc, char **argv){

	allcases(); 
return 0;
}
