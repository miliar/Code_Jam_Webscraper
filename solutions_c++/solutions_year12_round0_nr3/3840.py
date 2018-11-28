#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define mpair make_pair
#define pii pair<int,int>
#define MM(a,b) memset(a,b,sizeof(a));
typedef long long lld;
typedef unsigned long long u64;
template<class T> bool up_max(T& a,const T& b){return b>a? a=b,1 : 0;}
template<class T> bool up_min(T& a,const T& b){return b<a? a=b,1 : 0;}
#define maxn

int len, a, b;
char A[10];

int solve(int x){
    char ch[10], j=0;
    while( x ) ch[j++]= (x%10 + '0'), x/= 10;
    ch[j]= '\0';
    reverse( ch, ch+j );
    /// puts( ch );   /// ( O(10) );

    char t1[10], t2[10];
    strcpy( t1, ch );

    int i, ret= 0;
    char aa[10][10];
    for(i=1;i<len;++i){
        copy( t1+1, t1+len, t2 );
        t2[ len-1 ]= t1[0]; t2[ len ]= '\0';
        if( (strcmp( A, t2 ) <= 0) && (strcmp( t2, ch ) < 0) ){
            strcpy( aa[++ret], t2 );
        }
        strcpy( t1, t2 );
    }
    bool ff[10];
    int cc= 0;
    for(i=1;i<=ret;++i) ff[i]= 0;
    for(i=1;i<ret;++i){
        if( ff[i]==1 ) continue;
        for(j=i+1;j<=ret;++j){
            if( strcmp( aa[i],aa[j] ) == 0 ){
                ++cc, ff[j]= 1;
            }
        }
    }
    return ret-cc;
}

int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T, TT=0,i;
    cin>>T;
    while(T--){
        scanf("%d%d", &a, &b);
        len= 0;
        int t= a; while(t) t/= 10, len++;
        t= a, i=0;
        while(t) A[i++]= (t%10+'0'), t/= 10;
        A[i]= '\0';
        reverse( A, A+i );
        // puts(A);

        int ans= 0;
        for(i=a+1;i<=b;++i){
            int tt= solve(i);
            //printf("%d  %d\n", i, tt );
            ans+= tt;
        }

        printf("Case #%d: %d\n", ++TT, ans);
    }
}
