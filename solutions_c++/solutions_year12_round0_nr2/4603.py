#include <iostream>

using namespace std;

static int NT; // numero de casos 
static int S; // número de tripletes sorprendentes con difierencias entre ellos = 2
static int p; //el mínimo que tiene que ser alguna de las valoraciones


// puntuacion minima (p - 2) * 3 + 2
int main()
{
    cin >> NT;
    
    
    for (int i = 1; i <= NT; ++i) {
        int googlers; //N 
        int tienenMinimo = 0;
        cin >> googlers;
        cin >> S >> p;
        int minPunts = (p - 1) * 2 + p; 
        if (minPunts < p) 
            minPunts = p;
   
        int minPuntsAnomalo = (p - 2) * 2 + p; 
        if (minPuntsAnomalo < p) 
            minPuntsAnomalo = p;
        int anomalosGastados = 0;
        
//         cout  << "minPuntss " << minPunts  << " minpuntsanomalo " << minPuntsAnomalo << " S "<< S << " p " << p << '\t';
        for (int j = 0; j < googlers; ++j) {
            int candidate;
            cin >> candidate;
            
            if ( candidate >= minPunts)
                ++tienenMinimo;
            else if (anomalosGastados < S && candidate >= minPuntsAnomalo) {
                ++tienenMinimo;
                ++anomalosGastados;
            }
        }
        cout << "Case #" << i << ": " << tienenMinimo << endl;
    }
    
    return 0;
}