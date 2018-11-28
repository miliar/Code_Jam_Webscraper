#include <stdio.h>
#define MAXN 2000
#define LOGN 20

int v[MAXN][LOGN], marc[MAXN];
long long c[MAXN];
int n, pot;

struct par{
       int soma, pos;
};

par busc( int p, int sum ){
    int i;
    par ret;
    ret.soma=ret.pos=0;
    for( i=pot ; i>=0 ; i-- ){
         if( sum>=v[p][i] && (ret.pos+(1<<i))<=n ){
             ret.soma+=v[p][i];
             sum-=v[p][i];
             ret.pos+=(1<<i);
             p=(p+(1<<i))%n;
         }
    }
    return ret;
}

int main(){
    int t, r, k;
    int i, j, l, sum;
    int ult, q , pos;
    par ret;
    FILE *saida = fopen("theme.out","w");
    scanf("%d",&t);
    for( i=1 ; i<=t ; i++ ){
         scanf("%d %d %d",&r,&k,&n);
         sum=0;
         for( j=0 ; j<n ; j++ ){
              scanf("%d",&v[j][0]);
              sum+=v[j][0];     
         }
         fprintf(saida,"Case #%d: ",i);
         c[0]=0;
         for( j=1 ; (1<<j)<=n ; j++ )
              for( l=0 ; l<n ; l++ )
                   v[l][j]=v[l][j-1]+v[(l+(1<<(j-1)))%n][j-1];
         pot=j-1;
         for( l=0 ; l<n ; l++ )
              marc[l]=0;
         ult=0;
         j=0;
         while( marc[ult]==0 ){
                marc[ult]=j+1;
                ret=busc(ult,k);
                ult=(ult+ret.pos)%n;
                j++;
                c[j]=c[j-1]+ret.soma;
                //printf("%I64d ",c[j]);
                //printf("%d - ult:%d , c:%I64d\n",j,ult,c[j]);
         }
         //printf("\n");
         if( r<=j )
             fprintf(saida,"%I64d\n",c[r]);
         else{
              r-=j;
              q=j-marc[ult]+1;
              pos=marc[ult];
              fprintf(saida,"%I64d\n",c[j] + (r/q)*(c[j]-c[pos-1]) + c[pos+r%q-1]-c[pos-1]);
              //printf("pos: %d, q: %d\n",pos,q);
         }
    }
    fclose(saida);
    //scanf("%d",&i);
    return 0;   
}
