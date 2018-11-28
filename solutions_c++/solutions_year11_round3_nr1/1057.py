#include<stdio.h>

int main(){

    int t,r,c;
    char tile[52][52],cannot=0;
    scanf("%d",&t);
    for(int casenum=1;casenum<=t;++casenum)
    {
        cannot=0;
        scanf("%d %d",&r,&c);
        for(int i=0;i<r;i++)
            scanf("%s",tile[i]);


        for(int i=0;i<r;i++)
            for(int j=0;j<c;j++){
                if(tile[i][j]=='#'){
                    if(tile[i+1][j]=='#'&&tile[i][j+1]=='#'&&tile[i+1][j+1]=='#'&&i<r-1&&j<c-1){
                        tile[i][j]='/';
                        tile[i+1][j]='\\';
                        tile[i][j+1]='\\';
                        tile[i+1][j+1]='/';
                    }
                    else{

                        cannot=1;
                        i=r;
                        break;
                    }

                }

            }


        printf("Case #%d:\n",casenum);
        if(cannot)
            printf("Impossible\n");
        else
            for(int i=0;i<r;i++)
                printf("%s\n",tile[i]);
    }

    return 0;
}
