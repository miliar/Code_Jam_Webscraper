#include<stdio.h>
#include<string.h>
const int N=4;
char s[5][5];
int ca;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j,s1,s2,s3,s4;
    int flag,cc=0;
    scanf("%d",&ca);
    while (ca--){
        printf("Case #%d: ",++cc);
        s1=s2=s3=s4=0;
        for (i=0;i<N;i++) scanf("%s",s[i]);
        for (i=0;i<N;i++)
            for (j=0;j<N;j++)
                if (s[i][j]=='.') s4++;
        flag=0;
        for (i=0;i<N;i++){
            s1=s2=s3=0;
            for (j=0;j<N;j++){
                if (s[i][j]=='T') s3++;
                else if (s[i][j]=='X') s1++;
                else if (s[i][j]=='O') s2++;
            }
            if ((s1==3&&s3==1)||s1==4){printf("X won\n");flag=1;break;}
            if ((s2==3&&s3==1)||s2==4){printf("O won\n");flag=1;break;}
        }
        if (flag) continue;
        for (j=0;j<N;j++){
            s1=s2=s3=0;
            for (i=0;i<N;i++){
                if (s[i][j]=='T') s3++;
                else if (s[i][j]=='X') s1++;
                else if (s[i][j]=='O') s2++;
            }
            if ((s1==3&&s3==1)||s1==4){printf("X won\n");flag=1;break;}
            if ((s2==3&&s3==1)||s2==4){printf("O won\n");flag=1;break;}
        }
        if (flag) continue;
        s1=s2=s3=0;
        for (i=0;i<N;i++){
            for (j=0;j<N;j++){
                if (i!=j) continue;
                if (s[i][j]=='T') s3++;
                else if (s[i][j]=='X') s1++;
                else if (s[i][j]=='O') s2++;
            }
            if ((s1==3&&s3==1)||s1==4){printf("X won\n");flag=1;break;}
            if ((s2==3&&s3==1)||s2==4){printf("O won\n");flag=1;break;}
        }
        if (flag) continue;  
        s1=s2=s3=0;
        for (i=0;i<N;i++){
            for (j=0;j<N;j++){
                if (i+j!=N-1) continue;
                if (s[i][j]=='T') s3++;
                else if (s[i][j]=='X') s1++;
                else if (s[i][j]=='O') s2++;
            }
            if ((s1==3&&s3==1)||s1==4){printf("X won\n");flag=1;break;}
            if ((s2==3&&s3==1)||s2==4){printf("O won\n");flag=1;break;}
        }
        if (flag) continue;
        if (s4>0) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    //while (1);
    return 0;
}
