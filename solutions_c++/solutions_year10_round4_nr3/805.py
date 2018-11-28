/*
 * C.cpp
 *
 *  Created on: Jun 5, 2010
 *      Author: Yasser
 */


#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

const int SIZE = 400;
bool a[SIZE][SIZE];
bool b[SIZE][SIZE];

int gen(){
	int c =0;
	memset(b,0,sizeof b);
	for(int i=0;i<SIZE;i++){
		for(int j=0;j<SIZE;j++){
			if(a[i][j] && (a[i-1][j] || a[i][j-1]))
				b[i][j] = 1 , c++;
			if(!a[i][j] && a[i-1][j] && a[i][j-1])
				b[i][j] = 1,c++;
		}
	}

	memcpy(a,b,sizeof b);

	return c;
}

int main(){
	freopen("test.in","rt",stdin);
	freopen("out.txt","wt",stdout);

	int TC;
	scanf("%d",&TC);
	int r , x1,x2,y1,y2;
	for(int tt = 0 ;tt <TC;tt++){
		scanf("%d",&r);
		memset(a,0,sizeof a);
		for(int i=0;i<r;i++){
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(int j=x1;j<=x2;j++)
				for(int k=y1;k<=y2;k++){
					a[j][k] = 1;
				}
		}


		int ret = 0;
		while(gen()){
			ret ++;
		}

		printf("Case #%d: %d\n",tt+1 , ret+1);
	}

	return 0;
}
