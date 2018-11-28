#include <iostream>
#include <windows.h>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    int C, D, N, T;
    string cTab[50], dTab[50], inv, out;
    fstream plikIn ("small.in", fstream::in | fstream::out);
    fstream plikOut ("small.out", fstream::in | fstream::out);

    plikIn >> T;

    for(int i=0;i<T;i++) {
        plikIn >> C;
        for(int j=0;j<C;j++) {
            plikIn >> cTab[j];

        }
        plikIn >> D;
        for(int j=0;j<D;j++) {
            plikIn >> dTab[j];
        }
        plikIn >> N;


        plikIn >> inv;
        //cout << "+" << inv << endl;
        Sleep(200);
        cout << "new";
        out.clear();
        for(int j=0;j<N;j++) {
            out += inv[j];
            cout << "[" << out << "]" << endl;
            if(j) {
                for(int k=0;k<C;k++) {
                    if( (cTab[k][0] == out[out.length()-2] && cTab[k][1] == out[out.length()-1]) ||
                       (cTab[k][1] == out[out.length()-2] && cTab[k][0] == out[out.length()-1])) {
                           cout << "(" << out.substr(0,j-1) << ")";
                        out = out.substr(0,out.length()-2);
                        cout << "+";
                        cout << "<" << cTab[k][2] << ">";
                        out += cTab[k][2];
                        cout << out;
                        break;
                    }
                }
                for(int k=0;k<D;k++) {
                    for(int l=0;l<out.length()-1;l++) {
                        if( (dTab[k][0] == out[l] && dTab[k][1] == out[out.length()-1]) ||
                            (dTab[k][1] == out[l] && dTab[k][0] == out[out.length()-1])) {
                            out.clear();
                            cout << "+";
                            cout << out << "|";
                            break;
                        }
                    }
                }
            }

        }

        cout << endl << ">>" << out << endl;


        plikOut << "Case #" << i+1 << ": [";
        for(int j=0;j<out.length();j++)
        {
            if(j) plikOut << ", ";
            plikOut << out[j];
        }
        plikOut << "]" << endl;

    }



    plikIn.close();
    plikOut.close();

    return 0;
}
