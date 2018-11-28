//poj 

#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<queue>

using namespace std;
typedef long long llt;

#define maxv 210

#define LEN 30
#define myAbs(x) ((x)>=0?(x):-(x))
#define Max(x,y) ((x)>(y)?(x):(y))
#define Min(x,y) ((x)<(y)?(x):(y))
#define inf 1999999999
#define MOD 200039
#define eps 1e-8
#define EPS 1e-8
#define M_PI 3.14159265358979323846

int M[maxv][maxv], use[maxv], link[maxv], n, m, k, stock[maxv][maxv];
int ttt=0;
int can(int t)
{
	int i;
	for(i=1;i<=m;i++){
		if(!use[i] && M[t][i]){
			use[i]=1;
			if(link[i]==-1||can(link[i])){
				link[i]=t;
				return 1;
			}
		}
	}
	return 0;
}
int MM()
{
	int i, num;
	num=0;
	memset(link,0xff,sizeof(link));
	for(i=1;i<=n;i++){
		memset(use,0,sizeof(use));
		if(can(i)) num++;
	}
	return num;
}

void go()
{
	int i,j;
	int l, tmp;
	int res;
	scanf("%d%d",&n,&k);
	m= n;
	for(i=1;i<=n;++i){
		for(j=1;j<=k;++j){
			scanf("%d",stock[i]+j);
		}
	}
	memset(M,0,sizeof(M));
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			if(i==j) continue;
			tmp=1;
			for(l=1;l<=k;l++){
				if(stock[i][l]<=stock[j][l]){
					tmp=0;
					break;
				}
			}
			if(tmp) M[i][j]=1;
		}
	}
	res=MM();
	//cout<<res<<endl;
	printf("Case #%d: %d\n",++ttt,n-res);
}
int main()
{
	//freopen("C-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t, i;
	scanf("%d",&t);
	ttt=0;
	while(--t>=0){
		go();
	}
	return 0;
}

