#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("R1C.in","r");
FILE *out=fopen("R1C.out","w");

string ar[50];

int grid[50][50];

int gethex(char x)
{
	if(x=='A')return 10;
	if(x=='B')return 11;
	if(x=='C')return 12;
	if(x=='D')return 13;
	if(x=='E')return 14;
	if(x=='F')return 15;
	return x-'0';
}
int flag[50][50];

int cnt[50][50];

int ret[50];

int main()
{
	int i,j,n,k,m;
	int tests;
	fscanf(in,"%d",&tests);
	for(int test=0;test<tests;test++){
		fscanf(in,"%d%d",&n,&m);
		char junk[50];
		CLR(grid,-1);
		for(i=0;i<n;i++){
			fscanf(in,"%s",junk);
			ar[i]=junk;
			for(j=0;j<ar[i].size();j++){
				for(k=0;k<4;k++){
					grid[i][(j+1)*4-k-1]=(gethex(ar[i][j])&(1<<k))==0;
				}
			}
		}
		CLR(flag,0);
		CLR(ret,0);
		int bi=0,bj;
		for(k=0;bi!=-1;k++){
			CLR(cnt,0);
			for(i=0;i<n;i++){
				for(j=m-1;j>=0;j--){
					if(flag[i][j])cnt[i][j]=0;
					else if(grid[i][j]==grid[i][j+1])cnt[i][j]=1;
					else cnt[i][j]=cnt[i][j+1]+1;
				}
			}
			int big=0;
			bi=-1;
			for(i=0;i<n;i++){
				for(j=0;j<m;j++){
					int how=1;
					if(flag[i][j])continue;
					int qq=1<<20;
					for(k=i;k<n;k++){
						if(k!=i && grid[k][j]==grid[k-1][j])break;
						qq=min(qq,cnt[k][j]);
						int ww=min(k-i+1,qq);
						if(ww>big){
							big=ww;
							bi=i;
							bj=j;
						}
					}
				}
			}
			if(bi!=-1){
				ret[big]++;
				for(i=bi;i<bi+big;i++)for(j=bj;j<bj+big;j++)flag[i][j]=1;
			}
		}
		int ee=0;
		for(i=40;i>0;i--)if(ret[i])ee++;
		fprintf(out,"Case #%d: %d\n",test+1,ee);
		for(i=40;i>0;i--)if(ret[i]){
			fprintf(out,"%d %d\n",i,ret[i]);
		}
	}
	return 0;
}