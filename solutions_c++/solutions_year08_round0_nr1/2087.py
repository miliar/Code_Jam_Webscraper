// CodeJamSearchEngine.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream archivo;
	archivo.open("C:\\Codejam\\InputSearchEngine.txt");
	ofstream archivosalida;
	archivosalida.open("C:\\Codejam\\Output.txt");

	int c = 0;
	char buffer[100];
	string bufferstr;
	int numcases = 0;
	archivo.getline(buffer, 100);
	numcases = atoi(buffer);
	int casenumber = 0;
	

	for (c=numcases; c > 0; c--)
	{
		casenumber++;
		vector<string> buscadores;
		vector<string>::iterator itbuscadores;
		vector<string> buscadorescopia;
		vector<string>::iterator itbuscadorescopia;
		int numbuscadores = 0;
		int numquerys = 0;
		int numcambios = 0;
		
		archivo.getline(buffer, 100); //numero de buscadores posibles
		numbuscadores = atoi(buffer);
		
		int c1 = 0;
		for (c1 = 0; c1 < numbuscadores; c1++)
		{
			archivo.getline(buffer, 100);
			bufferstr = buffer;

			buscadores.push_back(bufferstr);
		}
		buscadores.push_back("END");

		archivo.getline(buffer, 100); // numero de querys
		numquerys = atoi(buffer);

		buscadorescopia = buscadores;

		for (c1 = 0; c1 < numquerys; c1++)
		{
			archivo.getline(buffer, 100);
    		bufferstr = buffer;
			cout << bufferstr << " ";
			itbuscadorescopia = find(buscadorescopia.begin(),buscadorescopia.end(), bufferstr);
			if (itbuscadorescopia != buscadorescopia.end())
			{
				buscadorescopia.erase(itbuscadorescopia);
			    cout << "borrado";
			}
			cout << "size" << buscadorescopia.size()-1 << " ";
			if ((buscadorescopia.size() - 1) < 1)
			{
				buscadorescopia = buscadores;
                itbuscadorescopia = find(buscadorescopia.begin(),buscadorescopia.end(), bufferstr);
				buscadorescopia.erase(itbuscadorescopia);


				numcambios++;
			}
			
		}
		cout << numcambios << " ";
		archivosalida << "Case #" << casenumber << ": " << numcambios << '\n';
		
	}

    cin >> c;

	archivo.close();
	archivosalida.close();

	return 0;
}

