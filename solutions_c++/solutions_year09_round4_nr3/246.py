#include <iostream>
using namespace std;
//二分图最大匹配,hungary算法,邻接阵形式,复杂度O(m*m*n)
//返回最大匹配数,传入二分图大小m,n和邻接阵mat,非零元素表示有边
//match1,match2返回一个最大匹配,未匹配顶点match值为-1
#include <string.h>
#define MAXN 310
#define _clr(x) memset(x,0xff,sizeof(int)*MAXN)

int hungary(int m,int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<m;ret+=(match1[i++]>=0))
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
	return ret;
}

int main(){
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int cas,ca=1,n,k,i,t,j;
    cin>>cas;
    int a[110][110],g[120][MAXN],match1[MAXN],match2[MAXN];
    while(cas--){
        cin>>n>>k;
        for(i=0;i<n;i++){
            for(j=0;j<k;j++){
                cin>>a[i][j];
            }
        }
        memset(g,0,sizeof(g));
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                for(t=0;t<k;t++){
                    if(a[j][t]<=a[i][t])break;
                }
                if(t==k)g[i][j]=1;
            }
        }
        int res=hungary(n,n,g,match1,match2);
        printf("Case #%d: %d\n",ca++,n-res);
    }
    return 0;
}
        
        
