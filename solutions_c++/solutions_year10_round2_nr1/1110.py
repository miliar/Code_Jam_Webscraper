#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct dir
{
	char nome[101];
	int novo;
	dir * lista;
	dir * prox;
}dir;

dir * root;

void insere(char * cam[101], int sub, int n)
{
	dir ** aux;
	aux =  &root;
	int a = 1;
	for (int i = 0; i < sub; i++)
	{
		while (*aux != NULL)
		{
			a = strcmp(cam[i], (*aux)->nome);
			if (a <= 0)
				break;
			aux = &((*aux)->prox);
		}
		if (!a)
		{
			aux = &((*aux)->lista);
			a = 1;
		}
		else
		{
			dir * temp = (dir*)malloc(sizeof(dir));
			temp->novo = n;
			temp->lista = NULL;
			temp->prox = *aux;
			strcpy(temp->nome, cam[i]);
			*aux = temp;
			aux = &(temp->lista);
		}
	}
	return;
}

int percorre(dir * lista)
{
	int i = 0;
	dir * temp;
	
	while (lista != NULL)
	{
		temp = lista;
		if (lista->novo)
		{
			i++;
		}
		i += percorre(lista->lista);
		lista = lista->prox;
		free(temp);
	}

	return i;
}

int main()
{
	int casos, N, M;
	char temp[101];
	char * vettemp[101];
	scanf("%d", &casos);
	for (int c = 1; c <= casos; c++)
	{
		root = NULL;
		scanf("%d %d", &N, &M);
		for (; N > 0; N--)
		{
			scanf("%s", temp);
			int i = 0;
			vettemp[i] = strtok(temp, "/");
			while (vettemp[i] != NULL)
			{
				i++;
				vettemp[i] = strtok(NULL, "/");
			}
			insere(vettemp, i, 0);
		}
		for (; M > 0; M--)
		{
			scanf("%s", temp);
			int i = 0;
			vettemp[i] = strtok(temp, " /");
			while (vettemp[i] != NULL)
			{
				i++;
				vettemp[i] = strtok(NULL, "/");
			}
			insere(vettemp, i, 1);
		}
		printf("Case #%d: %d\n", c, percorre(root));
	}
	return 0;
}
