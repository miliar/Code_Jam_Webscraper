//---------------------------------------------------------------------------
#include <stdio.h>
#include <mem.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef __int64 int64;

//corregir si se toman mas de 99
const int MAXDIGITS=60;

struct TNumerote
{
char digito[MAXDIGITS];
};

bool operator<(const TNumerote &a,const TNumerote &b)
{
        for (int i=MAXDIGITS-1;i>=0;i--)
        {
                if (a.digito[i]!=b.digito[i])
                {
                        return a.digito[i]<b.digito[i];
                }
        }
        return false;
}

bool operator==(const TNumerote &a,const TNumerote &b)
{
        for (int i=MAXDIGITS-1;i>=0;i--)
        {
                if (a.digito[i]!=b.digito[i])
                {
                        return false;
                }
        }
        return true;
}

bool escero(const TNumerote &a)
{
        for (int i=0;i<MAXDIGITS;i++)
        {
                if (a.digito[i]!=0)
                {
                        return false;
                }
        }
        return true;
}

TNumerote Resta(TNumerote a,TNumerote b)
{
        TNumerote res;
        memset(res.digito,0,sizeof(res.digito));
        for (int i=0;i<(MAXDIGITS-1);i++)
        {
                res.digito[i]=a.digito[i]-b.digito[i];
                if (res.digito[i]<0)
                {
                        res.digito[i]+=10;
                        a.digito[i+1]--;
                }
        }
        return res;
}

double NumeroteAdouble(const TNumerote &a)
{
        double res=0;
        for (int i=MAXDIGITS-1;i>=0;i--)
        {
                res*=10.0;
                res+=a.digito[i];
        }
        return res;
}

TNumerote Multiplica(const TNumerote &a, const TNumerote &b)
{
        TNumerote res;
        memset(res.digito,0,sizeof(res.digito));
        for (int i=0;i<MAXDIGITS;i++)
        {
                char carro=0;
                for (int j=0;(j+i)<MAXDIGITS;j++)
                {
                        carro+=(a.digito[j]*b.digito[i])+res.digito[i+j];
                        res.digito[i+j]=carro%10;
                        carro/=10;
                }
        }
        return res;
}

TNumerote Suma(const TNumerote &a, const TNumerote &b)
{
        TNumerote res;
        char carro=0;
        for (int i=0;i<MAXDIGITS;i++)
        {
                carro+=a.digito[i]+b.digito[i];
                res.digito[i]=carro%10;
                carro/=10;
        }
        return res;
}

TNumerote Residuo(TNumerote a,TNumerote b)
{
        //computes a=q*b+r and returns r
        /*if (a<b)
        {
                return a;
        }
        */
        //convert to double and start from there
        double da=NumeroteAdouble(a);
        double db=NumeroteAdouble(b);
        double division=da/db;
        char cadena[102];
        sprintf(cadena,"%0101.0lf",division);
        TNumerote q;
        for (int i=0;i<MAXDIGITS;i++)
        {
                q.digito[i]=(cadena[100-i]-'0');
        }
        TNumerote qb=Multiplica(b,q);
        while (qb<a)
        {
                qb=Suma(qb,b);
        }
        while (a<qb)
        {
                qb=Resta(qb,b);
        }
        return Resta(a,qb);
}

TNumerote GDC(TNumerote a,TNumerote b)
{
        if (escero(a))
        {
                return b;
        }
        return GDC(Residuo(b,a),a);
}

//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
        FILE *entrada=fopen("entrada.txt","r");
        FILE *salida=fopen("salida.txt","w");
        int T;
        fscanf(entrada,"%d",&T);
        vector<TNumerote> Num;
        for (int t=1;t<=T;t++)
        {
                Num.clear();
                int N;
                char basura;
                fscanf(entrada,"%d%c",&N,&basura);
                Num.resize(N);
                for (int i=0;i<N;i++)
                {
                        char leido[50];
                        memset(Num[i].digito,0,sizeof(Num[i].digito));
                        int longitud=0;
                        while (true)
                        {
                                fscanf(entrada,"%c",&basura);
                                if ((basura>='0')&&(basura<='9'))
                                {
                                        leido[longitud]=basura;
                                        longitud++;
                                }
                                else
                                {
                                        for (int j=0;j<longitud;j++)
                                        {
                                                Num[i].digito[j]=leido[(longitud-j)-1]-'0';
                                        }
                                        break;
                                }
                        }
                }
                sort(Num.begin(),Num.end());
                TNumerote GDCcompleto=Resta(Num[1],Num[0]);
                for (int i=2;i<N;i++)
                {
                        TNumerote NuevaDif=Resta(Num[i],Num[i-1]);
                        GDCcompleto=GDC(GDCcompleto,NuevaDif);
                }
                TNumerote falta=Resta(GDCcompleto,Residuo(Num[0],GDCcompleto));
                if (falta==GDCcompleto)
                {
                        fprintf(salida,"Case #%d: 0\n",t);
                }
                else
                {
                        fprintf(salida,"Case #%d: ",t);
                        int inicial=MAXDIGITS-1;
                        while (falta.digito[inicial]==0)
                        {
                                inicial--;
                        }
                        while (inicial>=0)
                        {
                                fprintf(salida,"%c",falta.digito[inicial]+'0');
                                inicial--;
                        }
                        fprintf(salida,"\n");
                }
        }

        fclose(entrada);
        fclose(salida);
        return 0;
}
//---------------------------------------------------------------------------

