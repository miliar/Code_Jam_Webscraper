#include <stdio.h>
#include <stdlib.h>
#include <string> 
#include <iostream>

using namespace std;

int main(void)
{
    int casos;
    int c = 1;
    cin >> casos;

    while(casos){
        char comb[30][30];
        int oppo[30][30];
        for (int i = 0; i < 30; i++) {
            for (int y = 0; y < 30; y++) {
                comb[i][y] = '?';
                oppo[i][y] = 0;
            }
        }

        int comn;
        cin >> comn;

        for (int i = 0; i < comn; i++) {
            string temp;
            cin >> temp;
            comb[temp[0]-'A'][temp[1]-'A'] = temp[2];
            comb[temp[1]-'A'][temp[0]-'A'] = temp[2];
        }

        int oppon;
        cin >> oppon;

        for (int i = 0; i < oppon; i++) {
            string temp;
            cin >> temp;
            oppo[temp[0]-'A'][temp[1]-'A'] = 1;
            oppo[temp[1]-'A'][temp[0]-'A'] = 1;
        }

        int len;
        cin >> len;

        string linea;
        cin >> linea;

        string final;
        //final.resize(110);
        final += linea[0];
        int clear = 0;
        char ult = linea[0];

        for (int i = 1; i < len; i++) {
            
            if(ult != '?' && comb[linea[i]-'A'][ult-'A']!='?'){
                final = final.substr(0,final.length()-1);
                ult = comb[linea[i]-'A'][ult-'A'];
                final += ult;
            }
            else{
                clear=0;
                for (int y = 0; y < 26; y++) {
                    if(oppo[linea[i]-'A'][y] && final.find('A'+y)!=string::npos){
                        ult = '?';
                        final.clear();
                        //final.resize(110);
                        clear = 1;
                        break;
                    }
                }
                if(clear==0){
                    final += linea[i];
                    ult = linea[i];
                }
                    
            }
        }



        cout << "Case #" << c << ": [";
        if(clear)
            cout << "]" << endl;
        else{
            int x;
            for ( x = 0; x < final.length()-1; x++)
                cout << final[x] << ", ";
            cout << final[x] << "]" <<endl;
        }

        casos--; 
        c++;
    }

    return 0;
}
