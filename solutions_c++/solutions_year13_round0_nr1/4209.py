//============================================================================
// Name        : gcj-a.cpp
// Author      : 
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <stdlib.h>
using namespace std;

string partida(string toc)
{
	string res;
	char aux='X';
	bool flag = false;		//hay puntos "." que forman un ganador
	int k=-1;
	for(int i=0;i<16;i++)
	{
		res=toc[i];
		if(res == "T")
		{
			toc[i]=aux;
			k=i;
		}
	}
for(int j=0;j<2;j++)
{
	//Mira por filas
	for(int i=0;i<16;i=i+4)
	{
		//Mira la fila
		if(toc[i]==toc[i+1] && toc[i]==toc[i+2] && toc[i]==toc[i+3])
		{
			res = toc[i];
			if(res == ".")
			{
				flag=true;
				continue;
			}
			else
				return res +" won";
		}
	}

	//Mira por columnas
	for(int i=0;i<4;i++)
	{
		//Mira la columna
		if(toc[i]==toc[i+4] && toc[i]==toc[i+8] && toc[i]==toc[i+12])
		{
			res = toc[i];
			if(res == ".")
			{
				flag=true;
				continue;
			}
			else
				return res +" won";
		}
	}

	//Mira diagonal izquierda
	if(toc[0]==toc[5] && toc[0]==toc[10] && toc[0]==toc[15])
	{
		res = toc[0];
		if(res == ".")
			flag=true;
		else
			return res +" won";
	}

	//Mira diagonal derecha
	if(toc[3]==toc[6] && toc[3]==toc[9] && toc[3]==toc[12])
	{
		res = toc[3];
		if(res == ".")
			flag=true;
		else
			return res +" won";;
	}
	aux='O';
	if(k!=-1)
		toc[k]=aux;
}
	if(flag)
		return "Game has not completed";
	else
	{
		for(int i=0;i<16;i++)
		{
			res=toc[i];
			if(res == ".")
				return "Game has not completed";
		}
	}

	return "Draw";
}

int main() {
	int x,t,i=0;
	string n,toc,res;

    ofstream fout("D:\\eclipse\\gcj-a\\Debug\\A-large.out");
    ifstream fin("D:\\eclipse\\gcj-a\\Debug\\A-large.in");

   	fin>>t;
    for(x=0;x<t*4;x++){
		fin>>n;
		toc=toc+n;
		if((int)toc.length()==16)
		{
			res = partida(toc);
			i++;
			fout<<"Case #"<<i<<": "<<res<<endl;
			toc="";
		}
	}
    fout.close();
    fin.close();
   	return 0;
}

