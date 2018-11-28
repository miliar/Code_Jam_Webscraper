#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <string>

char str[1000];
int to[100000][2];
int deg[100000];
int pre[100000][10];
int mp[100000];
int u[100000];
int que[100000];
int n,m;

#define M 1000003

inline int ID(int x,int y) {
    return ((x+n)%n)*m+((y+m)%m);
}

int main() {
    int tt,TT,i,j,k,D,x,y,s,p,q,f;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%d %d",&n,&m);
        D = n*m;
        for( i=0; i<n; i++ ) {
            scanf("%s",str);
            for( j=0; j<m; j++ ) {
                if(str[j]=='/') {
                    to[ID(i,j)][0] = ID(i-1,j+1)+D;
                    to[ID(i,j)][1] = ID(i+1,j-1)+D;
                }else if(str[j]=='\\') {
                    to[ID(i,j)][0] = ID(i+1,j+1)+D;
                    to[ID(i,j)][1] = ID(i-1,j-1)+D;
                }else if(str[j]=='-') {
                    to[ID(i,j)][0] = ID(i,j+1)+D;
                    to[ID(i,j)][1] = ID(i,j-1)+D;
                }else {
                    to[ID(i,j)][0] = ID(i-1,j)+D;
                    to[ID(i,j)][1] = ID(i+1,j)+D;
                }
            }
        }
        memset(deg,0,sizeof(deg));
        memset(u,0,sizeof(u));
        memset(mp,0,sizeof(mp));
        for( i=0; i<D; i++ ) {
            pre[to[i][0]][deg[to[i][0]]++] = i;
            pre[to[i][1]][deg[to[i][1]]++] = i;
            mp[to[i][0]]++;
            mp[to[i][1]]++;
        }
        p = -1;
        q = -1;
        for( i=0; i<D; i++ ) {
            if(deg[i+D]==1) {
                que[++p] = i+D;
                u[i+D] = 1;
            }else if(deg[i+D]==0) {
                break;
            }
        }
        if(i<D) {
            printf("Case #%d: %d\n",tt+1,0);
            continue;
        }
        f = 1;
        while(p!=q) {
            x = que[++q];
            for( i=0; i<mp[x]; i++ ) {
                if(!u[pre[x][i]]) {
                    y = pre[x][i];
                    break;
                }
            }
            if(i==mp[x]) {
                f = 0;
                break;
            }
            u[y] = 1;
            if(to[y][0]==x) {
                deg[to[y][1]]--;
                if(deg[to[y][1]]==1) {
                    que[++p] = to[y][1];
                    u[to[y][1]] = 1;
                }
            }else {
                deg[to[y][0]]--;
                if(deg[to[y][0]]==1) {
                    que[++p] = to[y][0];
                    u[to[y][0]] = 1;
                }
            }
        }
        if(!f) {
            printf("Case #%d: %d\n",tt+1,0);
            continue;
        }
        for( i=0; i<D; i++ ) {
            if(!u[i+D] && deg[i+D]!=2) {
                break;
            }
        }
        if(i<D) {
            printf("Case #%d: %d\n",tt+1,0);
            continue;
        }
        s = 1;
        for( i=0; i<D; i++ ) {
            if(!u[i+D]) {
                s = (s*2)%M;
                j = i+D;
                u[j] = 1;
                while(1) {
                    for( k=0; k<mp[j]; k++ ) {
                        if(!u[pre[j][k]]) {
                            k = pre[j][k];
                            break;
                        }
                    }
                    u[k] = 1;
                    if(to[k][0]==j) {
                        k = to[k][1];
                    }else {
                        k = to[k][0];
                    }
                    if(k==i+D) break;
                    j = k;
                    u[j] = 1;
                }
            }
        }
        printf("Case #%d: %d\n",tt+1,s);
    }
    return 0;
}
