/** Librerias **/
#include <iostream>

/** Constantes **/
#define MAX 105
using namespace std;

/** Macros **/

/** Tipos **/
typedef struct{
	int boton, orden;
} elemento;

typedef elemento vec_elem[MAX];

/** Globales **/

/** Prototipos de funciones **/ 
void mov_rob(vec_elem vec,int tam_vec,int &pos_vec,int &pos_act,int &ord_act);

/** Cuerpo principal **/
int main()
{
	int cant_casos, cant_bot, ii, jj, tam_b, tam_o, ord_act, pos_b, pos_o, cont_o, cont_b, tiempo;
	int copia;
	vec_elem vec_b, vec_o;
	char color;
	
	cin >> cant_casos;
	for (ii = 1; ii <= cant_casos; ii++)
	{
		cin >> cant_bot;
		tam_b = tam_o = 0;
		for (jj = 1; jj <= cant_bot; jj++)
		{
			cin >> color;
			if (color == 'O')
			{
				cin >> vec_o[tam_o].boton;
				vec_o[tam_o++].orden = jj;
			}
			else
			{
				cin >> vec_b[tam_b].boton;
				vec_b[tam_b++].orden = jj;
			}
		}
		
		ord_act = pos_b = pos_o = 1;
		cont_o = cont_b = tiempo = 0;
		while (ord_act <= cant_bot)
		{
			copia = ord_act;
			mov_rob(vec_o, tam_o, cont_o, pos_o, ord_act);
			
			if (copia != ord_act)
				mov_rob(vec_b, tam_b, cont_b, pos_b, copia);
			else
				mov_rob(vec_b, tam_b, cont_b, pos_b, ord_act);
			tiempo++;
		}
		cout << "Case #" << ii << ": " << tiempo << endl;
	}
	
	//Fin
	return 0;
}

/** Implementacion de funciones **/

void mov_rob(vec_elem vec,int tam_vec,int &pos_vec,int &pos_act,int &ord_act)
{
	if (pos_vec < tam_vec)
	{
		if ((pos_act == vec[pos_vec].boton) && (ord_act == vec[pos_vec].orden))
		{
			ord_act++;
			pos_vec++;
		}	
		else if (pos_act > vec[pos_vec].boton)
			pos_act--;
		else if (pos_act < vec[pos_vec].boton)
			pos_act++;
	}
}
