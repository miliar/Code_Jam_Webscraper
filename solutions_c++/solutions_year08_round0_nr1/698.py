#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define finname "A-large.in"
#define foutname "A-large.out"

typedef unsigned long long ULL;

using namespace std;

int main()
{
    cout << "El programa dira las combinaciones maximas de busqueda segun el" << endl;
    cout << "texto a buscar y el motor de busqueda." << endl << endl;
    ifstream fin(finname);
    ofstream fout(foutname);
    if(!fin)
    {
        cout << "No se pudo abrir el archivo con la entrada de datos." << endl;
        system("PAUSE");
        return 1;
    }
    short limite;
    fin >> limite;  
    for(short actual=1; actual<=limite; actual++)
    {
        short S;
        int Q;
        vector<string> search_engines, queries;
        fin >> S;
        string temp;
        getline(fin, temp); // Para coordinar los >> y los getline.
        for(short s_actual=0; s_actual<S; s_actual++)
        {
            string temp;
            getline(fin, temp);
            search_engines.push_back(temp);
        }
        fin >> Q;
        getline(fin, temp); // Para coordinar los >> y los getline.
        for(short q_actual=0; q_actual<Q; q_actual++)
        {
            string temp;
            getline(fin, temp);
            queries.push_back(temp);
        }
        short Y=0, aparecidos=0, ultimo_aparecido=-1;
        vector<bool> aparecio;
        for(short i=0; i<S; i++)
        {
            aparecio.push_back(false);
        }
        for(short i=0; i<Q; i++)
        {
            for(short j=0; j<S; j++)
            {
                if(queries[i] == search_engines[j] && !aparecio[j])
                {
                    aparecio[j] = true;
                    aparecidos++;
                    ultimo_aparecido = j;
                }
            }
            if(aparecidos == S)
            {
                for(short j=0; j<S; j++)
                {
                    aparecio[j] = false;
                }
                Y++;
                aparecidos = 1;
                aparecio[ultimo_aparecido] = true;
            }
        }
        fout << "Case #" << actual << ": " << Y << endl;
        cout << "Case #" << actual << ": " << Y << endl;
    }
    fin.close();
    fout.close();
    cout << endl;
    system("PAUSE");
    return EXIT_SUCCESS;
}
