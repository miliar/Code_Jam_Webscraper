#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;
#define abs(a) ((a)>=0?(a):-(a))
#define max(a,b) (a>b?a:b)

int main(){
    int debug = 1;
    if( debug ){
        freopen("A-large.in","r",stdin);
        freopen("A-large.out","w",stdout);
    }
    int Cas, n;
    scanf("%d",&Cas);
    for(int cas=1; cas<=Cas; ++cas){
        scanf("%d",&n);
        int s[2] = {1,1}, t[2] = {0,0}, ob;
        char flag = ' ';
        for(int i=1; i<=n; i++){
            char color;
            int num;
            scanf(" %c %d",&color,&num);
            if( flag == ' ' ) flag = color;
            if( color=='O' ) ob = 0;
            else ob = 1;
            t[ob] += abs(num-s[ob]) + 1;
            s[ob] = num;
            if( flag != color ){
                if( t[ob] <= t[(ob+1)&1] ) t[ob] = t[(ob+1)&1] + 1;
                flag = color;
            }
        }
        printf("Case #%d: %d\n",cas,max(t[0],t[1]));
    }
    if( debug ){
        fclose(stdin);
        fclose(stdout);
    }
    return 0;
}
