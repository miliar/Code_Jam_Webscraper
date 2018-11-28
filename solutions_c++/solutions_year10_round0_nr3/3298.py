#include <iostream>
#include <fstream>
#include <cstdlib> // for exit function
// This program reads values from the file 'example.dat'
// and echoes them to the display until a negative value
// is read.

#include <string>

using namespace std;

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s file.in\n", argv[0]);
        return -1;
    }

    ifstream indata; // indata is like cin
    indata.open(argv[1]); // opens the file

    if(!indata) { // file couldn't be opened
        cerr << "Error: file could not be opened" << endl;
        exit(1);
    }

    int T;
    int R, K, N;
    int i;
    int recaudado = 0;
    int vagon = 0;

    int viajes;
    int grupo_actual = 0;
    int personas;
    int personas_totales = 0;

    indata >> T;

    for (i = 1; i <= T; i++)
    {
        indata >> R >> K >> N;

        int grupos[N];


        int j;
        personas_totales = 0;
        for (j = 0; j < N; j++)
        {
            int aux;
            indata >> aux;
            grupos[j] = aux;
            personas_totales += aux;
        }

        personas = 0;
        grupo_actual = 0;
        recaudado = 0;
        
        if (personas_totales < K)
        {
            recaudado = R * personas_totales;
        }
        else
        {
            for (viajes = 0; viajes < R; viajes++)
            {
                for (personas = 0; personas < K;)
                {
                    if (personas + grupos[grupo_actual] > K)
                        break;

                    personas += grupos[grupo_actual];
                    grupo_actual++;
                    if (grupo_actual >= N)
                        grupo_actual = 0;
                }
                recaudado += personas;
            }
        }

        printf("Case #%d: %d\n", i, recaudado);
    }

    return 0;
}
