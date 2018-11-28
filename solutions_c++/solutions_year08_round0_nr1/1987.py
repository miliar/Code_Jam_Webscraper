#include <cstdio>
#include <map>
#include <string>
#include <set>
#include <list>

using namespace std;

int menor;

struct busca
{
    int indice;
    int switchs;
    int engine;
    busca(int i, int s, int e)
    {
	indice = i;
	switchs = s;
	engine = e;
    }
};

struct comparacao
{
    bool operator() (const busca& lhs, const busca&rhs)
    {
	printf("Comparação: E%d S%d I%d, E%d S%d I%d : %d\n", lhs.engine, lhs.switchs, lhs.indice, rhs.engine, rhs.switchs, rhs.indice, lhs.switchs < rhs.switchs);
//	return false;
	if ( lhs.switchs < rhs.switchs )
	    return true;
	if ( lhs.indice < rhs.indice )
	    return true;
	if ( lhs.indice > rhs.indice )
	    return true;
	if ( lhs.switchs > rhs.switchs )
	    return true;
	if ( lhs.engine != rhs.engine )
	    return true;

	return false;
    }
};

int n, s, q;
int query[1024];

int buscaEmLargura()
{
    //set<busca,comparacao> fila;
    //set<busca,comparacao>::iterator it;
    busca temp(0,0,0);

    list<busca> fila;
    list<busca>::iterator it;

    int i;

    for ( i = 0 ; i < s ; i++ )
    {
	fila.push_back(busca(0,0,i));
    }

    temp = (*fila.begin());
    fila.erase(fila.begin());
   
    while ( 1 )
    {
	if ( fila.size() == 0 )
	    break;

	if ( temp.switchs > fila.begin()->switchs )
	{
	    fila.push_back(temp);
	    temp = (*fila.begin());
	    fila.erase(fila.begin());
	}

	if ( temp.indice >= q )
	{
	    if ( temp.switchs < menor )
		menor = temp.switchs;

	    temp = (*fila.begin());
	    fila.erase(fila.begin());
	    continue;
	}

	if ( temp.engine == query[temp.indice] )
	{
	    for ( i = 0 ; i < s ; i++ )
	    {
		bool insere;
		if ( i == temp.engine )
		    continue;
		insere = true;
		for ( it = fila.begin() ; it != fila.end() ; it++ )
		{
		    if ( it->indice == temp.indice+1 &&
			    it->switchs == temp.switchs+1 &&
			    it->engine == i )
			insere = false;
		}
		if ( insere )
		    fila.push_back(busca(temp.indice+1, temp.switchs+1, i));

//		for ( it = fila.begin() ; it != fila.end() ; it++ )
//		{
//		    printf("%d: I%d S%d\n", it->engine, it->indice, it->switchs);
//		}
//		printf("------\n");
	    }

	    temp = (*fila.begin());
	    fila.erase(fila.begin());
	}
	else
	{
	    temp.indice++;
	}
    }

    return menor;
}

int main (void)
{
    int i, j;
    char linha[300];

    map<string,int> indices;
    //    char engines[101][110];

    fgets(linha, sizeof(linha), stdin);
    sscanf(linha, "%d",&n);

    for ( i = 0 ; i < n ; i++ )
    {
	fgets(linha, sizeof(linha), stdin);
	sscanf(linha, "%d", &s);

	for ( j = 0 ; j < s ; j++ )
	{
	    string palavra;

	    fgets(linha, sizeof(linha), stdin);
	    palavra = linha;

	    indices[palavra] = j;
	}

	fgets(linha, sizeof(linha), stdin);
	sscanf(linha, "%d", &q);

	menor = q+1;

	for ( j = 0 ; j < q ; j++ )
	{
	    string palavra;

	    fgets(linha, sizeof(linha), stdin);
	    palavra = linha;

	    query[j] = indices.find(palavra)->second;
	}

	menor = buscaEmLargura();

	printf("Case #%d: %d\n", i+1, menor);
    }

    return 0;
}

