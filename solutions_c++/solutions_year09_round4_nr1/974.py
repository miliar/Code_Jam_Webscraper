// ProblemaA.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <string>
#include <set>
#include <map>
#include <stdio.h>
#include <algorithm>

using namespace std;

typedef long long int64;

vector<int> primero;

int main(int argc, char* argv[])
{
	FILE *entrada = fopen("input.txt","rt");
	FILE *salida = fopen("salida.txt","wt");
	int T;
	char c;
	fscanf(entrada,"%d%c",&T,&c);
	char nombre[102400];	
	for (int t=1;t<=T;t++)
	{
		int N;
		fscanf(entrada,"%d%c",&N,&c);
		int cambios=0;
		primero.resize(N);
		for (int n=0;n<N;n++)
		{
			primero[n]=0;
			for (int i=0;i<N;i++)
			{
				fscanf(entrada,"%c",&c);
				if (c=='1')
				{
					primero[n]=i;
				}
			}
			fscanf(entrada,"%c",&c);
		}
		for (int n=N-1;n>0;n--)
		{
			vector<int> copia;
			copia.resize(n);
			for (int k=n;k>=0;k--)
			{
				bool puede=true;
				for (int i=0;i<k;i++)
				{
					copia[i]=primero[i];
				}
				for (int i=k;i<n;i++)
				{
					copia[i]=primero[i+1];
				}
				sort(copia.begin(),copia.end());
				for (int i=n-1;i>=0;i--)
				{
					if (copia[i]>i)
					{
						puede=false;
						break;
					}
				}
				if (puede)
				{
					cambios+=n-k;
					//change
					int aux=primero[k];
					for (int i=k;i<n;i++)
					{
						primero[i]=primero[i+1];
					}
					primero[n]=aux;
					break;
				}
			}
		}
		fprintf(salida,"Case #%d: %d\n",t,cambios);
	}
	fclose(entrada);
	fclose(salida);
	return 0;
}
