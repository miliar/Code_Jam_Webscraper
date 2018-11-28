#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;


struct SNode
{
    int a[30];
}node[110];

    int T,Case,N,K;
bool cmp(const SNode x,const SNode y)
{
   if(x.a[0]!=y.a[0] )return x.a[0]<y.a[0];

    for(int i=1;i<K;i++){
        if(x.a[i]!=y.a[i]){
            return x.a[i]>y.a[i];
        }
    }

    return true;

}

int mat[110][110];


#include <string.h>
#define MAXN 110
#define _clr(x) memset(x,0xff,sizeof(int)*n)

int hungary(int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<n;ret+=(match1[i++]>=0))
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

inline int path_cover(int n,int mat[][MAXN],int* pre,int* next){
	return n-hungary(n,mat,next,pre);
}


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    scanf("%d",&T);
    Case=1;
    while(T--){
        scanf("%d %d",&N,&K);
        for(int i=0;i<N;i++){
            for(int j=0;j<K;j++){
                scanf("%d",&node[i].a[j]);
            }
        }

//        sort(node,node+N,cmp);
//         for(int i=0;i<N;i++){
//            for(int j=0;j<K;j++){
//                printf("%d  ",node[i].a[j]);
//            }
//            printf("\n");
//        }
        memset(mat,0,sizeof(mat));
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                int k=0;
                for(;k<K;k++){
                    if(node[i].a[k]>=node[j].a[k])
                        break;
                }
//                printf("%d %d \n",k,K);
                if(k==K)mat[i][j]=1;
            }
        }
//          for(int i=0;i<N;i++){
//            for(int j=0;j<N;j++){
//                printf("%d ",mat[i][j]);
//            }
//            printf("\n");
//          }

//
//
//        int dp[110];
//        memset(dp,0,sizeof(dp));
//        int ans=0;
//        for(int i=0;i<N;i++){
//            dp[i]=1;
//            for(int j=i-1;j>=0;j--){
//                if( !mat[j][i]  && dp[i]<dp[j]+1 )
//                    dp[i]=dp[j]+1;
//            }
//            if(dp[i]>ans)ans=dp[i];
//        }

        int match1[110],match2[110];

        int ans= hungary( N, mat, match1, match2);
        printf("Case #%d: %d\n",Case,N-ans);
        Case++;
    }
    return 0;
}
