// BEGIN CUT HERE

// END CUT HERE
#line 5 "ImportsList.cpp"
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

struct node{
	int x;
	int y;
	node(int a, int b){
		x=a;
		y=b;
	}
};

int main(){
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	int N;
	fin>>N;
	for(int round=1;round<=N;round++){
		int row,col;
		fin>>row>>col;
		vector< vector<int> > map;
		
		for(int i=0;i<row;i++){
			vector<int> tmp;
			for(int j=0;j<col;j++){
				int tmp2;
				fin>>tmp2;
				tmp.push_back(tmp2);
			}
			map.push_back(tmp);
		}
		
		
		int dx[]={-1,0,0,1};
		int dy[]={0,-1,1,0};
		
		vector< vector<int> > graph;
		
		vector< vector<int> > paint;
		
		
		
		for(int i=0;i<row;i++){
			vector<int> ptmp;
			for(int j=0;j<col;j++){
				ptmp.push_back(-1);
			}
			paint.push_back(ptmp);
		}
		
		int sinknum=0;

			for(int i=0;i<row;i++){
				vector<int> tg;
				for(int j=0;j<col;j++){
					
						int min=map[i][j];
						int dir = -1;
						for(int k=0;k<4;k++){
							int tx=i+dx[k];
							int ty=j+dy[k];
							if(tx>=0 && tx<row && ty>=0 && ty<col && map[tx][ty]<min){
								min=map[tx][ty];
								dir=k;
							}
						}
						
						if(dir==-1){
							paint[i][j]=sinknum;
							sinknum++;
						}
						tg.push_back(dir);
				
				}
				graph.push_back(tg);
			}
		
		
		
			
		//repaint;
		int cnt=row*col - sinknum;
		while(cnt>0){
			
			for(int i=0;i<row;i++){
				for(int j=0;j<col;j++){
					if(paint[i][j]!=-1){	continue;}
					int tx=i+dx[graph[i][j]];
					int ty=j+dy[graph[i][j]];
					if(paint[tx][ty]!=-1){
						paint[i][j]=paint[tx][ty];
						cnt--;
					}
				}
			}
		}
		
		
		//after iteration;

		
		
		vector< pair<int,int> > p;
		int next=0;
		
		for(int i=0;i<row;i++){
			for(int j=0;j<col;j++){
				bool has=false;
				for(int k=0;k<p.size();k++){
					if(paint[i][j] == p[k].first){
						paint[i][j] = p[k].second;
						has=true;
						break;
					}
				}
				if(!has){
					p.push_back(make_pair(paint[i][j],next));
					paint[i][j]=next;
					next++;
				}
			}
		}
		
		
		
		fout<<"Case #"<<round<<":"<<endl;
		for(int i=0;i<row;i++){
			for(int j=0;j<col-1;j++){
				fout<<char(paint[i][j]+'a')<<" ";
			}
			fout<<char(paint[i][col-1]+'a')<<endl;
		}
		
	}
}


















