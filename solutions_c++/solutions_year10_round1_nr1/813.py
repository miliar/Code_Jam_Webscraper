#include <stdio.h>
#define MAX 60

int n,k;
char before[MAX][MAX];
char after[MAX][MAX];

void print(){
    int i;
    for(i=0;i<n;i++)
        printf("%s\n", after[i]);
    printf("\n");
}
int count(char c){
    int i,j,l,m,cnt;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(after[i][j] == c){
                for(cnt=0,l=j; l<n&&after[i][l]==c ;l++,cnt++);
                if(cnt>=k)
                    return 1;
                for(cnt=0,m=i; m<n&&after[m][j]==c ;m++,cnt++);
                if(cnt>=k)
                    return 1;
                for(cnt=0,l=j,m=i; l<n&&m<n&&after[m][l]==c ;l++,m++,cnt++);
                if(cnt>=k)
                    return 1;
                for(cnt=0,l=j,m=i; l<n&&m>=0&&after[m][l]==c ;l++,m--,cnt++);
                if(cnt>=k)
                    return 1;
            }
        }
    }
    return 0;
}
void solve(){
    int i,j,l,m,r,b;
    scanf("%d %d", &n, &k);
    for(i=0;i<n;i++)
        scanf("%s", before[i]);
    /* Rotate */
    for(i=0;i<n;i++){
        for(j=0;j<n;j++)
            after[i][j] = before[n-1-j][i];
    }
    /* Gravity */
    for(j=0;j<n;j++){
        for(i=n-1;i>=0;i--){
            if(after[i][j] != '.')
                continue;
            for(l=i;l>=0 && after[l][j] == '.';l--);
            for(m=i;l>=0;l--,m--)
                after[m][j] = after[l][j];
            for(;m>=0;m--)
                after[m][j] = '.';
        }
    }
    /* Count R*/
    r = count('R');
    b = count('B');
    if(r&&b)    printf("Both");
    else if(r)  printf("Red");
    else if(b)  printf("Blue");
    else        printf("Neither");
}
int main(){
    int i,T;
    scanf("%d", &T);
    for(i=1;i<=T;i++){
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
    return 0;
}
