#include<stdio.h>
#include<string.h>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

#define MAX 11900000
//#define MAX 10000

int PD[12][MAX];
int n, v[16];

int calcula(int valor, int base)
{
	if(valor >= MAX) return 0;

	if(PD[base][valor] != -1) return PD[base][valor];

	if(valor == 1) return PD[base][valor] = 1;
	if(valor == 0) return PD[base][valor] = 0;

	PD[base][valor] = 0;
	int tmp = valor;
	int r = 0;

	while(tmp != 0)
	{
		r += (tmp%base)*(tmp%base);
		tmp /= base;
	}

	if(r == 1) return PD[base][valor] = 1;

	return PD[base][valor] = calcula(r, base);
}

void precalcula()
{

	for(int i = 2; i <= 10; i++)
		for(int k = 0; k < MAX; k++)
			PD[i][k] = -1;

	for(int i = 2; i <= 10; i++)
			for(int k = 2; k < MAX; k++)
			{
				calcula(k, i);

			}
}



int main()
{
	int T, res, lidos, ct;
	char linha[128];

	scanf("%d ", &T);

	precalcula();

	for(int i = 0; i < T; i++)
	{

			gets(linha);
			int tam = strlen(linha);
			n = 0;
			lidos = 0;
			ct = 0;
			while(1)
			{
				if(sscanf(&linha[lidos], " %d%n", &v[n], &ct) < 1) break;

				lidos += ct;
				n++;
				if(tam <= lidos) break;


			}

			res = -1;
			int foi;
			for(int j = 2; j < MAX; j++)
			{
				foi = 1;
				for(int k = 0; k < n; k++)
				{
					if(PD[v[k]][j] != 1)
					{
						foi = 0;
						break;
					}
				}
				if(foi == 1)
				{
					res = j;
					break;
				}
			}

			//res = calcula();
			printf("Case #%d: %d\n", i + 1, res);

	}

	return 0;
}
