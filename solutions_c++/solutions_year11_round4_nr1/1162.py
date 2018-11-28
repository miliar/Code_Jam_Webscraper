#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

typedef struct {
        int b, e, a;
}walkway;

int T, X, S, R, t, N, c, nal;
walkway arr[1010];

int cmp( const void *a, const void *b )
{
    return ((walkway*)a)->a - ((walkway*)b)->a;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    bool nr;
    int i, j, k;
    double ct, lt, ans;
    
    for ( scanf("%d",&T); T; T-- ) {
        for ( scanf("%d%d%d%d%d",&X,&S,&R,&t,&N), nal = X, i = 0; i < N; i++ ) {
            scanf("%d%d%d",&arr[i].b,&arr[i].e,&arr[i].a);
            nal -= (arr[i].e-arr[i].b);
        }
        
        qsort(arr,N,sizeof(arr[0]),cmp);
        nr = 0;
        ans = 0;
        ct = (double)nal / R;
        if ( ct > (double)t ) {
            ans = t + (nal-t*R)/(double)S;
            nr = 1;
        }
        else {
            lt = (double)t - ct;
            ans = ct;
        }
        //printf("%.3lf\n",ans);
        for ( i = 0; i < N; i++ ) {
            if ( nr ) {
                ans += (arr[i].e-arr[i].b)/(double)(S+arr[i].a);
            }
            else {
                ct = (double)(arr[i].e-arr[i].b)/(R+arr[i].a);
                if ( ct > lt ) {
                    ans += lt + (arr[i].e-arr[i].b-lt*(R+arr[i].a))/(double)(S+arr[i].a);
                    nr = 1;
                }
                else {
                    lt -= ct;
                    ans += (double)(arr[i].e-arr[i].b)/(double)(R+arr[i].a);
                }
            }
        }
        
        printf("Case #%d: %.9lf\n",++c,ans);
    }
    
    return 0;
}

