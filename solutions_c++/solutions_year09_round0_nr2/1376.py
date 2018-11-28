#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
class cell;

vector<vector<cell> > cells;
class cell{
public:
	cell(int attitude,int hight,int width):a(attitude),h(hight),w(width),s('0')
	{for(int i=0;i<4;i++) b[i]=false;}
	int a,h,w;
	char s;
	bool b[4];
	bool name(char n){
		if(s!='0') return false;
		s = n;
		if(b[0]) cells[h-1][w].name(n);
		if(b[1]) cells[h][w-1].name(n);
		if(b[2]) cells[h][w+1].name(n);
		if(b[3]) cells[h+1][w].name(n);
		return true;
	}
};

int main(){ 
	int T,H,W;
	cin>>T;
	int buf;
	ofstream cou("gjamB.txt");

	for(int t=1;t<=T;t++){
		cin>>H>>W;

		for(int h=0;h<H;h++){
			cells.push_back(vector<cell>());
			for(int w=0;w<W;w++){
				cin>>buf;
				cells[h].push_back(cell(buf,h,w));
			}
		}

		int at,min,index;
		//vector<pair<int,int> >  sink;
		for(int h=0;h<H;h++){
			for(int w=0;w<W;w++){
				index = -1;
				min = 10000;
				at = cells[h][w].a;
				if(h>0){buf = cells[h-1][w].a;if(min>buf && at>buf){min = buf;index=0;}}
				if(w>0){buf = cells[h][w-1].a;if(min>buf && at>buf){min = buf;index=1;}}
				if(w<W-1){buf = cells[h][w+1].a;if(min>buf && at>buf){min = buf;index=2;}}
				if(h<H-1){buf = cells[h+1][w].a;if(min>buf && at>buf){min = buf;index=3;}}
				if(index!=-1){
					cells[h][w].b[index] = true;
					switch(index){
						case 0:
							cells[h-1][w].b[3-index] = true;
							break;
						case 1:
							cells[h][w-1].b[3-index] = true;
							break;
						case 2:
							cells[h][w+1].b[3-index] = true;
							break;
						case 3:
							cells[h+1][w].b[3-index] = true;
							break;
					}
				}
				//else
				//	sink.push_back(pair<int,int>(h,w));
			}
		}

		char name = 'a';
		for(int h=0;h<H;h++){
			for(int w=0;w<W;w++){
				if(cells[h][w].name(name))
					name +=1;
			}
		}
		//for(int n=0;n<sink.size();n++){
		//	cells[sink[n].first][sink[n].second].name(name+n);
		//}

		cou<<"Case #"<<t<<":"<<endl;
		for(int h=0;h<H;h++){
			for(int w=0;w<W;w++){
				cou<<cells[h][w].s;
				if(w!=W-1) cou<<" ";
			}
			cou<<endl;
		}
		cells.clear();
	}

	return 0;
}