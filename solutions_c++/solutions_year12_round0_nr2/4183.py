#include<cstdio>
#include<cmath>
#define in "in.in"
#define out "out.out"
using namespace std;

int cazuri,nrr,p,n;

void verifica(int);

int main()
{

    freopen(in,"r",stdin);
    freopen(out,"w",stdout);

    int _n,i,aux;
    scanf("%d",&_n);
    int _i;
    for(_i=1;_i<=_n;_i++)
    {
        scanf("%d %d %d",&nrr,&p,&n);
        for(i=1;i<=nrr;i++)
        {
            scanf("%d",&aux);
            if(aux)
                verifica(aux);
            else
            if(n==0 && aux==0)
                cazuri++;
        }
        printf("Case #%d: %d \n",_i,cazuri);
        cazuri=0;
    }
}

void verifica(int nro)
{
    int nr1,nr2,nr3;
    if(nro>=n){
        nr1=n;
        nro-=n;
        nr2=nro/2;
        nr3=nro-nr2;
        if(nr1<=nr2 && nr1<=nr3)
            cazuri++;
        else
            if((nr1<=nr3 && nr1==nr2+1) || (nr1<=nr2 && nr1==nr3+1))
            cazuri++;
            else
                if(nr1==nr2+1 && nr1==nr3+1){
                        cazuri++;
                }
                else
                    if((nr1==nr2+1 || nr1==nr2+2) && (nr1==nr3+1 || nr1==nr3+2) && p){
                        cazuri++;
                        p--;
                    }
    }
}
