#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

int a[128][128];

int main() {
	int T;
	fin>>T;
	int testNum;
	int i,j,n,x,y,x1,y1;
	int ones;
	for(testNum=1;testNum<=T;++testNum) {
		memset(a,0,sizeof a);
		fin>>n;
		ones=0;
		while(n--) {
			fin>>x>>y>>x1>>y1;
			for(i=x;i<=x1;++i) for(j=y;j<=y1;++j) {
				if(a[i][j]==0)++ones;
				a[i][j] = 1;
			}
		}
		int ret = 0;
		while(ones>0) {
			++ret;
			for(i=100;i>=1;--i) for(j=100;j>=1;--j) {
				if(a[i][j]==0) {
					if(a[i-1][j]==1 && a[i][j-1]==1) {
						a[i][j]=1;
						++ones;
					}
				}
				else {
					if(a[i-1][j]==0 && a[i][j-1]==0) {
						a[i][j] = 0;
						--ones;
					}
				}
			}
			
		}
		fout<<"Case #"<<testNum<<": "<<ret<<"\n";
	}
	return 0;
}
