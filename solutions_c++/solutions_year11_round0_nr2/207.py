#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;
#define abs(a) ((a)>=0?(a):-(a))
#define max(a,b) (a>b?a:b)

int mar[30][30];
int mat[30][30];

int main(){
    int debug = 1;
    if( debug ){
        freopen("B-large.in","r",stdin);
        freopen("B-large.out","w",stdout);
    }
    int Cas, c, d, n;
    scanf("%d",&Cas);
    for(int cas=1; cas<=Cas; ++cas){
        memset(mar,0,sizeof(mar));
        memset(mat,0,sizeof(mat));
        scanf("%d",&c);
        while( c-- ){
            char st[10];
            scanf("%s",&st);
            mar[st[0]-'A'+1][st[1]-'A'+1] = mar[st[1]-'A'+1][st[0]-'A'+1] = st[2] - 'A' +1;
        }
        scanf("%d",&d);
        while( d-- ){
            char st[10];
            scanf("%s",&st);
            mat[st[0]-'A'+1][st[1]-'A'+1] = mat[st[1]-'A'+1][st[0]-'A'+1] = 1;
        }
        int f[111], l = 0;
        char st[111];
        scanf("%d",&n);
        scanf("%s",&st);
        for(int i=0; i<n; ++i){
            if( l && mar[st[i]-'A'+1][f[l]] ){
                f[l] = mar[st[i]-'A'+1][f[l]];
            }else{
                f[++l] = st[i]-'A'+1;
                for(int j=1; j<=l-1; ++j)
                  if( mat[st[i]-'A'+1][f[j]] ) l = 0;
            }
        }
        printf("Case #%d: [",cas);
        for(int i=1; i<=l; ++i){
            if( i==1 ) printf("%c",f[i]+'A'-1);
            else printf(", %c",f[i]+'A'-1);
        }
        printf("]\n");
    }
    if( debug ){
        fclose(stdin);
        fclose(stdout);
    }
    return 0;
}
