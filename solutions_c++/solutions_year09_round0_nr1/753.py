#include <stdio.h>
#include <string.h>
char dict[5010][20];
char str[1000][450];
int calc[510];
int match(int i, int j){
    int p1,p2=0;
    int found;
    for (p1=0;p1<strlen(dict[i]);p1++){
        if (str[j][p2]==dict[i][p1]){ p2++; continue;}
        if (str[j][p2]=='('){
           p2++;
           found=0;
           while (str[j][p2]!=')'){if (str[j][p2]==dict[i][p1]) found=1; p2++;}
           p2++;
           if (found==0) return 0;
           continue;
        }
        return 0;
    }
    return 1;
}
int main(){
    freopen("alarge.in","r",stdin);
    freopen("out.txt","w",stdout);
    int l,d,n,i,j;
    scanf("%d%d%d ",&l,&d,&n);
    for (i=1;i<=d;i++)
        gets(dict[i]);
    memset(calc,0,sizeof(calc));
    for (i=1;i<=n;i++)
        gets(str[i]);
    for (i=1;i<=d;i++)
        for (j=1;j<=n;j++)
            if (match(i,j)){ calc[j]++;}
    for (i=1;i<=n;i++)
        printf("Case #%d: %d\n",i,calc[i]);
    return 0;
}
    

