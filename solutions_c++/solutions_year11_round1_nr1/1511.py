#include <stdio.h>
#include <stdlib.h>
#include <string> 
#include <iostream>
#include <queue>

using namespace std;


int main(void)
{
    int casos;
    int c = 1;

    cin >> casos;

    while(casos){
        int n, pd, pg;
        cin >> n;
        cin >> pd;
        cin >> pg;
        int encontro = 0;

        double parteDecimal;
        int parteInt;

    if(pg==100 && pd < 100)
        cout << "Case #" << c << ": " <<  "Broken" << endl;
    else if (pg==0 && pd > 0)
        cout << "Case #" << c << ": " <<  "Broken" << endl;
    else if (pd == 0)
        cout << "Case #" << c << ": " <<  "Possible" << endl;
    else{
        

        for (int i = 1; i <= n; i++) {
            parteInt = i*pd/100;
            parteDecimal = 1.0*i*pd/100 - parteInt;



            if(parteDecimal == 0){
                    cout << "Case #" << c << ": " <<  "Possible" << endl;
                    encontro = 1;
                    break;
                

            }
        }
        if(encontro==0)
            cout << "Case #" << c << ": " <<  "Broken" << endl;
    }
        casos--; 
        c++;
    }

    return 0;
}
