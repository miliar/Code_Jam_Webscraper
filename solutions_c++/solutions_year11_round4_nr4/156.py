#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

#define MAXN (2048)
#define MAX MAXN
#define TAM(a) ((int)(a).size())

vector <int> adj[MAXN];

int m, n;

set<string> foi[MAXN];

typedef struct
{
	string s;
	int v;
	int dist;
}tipofila;

queue<tipofila> fila;

char temp[MAX];
char temp2[MAX];

int main()
{
	int cas, casos;
	int i, j, a, b;	
	scanf("%d", &casos);
	
	for (cas = 1; cas <= casos; cas++)
	{
		printf("Case #%d: ", cas);
		scanf("%d %d", &n, &m);
		
		for (i=0; i<n; i++)
		{
			foi[i].clear();
			adj[i].clear();
		}
		
		while (!fila.empty())
		{
			fila.pop();	
		}
		
		for (i=0; i<m; i++)
		{
			scanf("%d,%d", &a,&b);
			adj[a].push_back(b);
			adj[b].push_back(a);
		}
		
		
		for (i=0; i<n; i++)
		{
			temp[i] = '0';
		}
		temp[n] = 0;
		
		temp[0] = '1';
		for (i=0; i<TAM(adj[0]); i++)
		{
			temp[adj[0][i]] = '1';
		}
		tipofila aux;
		aux.s = temp;
		aux.dist = 0;
		aux.v = 0;
		
		fila.push(aux);
		int gg;
		int achei = 0, optdist=-1, opt=-1;
		tipofila novo;



		while (!fila.empty())
		{
			aux = fila.front();
//			printf("olhando %d\n", aux.v);
			fila.pop();
			
			if (achei && aux.dist > optdist)
				break;
				
			for (i=0; i<TAM(adj[aux.v]); i++)
			{
//				printf(" vizinho %d (%d-esimo de %d)\n", adj[aux.v][i], i, TAM(adj[aux.v]));
				if (adj[aux.v][i] == 1)
				{
//					printf("achei caminho pro ultimo\n");
					if (!achei)
					{
						optdist = aux.dist;
						opt = 0;
						
						for (j=0; j<n; j++)
							if (aux.s[j] == '1')
								opt++;
						opt -= 1 + optdist;
						achei = 1;
					}
					else
					{
						gg = -1 - optdist;
							for (j=0; j<n; j++)
								if (aux.s[j] == '1')
									gg++;
						if (gg > opt)
							opt = gg;
					}
//					printf("pronto\n");
					continue;
				}
//				printf("...\n");
				if (adj[aux.v][i] == 0)
					continue;
				strcpy(temp, aux.s.c_str());
				for (j=0; j<TAM(adj[adj[aux.v][i]]); j++)
				{
					temp[adj[adj[aux.v][i]][j]] = '1';
				}
				if (foi[adj[aux.v][i]].find(temp) == foi[adj[aux.v][i]].end())
				{
					novo.s = temp;
					novo.v = adj[aux.v][i];
					novo.dist = aux.dist+1;
					foi[adj[aux.v][i]].insert(temp);
					fila.push(novo);
//					printf("inseri %d com string %s\n", novo.v, temp);
				}	
			}
		}
		assert(optdist != -1);
		printf("%d %d\n", optdist, opt);
//		printf("\n\n\n\n");
	}
	
	return 0;
}
