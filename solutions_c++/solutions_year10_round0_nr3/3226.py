#include <cstdio>

#define max 1000

typedef struct
{
    int val;
    int pri;
}tipofamilia;

tipofamilia heap[max];
int t,i,r,k,n,p=0,u=0,total;

void debug()
{
    for (int j=1; j<=u; j++)
    {
        printf("%d %d\n",heap[j].val,heap[j].pri);
    }
}

void swap(tipofamilia &i,tipofamilia &j)
{
    tipofamilia aux;
    aux=i;
    i=j;
    j=aux;
}

void inserta()
{
    int pos,papa;
    pos=u;
    while (pos>1)
    {
        papa=pos/2;
        if (heap[pos].pri<heap[papa].pri)
        {
            swap(heap[pos],heap[papa]);
            pos=papa;
        }
        else
        {
            pos=0;
        }
    }
}

void reacomoda()
{
    int izq,der,papa;
    bool band=false;
    papa=1;
    while (band==false && (papa*2)<=u && u>0)
    {
        izq=papa*2;
        der=izq+1;
        if (der>u)
            der=izq;
        if (heap[izq].pri<heap[der].pri)
        {
                if (heap[izq].pri<heap[papa].pri)
                {
                      swap(heap[izq],heap[papa]);
                      papa=izq;
                }
                else
                   band=true;
        }
        else
        {
            if (heap[der].pri<heap[papa].pri)
            {
                    swap(heap[der],heap[papa]);
                    papa=der;
            }
            else
               band=true;
        }
    }
}

void elimina(tipofamilia &estado)
{
    estado=heap[1];
    swap(heap[1],heap[u]);
    u--;
    reacomoda();
}

void prueba()
{
      tipofamilia d;
      bool band;
      int aux,g;
      for (int j=1; j<=r; j++)
      {
          aux=0;
          band=false;
          g=0;
          while (aux<k && g!=n && band==false)
          {
               if ((heap[1].val+aux)<=k)
               {
                   aux+=heap[1].val;
                   elimina(d);
               //    debug();
                   u++;
                   p++;
                   heap[u]=d;
                   heap[u].pri=p;
                   inserta();
               }
               else
                  band=true;
               g++;
          }
          total+=aux;
      }
}

int main()
{
    scanf("%d",&t);
    for (i=1; i<=t; i++)
    {
        total=0;
        u=0;
        p=0;
        scanf("%d %d %d",&r,&k,&n);
        for (int j=1; j<=n; j++)
        {
            u++;
            scanf("%d",&heap[u].val);
            p++;
            heap[u].pri=p;
            inserta();
        }
        //debug();
        prueba();
        printf("Case #");
        printf("%d",i);
        printf(": ");
        printf("%d\n",total);
    }
}
