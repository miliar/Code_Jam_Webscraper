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

#define LEN 30
#define myAbs(x) ((x)>=0?(x):-(x))
#define Max(x,y) ((x)>(y)?(x):(y))
#define Min(x,y) ((x)<(y)?(x):(y))
#define inf 1999999999
#define MOD 200039
#define eps 1e-8
#define EPS 1e-8
#define M_PI 3.14159265358979323846

int ttt;
struct node{
	int x,y ,r;
};
node nd[maxv];
int n;

void solve(){
	int i,j,k;
	double tmp1,tmp2;
	double res;
	scanf("%d",&n);
	for(i=0;i<n;++i){
		scanf("%d%d%d",&nd[i].x, &nd[i].y,&nd[i].r);
	}
	res= 1e15;
	if(n==1){
		res= double(nd[0].r);
	}else if(n==2){
		//i=-1;
		//tmp2=(double)nd[(i+1)%n].r + nd[(i+2)%n].r 
		//	+ sqrt((double)(nd[(i+1)%n].x-nd[(i+2)%n].x)*(nd[(i+1)%n].x-nd[(i+2)%n].x) + (double)(nd[(i+1)%n].y-nd[(i+2)%n].y)*(nd[(i+1)%n].y-nd[(i+2)%n].y));
		if(nd[0].r < nd[1].r)
			res= (double)nd[1].r;
		else
			res= (double)nd[0].r;	
		//res= max(double(nd[0].r),double(nd[1].r));
	}else{
		for(i=0;i<n;++i){
			tmp1=(double)nd[i].r;
			tmp2=(double)nd[(i+1)%n].r + nd[(i+2)%n].r 
			+ sqrt((double)(nd[(i+1)%n].x-nd[(i+2)%n].x)*(nd[(i+1)%n].x-nd[(i+2)%n].x) + (double)(nd[(i+1)%n].y-nd[(i+2)%n].y)*(nd[(i+1)%n].y-nd[(i+2)%n].y));
			tmp2/=2.0;
			//printf("temp2 %lf\n",tmp2);
			if(tmp2 > tmp1+eps)
				tmp1= tmp2;
			if(tmp1< res-eps)
				res=tmp1;
		}
	}
	printf("Case #%d: %.7lf\n",++ttt,res);
}
int main(){
	//freopen("D-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	scanf("%d", &t);
	ttt=0;
	while(--t>=0)
		solve();
	//system("PAUSE");
	return 0;
}



