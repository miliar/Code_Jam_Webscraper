#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char** argv){
    ofstream salida("A.out.txt");
    cout.rdbuf(salida.rdbuf());

    long long int n;
    int pd, pg, t, k, d, i, j;
    int tope;
    bool posible;
    cin >> t;
    for(k=1; k<=t; k++){
        cin >> n >> pd >> pg;
        posible = false;
        tope = min(n, 100LL);

        if(pd>0 && pg==0){
            cout << "Case #"<<k<<": Broken" << endl;
        }
        else if(pg==100 && pd<100){
            cout << "Case #"<<k<<": Broken" << endl;
        }
        else{
            for(d=1; d<=tope; d++){
                if(d*pd%100 == 0){
                    posible = true;
                    break;
                }
            }
            cout << "Case #"<<k<<": ";
            if(posible) cout << "Possible" << endl;
            else cout << "Broken" << endl;
        }
    }
	return 0;
}
