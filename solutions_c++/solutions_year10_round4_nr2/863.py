/*
 * B.cpp
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

int m[1050];
int ret = 0;

int fun(int from,int to){
	bool fl = false;


	for(int i=from;i<to;i++){
		if(m[i]){
			fl = 1;
			m[i]--;
		}
	}

	if(fl){
		ret ++;
		int mid = (from + to)/2;
		fun(from , mid);
		fun(mid , to);
	}
}

int main(){
	freopen("test.in","rt",stdin);
	freopen("out.txt","wt",stdout);

	int TC;
	scanf("%d" , &TC);
	int p,x;
	for(int tt=0;tt<TC;tt++){
		scanf("%d",&p);
		for(int i=0;i<(1<<p);i++){
			scanf("%d",&m[i]);
			m[i] = p-m[i];
		}


		for(int i=p-1;i>=0;i--){
			for(int j=0;j<(1<<i) ; j++)
				scanf("%d",&x);
		}

		ret = 0;

		fun(0,1<<p);

		printf("Case #%d: %d\n",tt+1 , ret);
	}


	return 0;
}
