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

#define eps 1e-8
#define PI 3.14159265358979323846
#define push_back(a) pb(a)
typedef long long ll;

int a[100][100];
int b[100][100];
int h,w;
bool inboard(int x,int y){
	if(x<h && y<w){
		return 1;
	}
	return 0;
}

int main(){
	int T,TT;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		printf("Case #%d: ",TT);
		int R,r,c,i,j,k;
		scanf("%d%d%d",&h,&w,&R);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<R;i++){
			scanf("%d%d",&r,&c);
			r--;c--;
			b[r][c]=1;
		}
		a[0][0]=1;
		int dx[]={1,2};
		int dy[]={2,1};
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				for(k=0;k<2;k++){
					if(inboard(i+dx[k],j+dy[k]) && !b[i+dx[k]][j+dy[k]]){
						a[i+dx[k]][j+dy[k]]+=a[i][j];
						a[i+dx[k]][j+dy[k]]%=10007;
					}
				}
			}
		}
		printf("%d\n",a[h-1][w-1]);
	}
}