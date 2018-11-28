#include<stdio.h>

int main() {
    char cc[36][4],dd[28][3],list[101],nn[101];
    int c,c1,cnt,d,d1,i,j,k,len,n,t;
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++) {
        scanf("%d",&c);for(i=0;i<c;i++)scanf("%s",&cc[i]);
        scanf("%d",&d);for(i=0;i<d;i++)scanf("%s",&dd[i]);
        scanf("%d",&n);scanf("%s",&nn);
        //printf("c:");for(i=0;i<c;i++){if(i)printf(",");printf("%s",cc[i]);}printf("\n");
        //printf("d:");for(i=0;i<d;i++){if(i)printf(",");printf("%s",dd[i]);}printf("\n");
        //printf("n:%s\n",nn);
        len=0;
        for(i=0;i<n;i++) {
            list[len]=nn[i];len++;
            //combine
            for(j=0;j<c;j++) {
                c1=0;
                if(len>=2) {
                    if((list[len-1]==cc[j][0])&&(list[len-2]==cc[j][1]))c1=1;
                    if((list[len-2]==cc[j][0])&&(list[len-1]==cc[j][1]))c1=1;
                    if(c1) {
                        list[len-1]=0;
                        list[len-2]=cc[j][2];
                        len--;
                    }
                }
            }
            //oppose
            for(j=0;j<d;j++) {
                d1=0;
                for(k=0;k<len-1;k++) {
                    if((list[len-1]==dd[j][0])&&(list[k]==dd[j][1]))d1=1;
                    if((list[k]==dd[j][0])&&(list[len-1]==dd[j][1]))d1=1;
                    if(d1) {
                        list[0]=0;
                        len=0;
                    }
                }
            }
        }
        printf("Case #%d: [",cnt);
        for(i=0;i<len;i++) {
            if(i)printf(", ");
            printf("%c",list[i]);
        }
        printf("]\n");
    }
    //while(1);
    return 0;
}
