#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 30000
#define INF 100000

int n,v;
int resp[MAXN][2];
bool mrk[MAXN][2];
bool isand[MAXN];
bool can[MAXN];
bool val[MAXN];

void calc(int m,int v){
	if(mrk[m][v]) return ;
	mrk[m][v] = true;
	int ou,ane;
	
	calc(2*m+1,0);
	calc(2*m+1,1);
	calc(2*m+2,0);
	calc(2*m+2,1);
	
	if(v == 0){
		ou = resp[2*m+1][0]+resp[2*m+2][0];
		ane = min(resp[2*m+1][0]+resp[2*m+2][0],min(resp[2*m+1][1]+resp[2*m+2][0],resp[2*m+1][0]+resp[2*m+2][1]));
		if(isand[m]){
			if(can[m]) resp[m][v] = min(1+ou,ane);
			else resp[m][v] = ane;	
		}
		else{
			if(can[m]) resp[m][v] = min(ou,1+ane);
			else resp[m][v] = ou;	
		}
	}
	else{
		ane = resp[2*m+1][1]+resp[2*m+2][1];
		ou = min(resp[2*m+1][1]+resp[2*m+2][1],min(resp[2*m+1][1]+resp[2*m+2][0],resp[2*m+1][0]+resp[2*m+2][1]));
		if(isand[m]){
			if(can[m]) resp[m][v] = min(1+ou,ane);
			else resp[m][v] = ane;	
		}
		else{
			if(can[m]) resp[m][v] = min(ou,1+ane);
			else resp[m][v] = ou;	
		}
	}
	
}

int main(){
	
	int t,lp;
	int i,j,k;
	
	scanf("%d",&t);
	
	for(lp=1;lp<=t;lp++){
		
		scanf("%d %d",&n,&v);
		
		for(i=0;i<n;i++){
			mrk[i][0] = mrk[i][1] = false;
			resp[i][0] = resp[i][1] = INF;
			can[i] = false;
		}
		
		for(i=0;i<(n-1)/2;i++){
			scanf("%d",&k);
			isand[i] = (k == 1);
			scanf("%d",&k);
			can[i] = (k == 1);
		}
		
		for(i=(n-1)/2;i<n;i++){
			scanf("%d",&k);
			val[i] = k;
			resp[i][k] = 0;
			resp[i][1-k] = INF;
			mrk[i][k] = mrk[i][1-k] = true;
		}
		
		calc(0,v);
		
		if(resp[0][v] < INF) printf("Case #%d: %d\n",lp,resp[0][v]);
		else printf("Case #%d: IMPOSSIBLE\n",lp);
	}
	
	return 0;
	
}
