#include "iostream"
#include "string"
#include "utility"
#define LIM 105

using namespace std;

int mat1[LIM], can1;
int mat2[LIM], can2;

pair<char,int> cola[LIM];

int mover ( int origen, int destino )
{
    if ( origen < destino )
       return origen+1;
    if ( origen > destino )
       return origen-1;
    return origen;
}//f mover

int main()
{
    freopen("A-large.in", "r",stdin );
    freopen("A-large.out","w",stdout);
    
    int casos;
    cin >> casos;
    for ( int caso = 1; caso <= casos; caso++ )
    {
        can1 = can2 = 0;
        
        int cantidad; /// cantidad de elementos en la cola
        cin >> cantidad;
        for ( int i = 0; i < cantidad; i++ )
        {
            char caracter;
            int boton;
            cin >> caracter >> boton;

            cola[i] = make_pair(caracter,boton);

            if ( caracter == 'O' )
               mat1[can1++] = boton;
            else
               mat2[can2++] = boton;
        } //f lectura de datos
        
        int pos1 = 1, pos2 = 1;
        int respuesta = 0;
        int indice1 = 0, indice2 = 0;
        for ( int i = 0; i < cantidad; i++ )
        {
            if( cola[i].first == 'O' )
            {
                while ( pos1 != mat1[indice1] )
                {
                      pos1 = mover( pos1, mat1[indice1] );
                      pos2 = mover( pos2, mat2[indice2] ); //hacer movimiento si es posible
                      ++respuesta;
                }
                ++indice1;   //pasar a la siguiente operacion del 'O'
                pos2 = mover( pos2, mat2[indice2] ); //hacer movimiento si es posible
                ++respuesta; // contar el oprimir boton
            }
            else
            {
                while ( pos2 != mat2[indice2] )
                {
                      pos2 = mover( pos2, mat2[indice2] ); 
                      pos1 = mover( pos1, mat1[indice1] ); //hacer movimiento si es posible
                      ++respuesta;
                }
                ++indice2;   //pasar a la siguiente operacion del 'B'
                pos1 = mover( pos1, mat1[indice1] ); //hacer movimiento si es posible
                ++respuesta; // contar el oprimir boton   
            }            
        }//f recorrido por cola
        
        cout << "Case #" << caso << ": " << respuesta << endl;
    }//f caso

 return 0;
}//fp

