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
#define eps 1e-8
#define PI 3.14159265358979323846
using namespace std;


char c[1010];
char cc[1010];
int k;
int a[10];
int b[10];
int best;
void getac(int d){
	int i;
	if(d==k){
		char last=0;
		int cnt=0;
		for(i=0;c[i];i++){
			cc[i]=c[a[i%k]+i/k*k];
			if(cc[i]!=last){
				last=cc[i];
				cnt++;
			}
		}
		if(cnt<best)
			best=cnt;
	}else{
		for(i=0;i<k;i++){
			if(!b[i]){
				b[i]=1;
				a[d]=i;
				getac(d+1);
				b[i]=0;
			}
		}
	}
}

int main(){
	int T,TT;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		scanf("%d",&k);
		scanf("%s",c);
		memset(b,0,sizeof(b));
		best=1010;
		getac(0);
		printf("Case #%d: %d\n",TT,best);
	
	}
}