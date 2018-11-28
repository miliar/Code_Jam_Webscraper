#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>

using namespace std;

char wd[20000][20];
int len[20000];
int code[20000][26];
char str[100];
int n;

class WD{
    public:
        int x,y,c;
};

WD c[20000];
int id[1024];
int tb[1024];
WD tmp[20000];
int buc[20000];

int cmp1(const WD& a,const WD& b) {
    return len[a.x]<len[b.x];
}

inline void arr(int L,int R,int d) {
    int i,n;
    n = R-L;
    for( i=0; i<n; i++ ) {
        buc[i] = 0;
    }
    for( i=L; i<R; i++ ) {
        tmp[i] = c[i];
        buc[c[i].y-d]++;
    }
    for( i=1; i<n; i++ ) {
        buc[i]+=buc[i-1];
    }
    for( i=L; i<R; i++ ) {
        c[--buc[tmp[i].y-d]+L] = tmp[i];
    }
}

int solve() {
    int i,j,k,h,r,pid,z,kk,d,x,tr,md;
    for( i=0; i<n; i++ ) {
        c[i].x = i;
        c[i].c = 0;
    }
    sort(c,c+n,cmp1);
    r = 0;
    c[0].y = 0;
    for( i=1; i<n; i++ ) {
        if(len[c[i].x]!=len[c[i-1].x]) {
            r++;
        }
        c[i].y = r;
    }
    r++;
    z = 0;
    memset(id,-1,sizeof(id));
    pid = 0;
    for( z=0; z<26; z++ ) {
        x = str[z]-'a';
        for( i=1,j=0; i<=n; i++ ) {
            if(i!=n && c[i].y==c[i-1].y) continue;
            if(j==i-1) {
                j = i;
                continue;
            }
            tr = r;
            for( k=j; k<i; k++ ) {
                if(code[c[k].x][x]) break;
            }
            if(k<i) {
                for( k=j; k<i; k++ ) {
                    d = code[c[k].x][x];
                    if(!d) {
                        c[k].c++;
                    }
                    if(id[d]!=pid) {
                        id[d] = pid;
                        tb[d] = r;
                        c[k].y = r++;
                    }else {
                        c[k].y = tb[d];
                    }
                }
                arr(j,i,tr);
            }
            pid++;
            j = i;
        }
    }
    md = -1;
    for( i=0; i<n; i++ ) {
        //printf("%s %d\n",wd[c[i].x],c[i].c);
        //fflush(0);
        if(c[i].c>md) {
            md = c[i].c;
            j = c[i].x;
        }else if(c[i].c==md && c[i].x<j) {
            j = c[i].x;
        }
    }
    return j;
}

int main() {
    int tt,TT,m,i,j,k;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d %d",&n,&m);
        fgets(wd[0],15,stdin);
        for( i=0; i<n; i++ ) {
            fgets(wd[i],15,stdin);
            len[i] = strlen(wd[i])-1;
            wd[i][len[i]] = 0;
            for( j='a'; j<='z'; j++ ) {
                code[i][j-'a'] = 0;
                for( k=0; wd[i][k]; k++ ) {
                    if(wd[i][k]==j) {
                        code[i][j-'a']|=(1<<k);
                    }
                }
            }
        }
        printf("Case #%d:",tt+1);
        for( i=0; i<m; i++ ) {
            fgets(str,50,stdin);
            str[strlen(str)-1] = 0;
            printf(" %s",wd[solve()]);
        }
        printf("\n");
    }
    return 0;
}
