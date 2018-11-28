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

class gtr{
public:
	int type;
	int malted;
}ar[3001][3001];

int sz[3001];

int must[3001],vis[3001];

int main()
{
	int test,t,n,m,i,j,mk;
	fscanf(in,"%d",&t);
	for(test=1;test<=t;test++){
		fscanf(in,"%d%d",&n,&m);
		for(i=0;i<m;i++){
			fscanf(in,"%d",&sz[i]);
			for(j=0;j<sz[i];j++){
				fscanf(in,"%d%d",&ar[i][j].type,&ar[i][j].malted);
				ar[i][j].type--;
			}
		}
		CLR(must,0);
		for( mk=0;mk<3000;mk++){
			for(i=0;i<m;i++){
				for(j=0;j<sz[i];j++){
					int malted=ar[i][j].malted;
					int type=ar[i][j].type;
					if(malted==1)continue;
					if(!must[type])break;
				}
				if(j==sz[i]){
					for(j=0;j<sz[i];j++){
						int malted=ar[i][j].malted;
						int type=ar[i][j].type;
						if(malted==1){
							must[type]=1;
							break;
						}
					}
					if(j==sz[i]){
						i=-1;
						goto PR;
					}
				}
			}
		}
PR:
		if(i==-1)fprintf(out,"Case #%d: IMPOSSIBLE\n",test);
		else {
			fprintf(out,"Case #%d:",test);
			for(i=0;i<n;i++)fprintf(out," %d",must[i]);
			fprintf(out,"\n");
		}		
	}
	return 0;
}