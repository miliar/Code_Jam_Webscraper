#include <stdio.h>
#include <string.h>
int d[20][501];
int main(){
    freopen("C-large.in","rt",stdin);
    freopen("out2.txt","wt",stdout);
    char codeJam[]="welcome to code jam";
    char test[501];
    int n,i,j,l,k;
    scanf("%d\n",&n);
    for(i=0;i<n;i++){
        for(l=0; 1; l++) {
			scanf("%c", &test[l]);
			if(test[l] == '\n' || test[l] == EOF) {
				test[l] = 0;
				break;
			}
		}
        if(test[0]=='w')d[0][0]=1;
        else d[0][0]=0;
        for(j=1;j<l;j++){
            if(test[j]=='w')d[0][j]=d[0][j-1]+1;
            else d[0][j]=d[0][j-1];
        }
        for(k=1;k<19;k++){
            for(j=k;j<l;j++){
                if(test[j]==codeJam[k])d[k][j]=d[k-1][j-1]+d[k][j-1];
                else d[k][j]=d[k][j-1];
                d[k][j]%=10000;
            }

        }
        printf("Case #%d: %04d\n",i+1,d[k-1][l-1]%10000);
    }
}
