#include <stdio.h>
#include <stdlib.h>

struct trip{
    int st,ed;
}ta[110],tb[110];
int mark[110];
int cmp1(const void *a,const void *b){
    return ((trip*)a)->st - ((trip*)b)->st;
}
int cmp2(const void *a,const void *b){
    return ((trip*)a)->ed - ((trip*)b)->ed;
}
int conv(char *tmp){
    int h=0,m=0;
    h=(tmp[0]-'0')*10+(tmp[1]-'0');
    m=(tmp[3]-'0')*10+(tmp[4]-'0');
    return h*60+m;
}

int main(void)
{
    int i, j, n, a, b, c=1;
    char tmp1[10],tmp2[10];
    scanf("%d", &n);
    while( n-- ){
        int t,na,nb;
        scanf("%d%d%d",&t,&na,&nb);
        for( i=0; i<na; i++){
            scanf("%s%s",tmp1,tmp2);
            ta[i].st = conv(tmp1);
            ta[i].ed = conv(tmp2);
        }
        for( i=0; i<nb; i++ ){
            scanf("%s%s",tmp1,tmp2);
            tb[i].st = conv(tmp1);
            tb[i].ed = conv(tmp2);
        }
        a=na,b=nb;
        qsort(ta,na,sizeof(ta[0]),cmp1);
        qsort(tb,nb,sizeof(tb[0]),cmp2);
        for( i=0; i<110; i++ )mark[i]=0;
        for( i=0; i<nb; i++ ){
            for( j=0; j<na; j++ ){
                if( !mark[j]&&tb[i].ed+t<=ta[j].st ){
                    a--;
                    mark[j]=1;
                    break;
                }
            }
        }
        for( i=0; i<110; i++ ) mark[i]=0;
        qsort(tb,nb,sizeof(tb[0]),cmp1);
        qsort(ta,na,sizeof(ta[0]),cmp2);
        for( i=0; i<na; i++ ){
            for( j=0; j<nb; j++ ){
                if( !mark[j]&&ta[i].ed+t<=tb[j].st ){
                    b--;
                    mark[j]=1;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",c++,a,b);
    }
    return 0;
}
