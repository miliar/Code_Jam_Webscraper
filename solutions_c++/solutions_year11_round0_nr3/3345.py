#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char** argv){
	ofstream salida("C.out.txt");
	cout.rdbuf(salida.rdbuf());

    int t, k, n, i, dulce[1005], tope, x;
    int sean, pat, think, maximo;

    cin >> t;
    for(k=1; k<=t; k++){
        cin >> n;
        for(i=0; i<n; i++){
            cin >> dulce[i];
        }

        tope = (1<<n)-1;
        maximo = -1;

        for(x=1; x<tope; x++){
            //cout << "========================" << x << endl;
            sean = pat = think = 0;
            for(i=0; i<n; i++){
                if( x&(1<<i) ){
                    sean += dulce[i];
                    think = think ^ dulce[i];
                    //cout << "elemento " << i << " si" << endl;
                }
                else{
                    pat = pat ^ dulce[i];
                    //cout << "elemento " << i << " no" << endl;
                }
            }

            if(think == pat){
                //cout << "\"igual\" sean gana " << sean << endl;
                //cout << "pat " << pat << endl;
                maximo = max(maximo, sean);
            }
        }

        cout << "Case #" << k << ": ";
        if(maximo == -1) cout << "NO" << endl;
        else cout << maximo << endl;

    }

	return 0;
}
