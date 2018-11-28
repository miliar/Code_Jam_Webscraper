#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdlib.h>
#include <cstdlib>
#include <fstream>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iterator>
#include <cmath>
#include <algorithm>
#include <functional>
#include <utility>
using namespace std;

#define INPUT "A-large (1).in"
#define OUTPUT "output.out"



namespace gcj ///Útiles varios input/output, conversiones, etc...
{
void open_inFile (ifstream& ifile, const char nombre[] = INPUT)
{
    ifile.open(nombre);
    if (!ifile.is_open())
    {
        cerr << "Error: No existe el archivo de entrada \"" << INPUT << "\"";
        exit(1);
    }
    else
    {
        cout << "Abierto archivo de input: \"" << INPUT << "\"" << endl << endl;
    }
}

template<typename T> T stringTo (string cadena)
{
    T num;
    istringstream buffer (cadena);
    buffer >> num;
    return num;
}

template<typename T> string toString (T num)
{
    ostringstream buffer;
    buffer << num;
    return buffer.str();
}
/*
string int_to_string (int entero) //Usa la vieja función itoa(). No es siempre compatible.
{
    static char numero[100];
    itoa(entero,numero,2);
    return numero;
}
*/

void print_file (vector<string> output, ostream& ofile)
{
    vector<string>::const_iterator its(output.begin());
    while (1)
    {
        ofile << *its++;
        if (its==output.end()) break;
        ofile << endl;
    }
    cout << endl << "Escrito archivo de output: \"" << OUTPUT << "\"" << endl << endl;
}

class guarda_output
{
    public:
    void operator() (double resultado, vector<string>& output, bool consola=false)
    {
        int caso = output.size();
        int precision = 8+log10(resultado);
        string buffer;
        buffer = "Case #";
        ostringstream buff1;
        buff1 << caso+1;
        buffer += buff1.str();
        buffer += ": ";
        ostringstream buff2;
        buff2 << setprecision(precision) << resultado;
        buffer += buff2.str();
        output.push_back(buffer);
        if (consola) cout << output.back() << endl;
    }

    void operator() (string& resultado, vector<string>& output, bool consola=false)
    {
        int caso = output.size();
        string buffer;
        buffer = "Case #";
        ostringstream buff;
        buff << caso+1;
        buffer += buff.str();
        buffer += ": ";
        buffer += resultado;
        output.push_back(buffer);
        if (consola) cout << output.back() << endl;
    }
    void operator() (char& resultado, vector<string>& output, bool consola=false)
    {
        int caso = output.size();
        string buffer;
        buffer = "Case #";
        ostringstream buff;
        buff << caso+1;
        buffer += buff.str();
        buffer += ": ";
        buffer += resultado;
        output.push_back(buffer);
        if (consola) cout << output.back() << endl;
    }
}guarda_output;

class consola_vector
{
    public:
    template<class T> void operator () (T const& cont)
    {
        typename T::const_iterator pos;
        typename T::const_iterator end(cont.end());
        for (pos=cont.begin(); pos!=end; ++pos)
        {
            cout << *pos;
            if(pos!=end-1) cout << ", ";
        }
        cout << endl;
    }
    template<class T> void operator << (T const& cont)
    {
        operator()(cont);
    }
}consola_vector;

template<class C, class E> bool es_en_contenedor(C const& cont, E elemento)
{
    typename C::const_iterator pos;
    typename C::const_iterator end(cont.end());
    for (pos=cont.begin(); pos!=end; ++pos)
    {
        if (elemento == *pos)
            return true;
    }
    return false;
}

template<typename T> bool comparePair (pair<T,T> const& p1, pair<T,T> const& p2)
{
    //Compara dos pairs sin tener en cuenta el orden de sus elementos. Han de tener todos el mismo tipo.
    if (p1==p2)
        return true;
    else if (p1.first == p2.second and p1.second == p2.first)
        return true;
    return false;
}


class base
{
    public:
    vector<int> valor_vector (int _valor, int _base)
    {
        int temp=0;
        vector<int>entero_base;
        while(_valor>0)
        {
            temp=_valor%_base;
            _valor -= temp;
            _valor /=_base;
            entero_base.push_back(temp);
        }
        if (entero_base.empty()) entero_base.push_back(0);
        reverse(entero_base.begin(),entero_base.end());
        return entero_base;
    }
    vector<int> operator () (int _valor, int _base)
    {
        return valor_vector(_valor, _base);
    }
    int operator () (vector<int> _valor, int _base)
    {
        int valor=0;
        reverse (_valor.begin(),_valor.end());
        int valor_size = _valor.size();
        for (int i=0;i<valor_size;i++)
        {
            valor += pow(_base,i)*_valor[i];
        }
        return valor;
    }
    string valor_string(int _valor, int _base)
    {
        string s_res;
        vector<int> v_res;
        v_res = valor_vector (_valor, _base);
        int v_res_size = v_res.size();
        string temp;
        for (int i=0;i<v_res_size; i++)
        {
            temp = toString(v_res[i]);
            s_res += temp;
        }
        return s_res;
    }
}base;

}
using namespace gcj;


