#include<iostream>
#include <cstring>
#include<vector>
#include<algorithm>
#define _clr(x) memset(x, 0xff, sizeof(int) * MAXN)
using namespace std;
int N,K;
const int MAXN = 310;
vector<int> A[MAXN ];
bool up[MAXN ][MAXN ],mk[MAXN ];
int match1[MAXN],match2[MAXN];
int hungary(int m, int n, const bool mat[][MAXN]) {
	int s[MAXN + 1], t[MAXN], p, q, ret = 0, i, j, k;
	_clr(match1);
	_clr(match2);
	for (i = 0; i < m; ret += (match1[i++] >= 0)) {
		_clr(t);
		for (s[p = q = 0] = i; p <= q && match1[i] < 0; p++) {
			k = s[p];
			for (j = 0; j < n && match1[i] < 0; j++) {
				if (mat[k][j] && t[j] < 0) {
					s[++q] = match2[j];
					t[j] = k;
					if (s[q] < 0) {
						for (p = j; p >= 0; j = p) {
							match2[j] = k = t[j];
							p = match1[k];
							match1[k] = j;
						}
					}
				}
			}
		}
	}
	return ret;
}
bool cmp(vector<int> X,vector<int > Y)
{
   
   for(int i=0;i<K;++i)
     if(X[i]>=Y[i])
       return false;
       return true;     
}
int main()
{
    int T,CASE,i,j,ans,tmp,prv;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    
    for(CASE=1;CASE<=T;++CASE)
    {
        scanf("%d%d",&N,&K);
        for(i=0;i<N;++i)
          for(A[i].clear(),j=0;j<K;++j)
           { scanf("%d",&tmp);
             A[i].push_back(tmp);
            }
            sort(A,A+N);
        /*    for(i=0;i<N;++i)
              for(j=0;j<K;++j)
                printf("%d%c",A[i][j],j==K-1?'\n':' ');*/
        for(i=0;i<N;++i)
          for(j=i+1;j<N;++j)
           { up[i][j]=cmp(A[i],A[j]);
           // printf("%d-%d :%d\n",i,j,up[i][j]);
            }
          
  /*  memset(mk,0,sizeof(mk));
    for(ans=i=0;i<N;++i)
      if(!mk[i])
      {   ++ans;
          mk[i]=1;
            prv=i;
       for(j=i+1;j<N;++j)
           if(!mk[j]&&up[prv][j])
            {mk[j]=1;prv=j;}
      }*/
     
               
       
      printf("Case #%d: %d\n",CASE,N-hungary( N,N, up));
    }
}
