//poj 

#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
#include<set>
#include<queue>

using namespace std;
typedef long long llt;

#define maxv 50

#define LEN 200
#define myAbs(x) ((x)>=0?(x):-(x))
#define Max(x,y) ((x)>(y)?(x):(y))
#define Min(x,y) ((x)<(y)?(x):(y))
#define inf 1999999999
#define MOD 200039
#define eps 1e-8
#define EPS 1e-8
#define M_PI 3.14159265358979323846

int ttt;
int n;
char str[maxv];
int M[maxv];

void solve(){
	int i,j,k;
	int tmp;
	int mi;
	int res;
	scanf("%d",&n);
	for(i=0;i<n;++i){
		M[i]=0;
		scanf("%s",str);
		for(j=0;j<n;++j){
			if(str[j]=='1')
				M[i]=j;
		}
		//printf("%d \n",M[i]);
	}
	res=0;
	for(i=0;i<n;++i){
		if(M[i]<=i)
			continue;
		for(j=i+1;j<n;++j){
			if(M[j]<=i)
				break;
		}
		//tmp = M[j];
		for(;j>i;--j){
			M[j]=M[j-1];
			++res;
		}
		//printf("test %d\n",j);
		//M[j]= M[i];
		//++res;
	}
	printf("Case #%d: %d\n",++ttt,res);
}
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	scanf("%d", &t);
	ttt=0;
	while(--t>=0)
		solve();
	//system("PAUSE");
	return 0;
}



/*
388
2 3
2 3 7
9 10

*/
