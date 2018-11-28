/** Librerias **/
#include <iostream>
#include <algorithm>

/** Namespaces **/
using namespace std;

/** Constantes **/
#define MAX 1005

/** Macros **/

/** Tipos **/

/** Globales **/

/** Prototipos de funciones **/ 

/** Cuerpo principal **/
int main()
{
	int ii, jj, cant_casos, cant_vals, cant_sumas;
	unsigned long int vec_vals[MAX], vec_sumas_bin[MAX], vec_sumas[MAX], suma_p, suma_s, suma_p_bin;
	
	cin >> cant_casos;
	for (ii = 1; ii <= cant_casos; ii++)
	{
		cin >> cant_vals;
		for (jj = 0; jj < cant_vals; jj++)
			cin >> vec_vals[jj];
		
		sort(vec_vals, vec_vals + cant_vals);
		
		cant_sumas = cant_vals - 1;
		for (jj = (cant_vals - 1); jj > 0; jj--)
		{
			if (jj == (cant_vals - 1))
				vec_sumas_bin[jj - 1] = vec_sumas[jj - 1] = vec_vals[jj];
			else
			{
				vec_sumas_bin[jj - 1] = vec_vals[jj] ^ vec_sumas_bin[jj];
				vec_sumas[jj - 1] = vec_vals[jj] + vec_sumas[jj];
			}
		}
		
		suma_p_bin = vec_vals[0];
		for (jj = 0; jj < cant_sumas; jj++)
		{
			if (vec_sumas_bin[jj] == suma_p_bin)
				break;
			suma_p_bin ^= vec_vals[jj + 1];	
		}
		
		cout << "Case #" << ii <<": ";
		if (jj == cant_sumas)
			cout << "NO" << endl;
		else
			cout << vec_sumas[jj] << endl;
		
		/*cout << endl << "Caso " << ii << endl;
		for (jj = 0; jj < cant_vals; jj++)
			cout << vec_vals[jj] << " ";
		cout << endl;
		
		for (jj = 0; jj < cant_sumas; jj++)
			cout << vec_sumas_bin[jj] << " ";
		cout << endl;
		
		for (jj = 0; jj < cant_sumas; jj++)
			cout << vec_sumas[jj] << " ";
		cout << endl;*/
	}
	
	//Fin
	return 0;
}

/** Implementacion de funciones **/
