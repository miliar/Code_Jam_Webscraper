#include<cstdio>
#include<string.h>

#define REP(i,n) for(int i=0;i<n;i++)

int r,c;
int size;
char tiles[55][55];

void changeTile(int row,int col) {
    if(row+1>=r || col+1>=c) return;
    if(tiles[row][col]!='#') return;
    if(tiles[row+1][col]=='#' && tiles[row+1][col+1]=='#' &&
       tiles[row][col+1]=='#') {
        tiles[row][col]='/';
        tiles[row+1][col]='\\';
        tiles[row][col+1]='\\';
        tiles[row+1][col+1]='/';
    }
}

int main() {
    freopen("D://test.txt","r",stdin);
    freopen("D://testout.txt","w",stdout);
    int t,tempa;
    bool tempb;
    scanf("%d\n",&t);
    REP(i,t) {
        size=0;
        scanf("%d%d",&r,&c);
        printf("Case #%d:\n",i+1);
        REP(j,r) {
            scanf("%s",tiles[j]);
            REP(k,c) {
                if(tiles[j][k]=='#') {
                    ++size;
                }
            }
        }
        if(size%4!=0) {
            printf("Impossible\n");
        }
        else if(size==0) {
            REP(j,r) {
                printf("%s\n",tiles[j]);
            }
        }
        else {
            REP(j,r) {
                REP(k,c) {
                    changeTile(j,k);
                }
            }
            tempb=false;
            REP(j,r) {
                REP(k,c) {
                    if(tiles[j][k]=='#') {
                        tempb=true;
                        break;
                    }
                }
                if(tempb)
                    break;
            }
            if(tempb) {
                printf("Impossible\n");
            }
            else {
                REP(j,r) {
                    printf("%s\n",tiles[j]);
                }
            }
        }
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
