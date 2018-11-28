// ProblemaA.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <string>
#include <set>
#include <stdio.h>

using namespace std;

#define maxhappy 11814489LL
typedef long long int64;

class TNodo
{
public:
	string Feature;
	double value;
	TNodo *Left,*Right;

	double CalculaP(set<string> &feat)
	{
		if (Left)
		{
			if (feat.count(Feature)>0)
			{
				return value*Left->CalculaP(feat);
			}
			else
			{
				return value*Right->CalculaP(feat);
			}
		}
		else
		{
			return value;
		}
	}

	TNodo()
	{
		Left=Right=NULL;
	}

	~TNodo()
	{
		if (Left)
		{
			delete Left;
		}
		if (Right)
		{
			delete Right;
		}
	}
};

void searchpar(FILE *entrada,char val)
{
	char c;
	while (true)
	{
		fscanf(entrada,"%c",&c);
		if (c==val)
		{
			break;
		}
	}
}

void LeeArbol(FILE *entrada,TNodo *Nodo)
{
	string number="";
	char c;
	//start number
	while(true)
	{
		fscanf(entrada,"%c",&c);
		if ((c!=' ')&&(c!='\n'))
		{
			break;
		}
	}
	number=number+c;
	//finish number
	while(true)
	{
		fscanf(entrada,"%c",&c);
		if ((c==' ')||(c=='\n')||(c==')'))
		{
			break;
		}
		else
		{
			number=number+c;
		}
	}
	sscanf(number.c_str(),"%lf",&Nodo->value);
	//skip spaces
	while ((c==' ')||(c=='\n'))
	{
		fscanf(entrada,"%c",&c);
	}
	//has a feature name?
	Nodo->Feature="";
	while ((c!=')')&&(c!='('))
	{
		Nodo->Feature=Nodo->Feature+c;
		fscanf(entrada,"%c",&c);
		if ((c==' ')||(c==')')||(c=='(')||(c=='\n'))
		{
			break;
		}
	}
	//skip spaces
	while ((c!=')')&&(c!='('))
	{
		fscanf(entrada,"%c",&c);
	}
	//is leaf?
	if (c==')')
	{
		return;
	}
	else if (c=='(')
	{
		Nodo->Left=new TNodo;
		LeeArbol(entrada,Nodo->Left);
		Nodo->Right=new TNodo;
		searchpar(entrada,'(');
		LeeArbol(entrada,Nodo->Right);
		while (c!=')')
		{
			fscanf(entrada,"%c",&c);
		}
	}
	else
	{
		printf("problem\n");
	}
}

int main(int argc, char* argv[])
{
	FILE *entrada = fopen("input.txt","rt");
	FILE *salida = fopen("salida.txt","wt");
	int T;
	char c;
	fscanf(entrada,"%d%c",&T,&c);
	TNodo *Raiz;
	char nombre[102400];
	for (int t=1;t<=T;t++)
	{
		searchpar(entrada,'(');
		Raiz=new TNodo;
		LeeArbol(entrada,Raiz);
		int N;
		fscanf(entrada,"%d%c",&N,&c);
		fprintf(salida,"Case #%d:\n",t);
		for (int n=0;n<N;n++)
		{
			int F;
			fscanf(entrada,"%s %d%c",nombre,&F,&c);
			set<string> features;
			for (int f=0;f<F;f++)
			{
				fscanf(entrada,"%s%c",nombre,&c);
				features.insert(nombre);
			}
			fprintf(salida,"%0.10lf\n",Raiz->CalculaP(features));
		}
		delete Raiz;
	}

	fclose(entrada);
	fclose(salida);
	return 0;
}
