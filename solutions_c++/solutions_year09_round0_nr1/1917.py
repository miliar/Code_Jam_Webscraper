#include<stdio.h>
int two[32];
struct data{
    char s[19];
}a[5010];
main(){
    int L,D,N,i,j,k,r,x[19],an;
    char s[400];
    two[0]=1;
    for(i=1;i<32;i++)two[i]=two[i-1]<<1;
    scanf("%d %d %d",&L,&D,&N);
    for(i=0;i<D;i++)scanf("%s",a[i].s);
    for(k=1;k<=N;k++){
        an=0;
        scanf("%s",s);
        for(i=0,j=0;i<L;i++){
            if(s[j]=='('){
                x[i]=0;
                for(j++;s[j]!=')';j++)x[i]+=two[s[j]-'a'];
                j++;
            }
            else
                x[i]=two[s[j++]-'a'];
        }
        for(i=0;i<D;i++){
            for(j=0;j<L;j++)
                if((x[j]&two[a[i].s[j]-'a'])==0)break;
            if(j==L)an++;
        }
        printf("Case #%d: %d\n",k,an);
    }
}
