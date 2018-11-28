#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    ifstream file("A-large.in");
    ofstream output;
    output.open("output.txt", ios::trunc);

    string iline;

    int cases;
    getline(file,iline);
    stringstream(iline) >> cases;

    for(int x = 1; x <= cases; x++){
        string lines[4];
        for(int u = 0; u <= 3; u++){getline(file,lines[u]);}

        bool xwin = false, owin = false;

        int xnum = 0, onum = 0, tnum = 0;
        for(int r = 0; r <= 3; r++){
            xnum = 0; onum = 0; tnum = 0;
            for(int c = 0; c <= 3; c++){
                if(lines[r][c] == 'X'){xnum++;}
                else if(lines[r][c] == 'O'){onum++;}
                else if(lines[r][c] == 'T'){tnum++;}
            }
            if( (xnum == 3 && tnum == 1) || xnum == 4){xwin = true; break;}
            else if( (onum == 3 && tnum == 1) || onum == 4){owin = true; break;}
        }

        if(xwin == false && owin == false){
            for(int a = 0; a <= 3; a++){
                xnum = 0; onum = 0; tnum = 0;
                for(int b = 0; b <= 3; b++){
                    if(lines[b][a] == 'X'){xnum++;}
                    else if(lines[b][a] == 'O'){onum++;}
                    else if(lines[b][a] == 'T'){tnum++;}
                }
                if( (xnum == 3 && tnum == 1) || xnum == 4){xwin = true; break;}
                else if( (onum == 3 && tnum == 1) || onum == 4){owin = true; break;}
            }
        }

        if(xwin == false && owin == false){
            xnum = 0; onum = 0; tnum = 0;
            for(int g = 0, h = 0; g <= 3; g++, h++){
                if(lines[g][h] == 'X'){xnum++;}
                else if(lines[g][h] == 'O'){onum++;}
                else if(lines[g][h] == 'T'){tnum++;}
            }
            if( (xnum == 3 && tnum == 1) || xnum == 4){xwin = true;}
            else if( (onum == 3 && tnum == 1) || onum == 4){owin = true;}
        }

        if(xwin == false && owin == false){
            xnum = 0; onum = 0; tnum = 0;
            for(int j = 3, k = 0; j >= 0; j--, k++){
                if(lines[j][k] == 'X'){xnum++;}
                else if(lines[j][k] == 'O'){onum++;}
                else if(lines[j][k] == 'T'){tnum++;}
            }
            if( (xnum == 3 && tnum == 1) || xnum == 4){xwin = true;}
            else if( (onum == 3 && tnum == 1) || onum == 4){owin = true;}
        }

        if(xwin == true){output << "Case #" << x << ": X won" << '\n';}
        else if(owin == true){output << "Case #" << x << ": O won" << '\n';}
        else{
            bool full = true;
            for(int v = 0; v <= 3; v++){for(int w = 0; w <= 3; w++){if(lines[v][w] == '.'){full = false;}}}

            if(full == true){output << "Case #" << x << ": Draw" << '\n';}
            else{output << "Case #" << x << ": Game has not completed" << '\n';}
        }

        getline(file,iline);
    }

    file.close();
    output.close();

    return 0;
}
