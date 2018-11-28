#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main() {
    
    ifstream fin("/Users/usamaelnily/Desktop/in.txt");
    ofstream fout("/Users/usamaelnily/Desktop/out.txt");
    
    string op = "";
    int t, c = 1;
    char b[4][4];
    fin >> t;
    while(t--) {
        int tc = 0;
        bool x = 0, o = 0;
        
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                fin >> b[i][j];
            }
        }
        
        for(int i = 0; i < 4; i++) {
            int xc = 0;
            int oc = 0;
            for(int j = 0; j < 4; j++) {
                if(b[i][j] == 'X' || b[i][j] == 'T')
                    xc++;
                if(b[i][j] == 'O' || b[i][j] == 'T')
                    oc++;
                if(b[i][j] != '.')
                    tc++;
                if(xc == 4) {
                    x = 1;
                    break;
                } else if(oc == 4) {
                    o = 1;
                    break;
                }
            }
        }
        
        for(int i = 0; i < 4; i++) {
            int xc = 0;
            int oc = 0;
            for(int j = 0; j < 4; j++) {
                if(b[j][i] == 'X' || b[j][i] == 'T')
                    xc++;
                if(b[j][i] == 'O' || b[j][i] == 'T')
                    oc++;
                if(xc == 4) {
                    x = 1;
                    break;
                } else if(oc == 4) {
                    o = 1;
                    break;
                }
            }
        }
        
        int xcd = 0;
        int ocd = 0;
        for(int i = 0; i < 4; i++) {
            if(b[i][i] == 'X' || b[i][i] == 'T')
                xcd++;
            if(b[i][i] == 'O' || b[i][i] == 'T')
                ocd++;
            if(xcd == 4) {
                x = 1;
                break;
            } else if(ocd == 4) {
                o = 1;
                break;
            }
            
        }
        
        xcd = 0;
        ocd = 0;
        for(int i = 0; i < 4; i++) {
            if(b[i][3 - i] == 'X' || b[i][3 - i] == 'T')
                xcd++;
            if(b[i][3 - i] == 'O' || b[i][3 - i] == 'T')
                ocd++;
            if(xcd == 4) {
                x = 1;
                break;
            } else if(ocd == 4) {
                o = 1;
                break;
            }
            
        }
        
        if(x)
            op = "X won";
        else if(o)
            op = "O won";
        else if(tc >= 16)
            op = "Draw";
        else
            op = "Game has not completed";
        
        fout <<"Case #" << c << ": " << op << endl;
        c++;
    }
    return 0;
}