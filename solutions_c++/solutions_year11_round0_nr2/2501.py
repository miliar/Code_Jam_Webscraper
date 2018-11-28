/** Librerias **/
#include <iostream>
#include <string>
#include <map>
#include <set>

/** Namespaces **/
using namespace std;

/** Constantes **/
#define CANT_ELEM 8

/** Macros **/

/** Tipos **/

/** Globales **/
string elementos("QWERASDF");

/** Prototipos de funciones **/ 

/** Cuerpo principal **/
int main()
{
	int cant_casos, cant_comb, cant_op, cant_char, ii, jj, kk, pos, tam_inicial, tam_final;
	map<char, char> vec_comb[CANT_ELEM];
	set<char> vec_op[CANT_ELEM];
	string cad_temp, cad_inicial, cad_final;
	map<char, char>::iterator it_m;
	set<char>::iterator it_s;
	
	cin >> cant_casos;
	for (ii = 1; ii <= cant_casos; ii++)
	{
		//Limpieza
		for (jj = 0; jj < CANT_ELEM; jj++)
		{
			vec_comb[jj].clear();
			vec_op[jj].clear();
		}
		
		cin >> cant_comb;
		for (jj = 0; jj < cant_comb; jj++)
		{
			cin >> cad_temp;
			
			pos = elementos.find(cad_temp[0]);
			vec_comb[pos].insert(pair<char,char>(cad_temp[1],cad_temp[2]));
			
			if (cad_temp[1] != cad_temp[0])
			{
				pos = elementos.find(cad_temp[1]);
				vec_comb[pos].insert(pair<char,char>(cad_temp[0],cad_temp[2]));
			}
		}
		
		cin >> cant_op;
		for (jj = 0; jj < cant_op; jj++)
		{
			cin >> cad_temp;
			
			pos = elementos.find(cad_temp[0]);
			vec_op[pos].insert(cad_temp[1]);
			
			if (cad_temp[1] != cad_temp[0])
			{
				pos = elementos.find(cad_temp[1]);
				vec_op[pos].insert(cad_temp[0]);
			}
		}
		
		cin >> tam_inicial >> cad_inicial;
		cad_final.clear();
		cad_final += cad_inicial[0];
		for (jj = 1; jj < tam_inicial; jj++)
		{
			tam_final = cad_final.size();
			//cout << cad_inicial[jj] << endl;
			//cout << "Antes: " << cad_final << endl;
			if ( tam_final > 0)
			{
				pos = elementos.find(cad_inicial[jj]);
				it_m = vec_comb[pos].find(cad_final[tam_final - 1]);
				if (it_m == vec_comb[pos].end())
				{
					for (kk = 0; kk < tam_final; kk++)
					{
						it_s = vec_op[pos].find(cad_final[kk]);
						if (it_s != vec_op[pos].end())
						{
							cad_final.clear();
							break;
						}
					}
					
					if (kk == tam_final)
						cad_final += cad_inicial[jj];
				}
				else
					cad_final[tam_final - 1] = it_m->second;
			}
			else
				cad_final += cad_inicial[jj];
			//cout << "Despues: " << cad_final << endl;
		}
		
		//Salida
		cout << "Case #" << ii << ": [";
		tam_final = cad_final.size();
		for (jj = 0; jj < tam_final; jj++)
		{
			cout << cad_final[jj];
			if (jj < (tam_final - 1))
				cout << ", ";
		}
		cout << "]" << endl;
	}
	
	//Fin
	return 0;
}

/** Implementacion de funciones **/
