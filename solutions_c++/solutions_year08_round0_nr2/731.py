#include <iostream>
#include <fstream>
using namespace std;


struct nodo
{
    int time;
    nodo *sig;
    nodo(int _time)
    {
        sig=NULL;
        time=_time;
    }
};

void push(nodo **principal, nodo *aux)
{
    if (*principal==NULL)
    {
        *principal=aux;        
    }
    else if (aux->time < (*principal)->time)
    {
        aux->sig=(*principal);
        *principal=aux;        
    }
    else
    {
        nodo *temp=(*principal);
        while (temp->sig!=NULL && aux->time > temp->sig->time)
            temp=temp->sig;
        if (temp->sig==NULL)
            temp->sig=aux;
        else
        {
            aux->sig=temp->sig;
            temp->sig=aux;            
        }        
    }
}

nodo* pop(nodo **principal)
{
    nodo *aux=(*principal);
    *principal=(*principal)->sig;
    aux->sig=NULL;
    return aux;
}

ifstream in("B-large.in");
ofstream out("B.out");

int NAB[101][2];
int NBA[101][2];
int N,T,A,B;
int startA,startB;
nodo* NA;
nodo* NB;

void resolver()
{
    int x,y;
    x=y=0;
    startA=startB=0;
        
    while (NAB[x][0]!=14400 || NBA[y][0]!=14400)
    {
        if (NAB[x][0]<NBA[y][0])
        {
            if (NA==NULL)
            {                              
                push(&NB,new nodo(NAB[x][1]+T));
                startA++;
            }
            else if (NA->time <= NAB[x][0])
            {                
                nodo *aux;
                aux=pop(&NA);                
                aux->time=NAB[x][1]+T;
                push(&NB,aux);
            }
            else
            {
                push(&NB,new nodo(NAB[x][1]+T));
                startA++;
            }
            x++;
        }
        else
        {
            if (NB==NULL)
            {                                
                push(&NA,new nodo(NBA[y][1]+T));
                startB++;
            }
            else if (NB->time <= NBA[y][0])
            {                
                nodo *aux;
                aux=pop(&NB);
                aux->time=NBA[y][1]+T;
                push(&NA,aux);
            }
            else
            {
                push(&NA,new nodo(NBA[y][1]+T));
                startB++;                
            }
            y++;
        }        
    }        
    while (NA!=NULL)
        pop(&NA);    
    while (NB!=NULL)
        pop(&NB);    
}

int main()
{
    int x;
    int i,j,min,aux;
    char temp;
    int hour,minute;
    NA=NULL;
    NB=NULL;
    
    in>>N;
    for (x=1; x<=N; x++)
    {
        in>>T;
        in>>A>>B;
        for (i=0; i<A; i++)
        {
            in>>hour>>temp>>minute;
            NAB[i][0]=hour*60+minute;
            in>>hour>>temp>>minute;
            NAB[i][1]=hour*60+minute;
        }
        NAB[i][0]=14400;
        for (i=0; i<B; i++)
        {
            in>>hour>>temp>>minute;
            NBA[i][0]=hour*60+minute;
            in>>hour>>temp>>minute;
            NBA[i][1]=hour*60+minute;
        }
        NBA[i][0]=14400;        
        for (i=0; i<A; i++)
        {
            min=i;
            for (j=i+1; j<A; j++)
            {
                if (NAB[j][0]<NAB[min][0])
                    min=j;
            }
            aux=NAB[i][0];
            NAB[i][0]=NAB[min][0];
            NAB[min][0]=aux;
            aux=NAB[i][1];
            NAB[i][1]=NAB[min][1];
            NAB[min][1]=aux;
        }        
        for (i=0; i<B; i++)
        {
            min=i;
            for (j=i+1; j<B; j++)
            {
                if (NBA[j][0]<NBA[min][0])
                    min=j;
            }
            aux=NBA[i][0];
            NBA[i][0]=NBA[min][0];
            NBA[min][0]=aux;
            aux=NBA[i][1];
            NBA[i][1]=NBA[min][1];
            NBA[min][1]=aux;
        }

        resolver();
        out<<"Case #"<<x<<": "<<startA<<" "<<startB<<endl;
    }

	return 0;
}