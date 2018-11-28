#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;

int R,C;
int alt[100][100];
int basin[100][100];
int rd[]={-1,0,0,1};
int cd[]={0,-1,1,0};
int curbasin;
int basinnum;

bool ok(int i,int j){
    return i>=0 && i<R && j>=0 && j<C;
}

void go(int i,int j){

    if(basin[i][j]!=-1){
	curbasin=basin[i][j];
	basinnum--;
	return;
    }

    int mnalt=20000;
    int ni,nj;

    for(int k=0;k<4;k++){
	int ii=i+rd[k];
	int jj=j+cd[k];
	if(ok(ii,jj))
	    if(alt[ii][jj]<mnalt){
		mnalt=alt[ii][jj];
		ni=ii;
		nj=jj;
	    }
    }

    if(mnalt<alt[i][j])
	go(ni,nj);

    basin[i][j]=curbasin;

}

main(){

    int T; scanf("%d",&T);
    for(int test=1;test<=T;test++){

	printf("Case #%d:\n",test);

	scanf("%d %d",&R,&C);
	for(int i=0;i<R;i++)
	    for(int j=0;j<C;j++){
		scanf("%d",&alt[i][j]);
		basin[i][j]=-1;
	    }

	curbasin=0;
	basinnum=0;
	for(int i=0;i<R;i++)
	    for(int j=0;j<C;j++)
		if(basin[i][j]==-1){
		    go(i,j);
		    basinnum++;
		    curbasin=basinnum;
		}

	for(int i=0;i<R;i++){
	    for(int j=0;j<C;j++)
		printf("%c ",basin[i][j]+'a');
	    putchar('\n');
	}
    }
}
	
