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

FILE *in=fopen("B.in","r");
FILE *out=fopen("B.out","w");

int n;

int best[10001][301];

map < string , int > mp;

class gtr{
public:
	int type;
	int start;
	int end;
}all[301];

int solve(int a,int b,int c)
{
	int i;
	int cur=0;
	int ret=0;
	while(cur!=10000){
		int maxx=max(best[cur][a],best[cur][b]);
		maxx=max(maxx,best[cur][c]);
		if(maxx<=cur)return 1<<20;
		cur=maxx;
		ret++;
	}
	return ret;
}

int main()
{
	int i,j,k,test,tests;
	fscanf(in,"%d",&tests);
	int start,end;
	char ar[100];
	for(test=1;test<=tests;test++){
		int p=1;
		int x;
		mp.clear();
		CLR(best,-1);
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++){
			fscanf(in,"%s",ar);
			string f=ar;
			if(mp[f])x=mp[f];
			else {
				x=p;
				mp[f]=p++;
			}

			fscanf(in,"%d%d",&start,&end);
			start--;

			all[i].start=start;
			all[i].end=end;
			all[i].type=x;
		}
		for(i=0;i<10000;i++){
			for(j=0;j<n;j++){
				if(all[j].start>i)continue;
				best[i][all[j].type]=max(best[i][all[j].type],all[j].end);
			}
		}
		int ret=1<<20;
		for(i=1;i<=p;i++){
			for(j=i;j<=p;j++){
				for(k=j;k<=p;k++){
					ret=min(ret,solve(i,j,k));
				}
			}
		}
		if(ret!=1<<20){
			printf("Case #%d: %d\n",test,ret);
			fprintf(out,"Case #%d: %d\n",test,ret);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n",test);
			fprintf(out,"Case #%d: IMPOSSIBLE\n",test);
		}
	}
	return 0;
}
