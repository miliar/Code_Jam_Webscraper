#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool a[100][10][2];
bool b[10];
bool bb[10];
int best;
int n,m;

bool chk1(int p){
	for(int i=0;i<n;i++){
		if(a[p][i][b[i]]){
			return 1;
		}
	}
	return 0;
}

bool chk(){
	for(int i=0;i<m;i++){
		if(!chk1(i))
			return 0;
	}
	return 1;
}

void getac(int d){
	int i;
	if(d==n){
		if(chk()){
			int cnt=0;
			for(i=0;i<n;i++){
				if(b[i])
					cnt++;
			}
			if(cnt<best){
				best=cnt;
				for(i=0;i<n;i++){
					bb[i]=b[i];
				}
			}
		}
		return;
	}
	b[d]=1;
	getac(d+1);
	b[d]=0;
	getac(d+1);
}

int main(){
	int T,tt;
	scanf("%d",&T);
	for(tt=1;tt<=T;tt++){
		int i,j;
		scanf("%d",&n);
		scanf("%d",&m);
		memset(a,0,sizeof(a));
		for(i=0;i<m;i++){
			int t;
			scanf("%d",&t);
			for(j=0;j<t;j++){
				int x,y;
				scanf("%d%d",&x,&y);
				x--;
				a[i][x][y]=1;
			}
		}
		best=1000;
		getac(0);

		//cout<<sizeof(long double)<<endl;
		printf("Case #%d: ",tt);
		if(best==1000){
			printf("IMPOSSIBLE\n");
		}else{
			for(i=0;i<n;i++){
				printf("%d ",bb[i]);
			}
			printf("\n");
		}

	}
}
