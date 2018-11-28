#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int main(int argc, char** argv){
	ofstream salida("B.out.txt");
	cout.rdbuf(salida.rdbuf());

	int t, c, d, n, k, i, j, x;
	char comb[40][3], opu[30][2], elem;
	list<char> lista;
	list<char>::iterator a, b;
	int count[130];

	cin >> t;
	for(k=1; k<=t; k++){
	    //conteo a cero
	    lista.clear();
	    for(i=60; i<100; i++){
            count[i] = 0;
	    }
	    //combinar
        cin >> c;
        for(i=0; i<c; i++){
            cin >> comb[i][0] >> comb[i][1] >> comb[i][2];
        }
        //oponer
        cin >> d;
        for(i=0; i<d; i++){
            cin >> opu[i][0] >> opu[i][1];
        }
        //invocar
        cin >> n;
        for(j=0; j<n; j++){
            cin >> elem;
            //final de la lista
            lista.push_back(elem);
            count[elem] ++;
            //combinar
            if(lista.size() > 1){
                a = lista.end(); a--;
                b = a; b--;
                for(i=0; i<c; i++){
                    if( (*a == comb[i][0] && *b == comb[i][1]) || (*a == comb[i][1] && *b == comb[i][0]) ){
                        count[*a]--; count[*b]--;
                        lista.pop_back(); lista.pop_back();
                        lista.push_back(comb[i][2]);
                        count[comb[i][2]]++;
                        break;
                    }
                }
            }
            //oponer
            for(i=0; i<d; i++){
                if(count[opu[i][0]]>0 && count[opu[i][1]]>0){
                    lista.clear();
                    //conteo a cero
                    for(x=60; x<100; x++){
                        count[x] = 0;
                    }
                }
            }
        }

        //salida
        cout << "Case #" << k << ": [";
        for(a=lista.begin(); a!=lista.end(); a++){
            if(a==lista.begin()) cout << *a;
            else cout << ", " << *a;
        }
        cout << "]" << endl;
	}

	return 0;
}