double RPI (double wp, double owp, double oowp)
{
    return (wp*0.25)+(owp*0.5)+(oowp*0.25);
}

class score
{
    public:
    double wp,owp,oowp;
    double wp_parcial;
    double rpi;
    double n_juegos;
};



int main()
{
    ifstream ifile;
    ofstream ofile;
    vector<string> output;
    string buf;

/// Variables del problema ***********************************************
    int T,N;

    vector<string>sch;
    double res;
    vector<score>sco;  //cada equipo tiene un score con wp, owp y oowp.

/// Lectura INPUT y operaciones ******************************************

    open_inFile(ifile);
    ifile >> T;
    cout << endl << T << " casos." << endl << endl;
    for (int t=0;t<T;t++)
    {
        //Reiniciar todos los contenedores y respuestas.
        res=0;
        sch.clear();
        sco.clear();

        ifile >> N;
        sco.resize(N);
        for (int n=0;n<N;n++)
        {
            ifile >> buf;
            sch.push_back(buf);
        }
        /// Operaciones para cada caso ******************************

        //Hayamos WP de cada equipo N.
        double n_juegos;
        double n_ganados;
        for (int n=0;n<N;n++) //cada equipo
        {
            n_juegos=0.0;
            n_ganados=0.0;
            for (int j=0;j<N;j++)
            {
                if (n!=j)
                {
                    if (sch[n][j]=='1')
                    {
                        n_ganados++;
                        n_juegos++;
                        sco[n].n_juegos++;
                    }
                    else if (sch[n][j]=='0')
                    {
                        n_juegos++;
                        sco[n].n_juegos++;
                    }
                }
            }
            sco[n].wp = n_ganados/n_juegos;
        }

        //Hayamos OWP de cada equipo N
        double suma;
        for (int n=0;n<N;n++)
        {
            suma=0.0;
            for (int i=0;i<N;i++)
            {
                if (i==n) continue;
                n_juegos=0.0;
                n_ganados=0.0;
                for (int j=0;j<N;j++)
                {
                    if (i!=j and j!=n)
                    {
                        if (sch[i][j]=='1')
                        {
                            n_ganados++;
                            n_juegos++;
                        }
                        else if (sch[i][j]=='0')
                        {
                            n_juegos++;
                        }
                    }
                }
                sco[i].wp_parcial = n_ganados/n_juegos;
                //sco[i].n_juegos = n_juegos;
            }
            for (int i=0;i<N;i++)//sumamos para hacer media
            {
                if (i==n) continue;
                //si juega contra él...
                if (sch[n][i]!='.')
                    suma += sco[i].wp_parcial;
            }
            sco[n].owp = suma/sco[n].n_juegos;
        }

        // hayamos OOWP
        for (int n=0;n<N;n++)
        {
            suma=0.0;
            for (int i=0;i<N;i++)
            {
                if (i==n) continue;
                if (sch[n][i]!='.')
                    suma += sco[i].owp;
            }
            sco[n].oowp = suma/sco[n].n_juegos;
        }

        //Hayamos RPI
        buf.clear();
        for (int n=0;n<N;n++)
        {
            sco[n].rpi = RPI(sco[n].wp,sco[n].owp, sco[n].oowp);
            buf+= "\n";
            buf += toString(sco[n].rpi);
        }




            guarda_output (buf,output,true);
    }
    ifile.close();
   // return 0;

/// Escritura OUTPUT. ****************************************************
    {
        ofile.open(OUTPUT);
        print_file(output, ofile);
        ofile.close();
        cout << "///***by Mesjetiu***\\\\\\" << endl;
        return 0;
    }
}
