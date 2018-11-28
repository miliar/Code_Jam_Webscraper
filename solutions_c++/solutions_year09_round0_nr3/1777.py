#include<cstdio>
const int N=505,M=20;
char test[]="welcome to code jam";
int s[N][M];
char tmp[N];
main()
{
    int i,j,k,l,T,C=1;
    scanf("%d%*c",&T);
    while(T--){
        gets(tmp);
        for(i=0;tmp[i];i++)
            for(j=0;j<M;j++)
                s[i][j]=0;
        s[0][0]=1;
        for(i=0;tmp[i];i++)
            for(k=i;tmp[k];k++)
                for(j=0;j<M;j++)
                    if(tmp[k]==test[j])(s[k][j+1]+=s[i][j])%=1000;
        for(i=1;tmp[i];i++)
            (s[i][19]+=s[i-1][19])%=1000;

        printf("Case #%d: %04d\n",C++,s[i-1][19]);
    }
}
