#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

struct cell
{
	int altitudes;
	int x;
	int y;
//	int zs;
};

int main(){
	int i,j,k,h,w;
	int lowest,lx,ly;
	int cx1,cx2,cy1,cy2;
	int tmpx,tmpy;
	int T,H,W;
	ifstream fin("B-large.in");
	string s;
	getline(fin,s);
	istringstream is(s);
	is>>T;
	for (k=0;k<T;k++){
		getline(fin,s);
		istringstream is(s);
		is>>H>>W;
		cell **cells = new cell*[H];
		for (i=0;i<H;i++){
			cells[i] = new cell[W];
		}
		for (i=0;i<H;i++){
			getline(fin,s);
			istringstream is(s);
			for (j=0;j<W;j++){
				is>>cells[i][j].altitudes;
				cells[i][j].x = i;
				cells[i][j].y = j;
//				cells[i][j].zs = 1;
			}
		}
		for (h=0;h<H;h++){
			for (w=0;w<W;w++){
				lowest = cells[h][w].altitudes;
				if(h-1>=0)
				{
					if(cells[h-1][w].altitudes<lowest){
						lowest = cells[h-1][w].altitudes;
						lx = h-1;
						ly = w;
					}
				}
				if(w-1>=0)
				{
					if(cells[h][w-1].altitudes<lowest){
						lowest = cells[h][w-1].altitudes;
						lx = h;
						ly = w-1;
					}
				}
				if(w+1<W)
				{
					if(cells[h][w+1].altitudes<lowest){
						lowest = cells[h][w+1].altitudes;
						lx = h;
						ly = w+1;
					}
				}
				if(h+1<H)
				{
					if(cells[h+1][w].altitudes<lowest){
						lowest = cells[h+1][w].altitudes;
						lx = h+1;
						ly = w;
					}
				}
				
				if(lowest == cells[h][w].altitudes)
					continue;
				for(cx1=h,cy1=w; cx1!=cells[cx1][cy1].x||cy1!=cells[cx1][cy1].y; cx1=cells[tmpx][tmpy].x,cy1=cells[tmpx][tmpy].y){
					tmpx = cx1;
					tmpy = cy1;
				}
				for(cx2=lx,cy2=ly; cx2!=cells[cx2][cy2].x||cy2!=cells[cx2][cy2].y; cx2=cells[tmpx][tmpy].x,cy2=cells[tmpx][tmpy].y){
					tmpx = cx2;
					tmpy = cy2;
				}
				if(cx1==cx2&&cy1==cy2)
					continue;
// 				if(cells[cx1][cy1].zs<=cells[cx2][cy2].zs){
// 					cells[h][w].x = cx2;
// 					cells[h][w].y = cy2;
// 					cells[cx2][cy2].zs += cells[cx1][cy1].zs;
// 				}else{
// 					cells[lx][ly].x = cx1;
// 					cells[lx][ly].y = cy1;
// 					cells[cx1][cy1].zs += cells[cx2][cy2].zs;
// 				}
				cells[h][w].x = cx2;
				cells[h][w].y = cy2;
			}
		}
		pair<int,int> pos;
		map<pair<int,int>,char> rm;
		char c= 'a';
		cout<<"Case #"<<k+1<<":"<<endl;
		for (h=0;h<H;h++){
			for (w=0;w<W;w++){
				for(cx1=h,cy1=w; cx1!=cells[cx1][cy1].x||cy1!=cells[cx1][cy1].y; cx1=cells[tmpx][tmpy].x,cy1=cells[tmpx][tmpy].y){
					tmpx = cx1;
					tmpy = cy1;
				}
				if(rm.count(make_pair(cx1,cy1))){
					cout<<rm[make_pair(cx1,cy1)]<<" ";
				}else{
					cout<<c<<" ";
					rm[make_pair(cx1,cy1)] = c++;
				}
			}
			cout<<endl;
		}
	}
	return 0;
}