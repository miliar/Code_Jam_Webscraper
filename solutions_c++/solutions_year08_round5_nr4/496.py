#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
using namespace std;

ifstream fin("D-small-attempt2.in");
//ifstream fin("A-large.in");
ofstream fout("D-small-attempt0.out");
//ofstrema fout("A-large.out");



void SolveCase(){
	long long d[101][101]={0};
	long long w,h,r;
	fin>>h>>w>>r;
	for (int i=0;i<r;i++){
		int x,y;
		fin>>x>>y;
		d[x][y]=-1;
	}
		d[1][1]=1;
		for (int i=1;i<=h;i++){
			for (int j=1;j<=w;j++){
				if (d[i][j]>0){
					int nx=i+1;
					int ny=j+2;
					if (nx<=h&&ny<=w&&d[nx][ny]>=0){
						d[nx][ny]+=d[i][j];
						d[nx][ny]%=10007;
					}
					nx=i+2;
					ny=j+1;
					if (nx<=h&&ny<=w&&d[nx][ny]>=0){
						d[nx][ny]+=d[i][j];
						d[nx][ny]%=10007;
					}
				}
			}
		}
		
	fout<<d[h][w]<<endl;
	cout<<d[h][w]<<endl;
}

int main(){
	int TestCase;
	fin>>TestCase;
	for (int Test=1;Test<=TestCase;Test++){
		fout<<"Case #"<<Test<<": ";
		SolveCase();
	}
	fout.close();
	return 0;
}
