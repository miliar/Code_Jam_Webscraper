// Alien.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

class TNodo
{
public:
	TNodo *hijos[256];
	int count;

	int cuenta(vector<string> &letras,int posicion)
	{
		if (posicion==letras.size())
		{
			return count;
		}
		int res=0;
		for (int i=0;i<letras[posicion].length();i++)
		{
			if (hijos[letras[posicion][i]])
			{
				res+=hijos[letras[posicion][i]]->cuenta(letras,posicion+1);
			}
		}
		return res;
	}

	void agregapalabra(string &palabra,int posicion)
	{
		if (posicion==palabra.length())
		{
			count=1;
			return;
		}
		if (!hijos[palabra[posicion]])
		{
			hijos[palabra[posicion]]=new TNodo();
		}
		hijos[palabra[posicion]]->agregapalabra(palabra,posicion+1);
	}

	TNodo()
	{
		count=0;
		memset(hijos,0,sizeof(hijos));
	}
	
	~TNodo(void)
	{
		for (int i=0;i<256;i++)
		{
			if (hijos[i])
			{
				delete hijos[i];
			}
		}
	}
};

int main(int argc, char* argv[])
{
	FILE *entrada = fopen("input.txt","rt");
	FILE *salida = fopen("salida.txt","wt");
	int L,D,N;
	fscanf(entrada,"%d %d %d\n",&L,&D,&N);
	char aux[102400];
	TNodo Diccionario;
	string palabra;
	for (int i=0;i<D;i++)
	{
		fscanf(entrada,"%s\n",aux);
		palabra=aux;
		Diccionario.agregapalabra(palabra,0);
	}
	for (int i=0;i<N;i++)
	{
		fscanf(entrada,"%s\n",aux);
		int pos=0;
		vector<string> letras(L);
		for (int j=0;j<L;j++)
		{
			string palabra="";
			if (aux[pos]=='(')
			{
				pos++;
				while (aux[pos]!=')')
				{
					bool esta=false;
					for (int k=0;(k<letras[j].length())&&(!esta);k++)
					{
						esta=(palabra[k]==aux[pos]);
					}
					if (!esta)
					{
						palabra=palabra+string(1,aux[pos]);
					}
					pos++;
				}
				letras[j]=palabra;
			}
			else
			{
				letras[j]=string(1,aux[pos]);
			}
			pos++;
		}
		if (i>0)
			fprintf(salida,"\n");
		fprintf(salida,"Case #%d: %d",i+1,Diccionario.cuenta(letras,0));
	}
	fclose(entrada);
	fclose(salida);
	return 0;
}

