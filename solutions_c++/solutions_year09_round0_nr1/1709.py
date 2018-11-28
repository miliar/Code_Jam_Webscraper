#include<cstdio>
char w[5000][19],tmp[9999],c[19][256];
main()
{
    int i,j,k,l,n,m,L,sum,C=1;
    while(scanf("%d %d %d",&L,&n,&m)==3){
        for(i=0;i<n;i++)
            scanf("%s",w[i]);
        for(i=0;i<m;i++){
            scanf("%s",tmp);
            for(j=0;j<L;j++)
                for(k=0;k<256;k++)
                    c[j][k]=0;
            for(j=k=0;tmp[j];j++,k++)
                if(tmp[j]=='(')
                    for(j++;tmp[j]!=')';j++)
                        c[k][tmp[j]]=1;
                else c[k][tmp[j]]=1;
            for(j=sum=0;j<n;j++){
                for(k=0;k<L;k++)
                    if(!c[k][w[j][k]])break;
                sum+=(k>=L);
            }
            printf("Case #%d: %d\n",C++,sum);
        }
    }
}
