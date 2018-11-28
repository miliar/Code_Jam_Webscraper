#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
using namespace std;

typedef long long LL;
const int MAXR=11;
const int MOD=10007;

struct pt{
    int x,y;
};
pt A[MAXR];
int C[MOD][MOD];
int H,W,R;

void pre(){
    int i,j;
    for(i=0;i<MOD;i++) C[i][0]=C[i][i]=1;
    for(i=2;i<MOD;i++){
        for(j=1;j<i;j++){
            C[i][j]=C[i-1][j]+C[i-1][j-1];
            if(C[i][j]>=MOD) C[i][j]-=MOD;
        }
    }
}
int F(int m,int n){
    int re=1;
    while(m>=MOD||n>=MOD){
        re=(re*C[m%MOD][n%MOD])%MOD;
        m/=MOD;
        n/=MOD;
    }
    return (re*C[m][n])%MOD;
}
int cmp(pt a,pt b){
    return a.x<b.x||(a.x==b.x&&a.y<b.y);
}
int sol(int s){
	int i,cnt,curx,cury,re;
	re=1;
	curx=cury=1;
	cnt=0;
	for(i=0;i<R;i++){
		if((1<<i)&s){
			cnt++;
			if(curx>=A[i].x||cury>=A[i].y||(A[i].x-curx+A[i].y-cury)%3)
				return 0;
			re=re*F((A[i].x-curx+A[i].y-cury)/3,A[i].x-curx-(A[i].x-curx+A[i].y-cury)/3)%MOD;
			curx=A[i].x;
			cury=A[i].y;
		}
	}
	if((H-curx+W-cury)%3) return 0;
	re=re*F((H-curx+W-cury)/3,H-curx-(H-curx+W-cury)/3)%MOD;
	if(re<0)
		re+=MOD;
	if(cnt&1)
		re=-re;
	return re;
}
int main(){
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small.out","w",stdout);
    pre();
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d%d%d",&H,&W,&R);
        int i,j;
        for(i=0;i<R;i++){
            scanf("%d%d",&A[i].x,&A[i].y);
        }
        sort(A,A+R,cmp);
        int ans=0;
        for(i=0;i<(1<<R);i++){
            ans=(ans+sol(i))%MOD;
        }
        if(ans<0) ans+=MOD;
        printf("Case #%d: %d\n",ic,ans);
    }
    return 0;
}
