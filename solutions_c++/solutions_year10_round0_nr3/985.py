//---------------------------------------------------------------------------
#include <stdio.h>
#include <mem.h>

typedef __int64 int64;

//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
        FILE *entrada=fopen("C-large.in","r");
        FILE *salida=fopen("salida.txt","w");
        int T;
        fscanf(entrada,"%d",&T);
        int64 g[1000];
        int64 suma[1000];
        char visitado[1000];
        int siguiente[1000];
        for (int t=1;t<=T;t++)
        {
                int64 R,k,total=0;
                int N;
                memset(suma,0,sizeof(suma));
                memset(visitado,0,sizeof(visitado));
                fscanf(entrada,"%I64d %I64d %d",&R,&k,&N);
                for (int i=0;i<N;i++)
                {
                        fscanf(entrada,"%I64d",&g[i]);
                        total+=g[i];
                }
                if (total<=k)
                {
                        total*=R;
                        fprintf(salida,"Case #%d: %I64d\n",t,total);
                        continue;
                }
                for (int i=0;i<N;i++)
                {
                        int extra=0;
                        while((suma[i]+g[(extra+i)%N])<=k)
                        {
                                suma[i]+=g[(extra+i)%N];
                                extra++;
                        }
                        siguiente[i]=(i+extra)%N;
                }
                int current=0;
                total=0;
                while (R>0)
                {
                        total+=suma[current];
                        visitado[current]=1;
                        current=siguiente[current];
                        R--;
                        if (visitado[current])
                        {
                                int inicial=current;
                                int pasos=0;
                                int64 porciclo=0;
                                //repeat the cycle
                                do
                                {
                                        total+=suma[current];
                                        porciclo+=suma[current];
                                        current=siguiente[current];
                                        pasos++;
                                        R--;
                                }while ((current!=inicial)&&(R>0));
                                total+=(R/pasos)*porciclo;
                                R=R%pasos;
                                while (R>0)
                                {
                                        total+=suma[current];
                                        current=siguiente[current];
                                        R--;
                                }
                        }
                }
                fprintf(salida,"Case #%d: %I64d\n",t,total);
        }

        fclose(entrada);
        fclose(salida);
        return 0;
}
//---------------------------------------------------------------------------
 