#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

const int maxl=15; 
const int maxd=5000; 
const int maxn=500; 
const int maxStr=500;
char findLetra(char* caso, int pos, char letra)
{
	int par=0;
	for (int n=0;n<maxStr;n++)
	{
		if(pos<0)
			return 0;
	
		switch(caso[n])
		{
			case 0:
				return 0;
			break;
			case '(':
				par++;
			break;
			case ')':
				par--;
				pos--;
			break;
			default:
				if(pos==0 && letra==caso[n])
					return letra;
				if(!par)
					pos--;
			break;
		}
	}
	return 0;
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	
	//leemos variables
	int l,d,n;
	scanf("%d%d%d",&l,&d,&n);

	//capturamos las palabras del idioma
	char palabras[maxd][maxl]={0};
	for(int i=0;i<d;i++)
	{
		scanf("%s",palabras[i]);		
	}
	
	//analizamos casos
	char caso[maxStr];
	char palabra[maxl];
	int contador=0;
	for(int casos=0;casos<n;casos++)
	{
		//capturamos caso
		scanf("%s",caso);

		//analizamos todas las palabras
		for(int p=0;p<d;p++)
		{
			bool palabraOk=true;
			for(int x=0;x<l;x++)
			{
				if (palabras[p][x]!=findLetra(caso,x,palabras[p][x]))
				palabraOk=false;
			}		
			if (palabraOk==true)
				contador++;
		}
		//imprimimos resultado
		printf("Case #%d: %d\n", casos+1, contador);
		contador=0;
	}

	exit(0);
}
