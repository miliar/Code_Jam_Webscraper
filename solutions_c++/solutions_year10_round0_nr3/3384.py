#include <stdio.h>
#include <stdlib.h>
#define NULO -1

typedef struct No
{
    int valor;
    struct No* prox;
} No;


typedef struct lista
{
    No* prim;
} lista;


void put(lista *l, int v)
{
	No *novo;
	No *it;

	novo = (No*)malloc(sizeof(No));

	novo->valor = v;
	// inicializar nó

	novo->prox = NULL;
	if( l->prim == NULL )
		l->prim = novo;
	else
	{
        it = l->prim;
		while( it->prox != NULL )
			it = it->prox;
		it->prox = novo;
	}
}


void pop(lista *l)
{
	No *it;

    it = l->prim;
    if(l->prim!=NULL)
    {
        l->prim = l->prim->prox;
    }
    else

    free(it);
    // retirar elemento 1
}


int peek(lista *l)
{
	if(l->prim!=NULL)
        return l->prim->valor;
    else
        return NULO;
}


void clear(lista* l)
{
    No *it;

    if( l->prim!=NULL )
    {
        it = l->prim;
        l->prim = l->prim->prox;
        free(it);
        clear(l);
    }
    l->prim = NULL;
}



int i, j, T;
int R, k, N;



int resolve(lista* l, lista* l2)
{
    int lucro=0;
    int vagas;
    int i;


    for(i=0; i<R; i++)
    {
        vagas =k;
        // esvaziar carrinho

        while( peek(l) <= vagas && peek(l)!=NULO )
        // enquanto couber mais alguem
        {
            vagas -= peek(l);
            // diminui vagas
            put(l2, peek(l));
            // armazenar em l2
            pop(l);
            // retirar de l
        }
        // FOI!!!

        lucro += k-vagas;
        // aumenta lucro

        while(peek(l2)!=NULO)
        {
            put(l, peek(l2));
            // voltar pra l de l2
            pop(l2);
            // retirar de l2
        }
        // Retornaram pra fila
    }

    return lucro;
}


int main()
{
    int grupo;

    lista l, l2;
    l.prim =NULL;
    l2.prim =NULL;

    int resposta[10010];
    FILE *arq, *arq2;

    arq = fopen("output.txt", "w");
    arq2 = fopen("C-small-attempt0.in", "r");

    fscanf( arq2, "%d", &T);

    for(i=0; i<T; i++)
    {
        clear(&l);
        clear(&l2);
        fscanf( arq2, "%d %d %d", &R, &k, &N);

        for(j=0; j<N; j++)
        {
            fscanf( arq2, "%d", &grupo);
            put(&l, grupo);
        }

        resposta[i] = resolve(&l, &l2);
    }
    fclose(arq2);


    for(i=0; i<T; i++)
    {
        fprintf(arq, "Case #%d: %d\n", i+1, resposta[i]);
    }

    fclose(arq);
    return 0;
}
