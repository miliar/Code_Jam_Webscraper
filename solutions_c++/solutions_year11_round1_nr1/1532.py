#include <stdio.h>

/*
a->b
*/

int solve(int n,int d,int g){
    if (g==0 && d!=0) return 0;
    if (g==100 && d!=100) return 0;
    if (n>=100) return 1;
    int i,j,oi,oj;
    for (i=1;i<=n;i++){
		if(i * d % 100 == 0){
		    return 1;
		}
    }
    return 0;
}

int c[101][101];

int main(){
    int T,cas;
    int n,d,g;
/*    int i,j;

    for (i=0;i<=100;i++) for (j=0;j<=100;j++){
        // i->j
        if (j==0 && i!=0) c[i][j] = -1;
        else if(j==100 && i!=100) c[i][j] = -1;
        else{
            //
        }
    }
*/
    scanf("%d",&T);
    for (cas=1;cas<=T;cas++){
        scanf("%d%d%d",&n,&d,&g);
        printf("Case #%d: %s\n", cas, solve(n,d,g)?"Possible":"Broken");
    }
    return 0;
}
