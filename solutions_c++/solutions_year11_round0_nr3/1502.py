#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define equal(a,b) (ABS((a)-(b))<eps)
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pair pair<int,int>

using namespace std;

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};
int c[1010];
int main(){
	string filename;
	filename ="C";
	filename = "C-small-attempt0";
	filename = "C-large";
	freopen((filename+".in").c_str(),"r",stdin);
	freopen((filename+".out").c_str(),"w",stdout);
	int T,N;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		//i = (i - 1) & superset
		scanf("%d",&N);
		int superset = (1<<N)-1;
		int no;
		int sum=0;
		for(int i=0; i<N; i++) {
			scanf("%d",&c[i]) ;
			if(i==0) no=c[i];
			else no^=c[i];
			sum+=c[i];
		}
		printf("Case #%d: ",t);
		if(no==0){
			sort(c,c+N);
			printf("%d\n",sum-c[0]);
		} else {
			printf("NO\n");
		}
	}
	//system("pause");
	return 0;
}
