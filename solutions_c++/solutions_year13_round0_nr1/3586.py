#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    //bool baigta = false;
    //char laimetojas = 'A';
    

    int n;
    fin >> n;
    for (int i=0; i <n; i++){
        int simboliai = 0;
        char laimetojas = 'A';
        bool baigta = false;
        // isivedam duomenis
        // 0 - niekas
        // 1 - kryziukas
        // 2 - nuliukas
        // 3 - T
        int lentele[4][4];
        for(int x = 0; x < 4; x++){
            for(int y = 0; y < 4; y++){
                char a;
                fin >> a;
                int k;
                if(a == '.'){
                    k = 0;
                }else if(a == 'X'){
                    k = 1;
                    simboliai++;
                }else if(a == 'O'){
                    k = 2;
                    simboliai++;
                }else if(a == 'T'){
                    k = 3;
                    simboliai++;
                }
                lentele[x][y] = k;
            }
        }
        // tikrinam stulpelius
        for(int x = 0; x < 4; x++){
            if((lentele[x][0]== 1 || lentele[x][0] == 3) &&(lentele[x][1]== 1 || lentele[x][1] == 3) && (lentele[x][2]== 1 || lentele[x][2] == 3) && (lentele[x][3]== 1 || lentele[x][3] == 3)){
                baigta = true;
                laimetojas = 'X';
            }else if((lentele[x][0]== 2 || lentele[x][0] == 3) && (lentele[x][1]== 2 || lentele[x][1] == 3) && (lentele[x][2]== 2 || lentele[x][2] == 3) && (lentele[x][3]== 2 || lentele[x][3] == 3)){
                baigta = true;
                laimetojas = 'O';
            }
        }
        
        //tikrinam eilutes
        for(int y = 0; y < 4; y++){
            if((lentele[0][y]== 1 || lentele[0][y] == 3) &&(lentele[1][y]== 1 || lentele[1][y] == 3) && (lentele[2][y]== 1 || lentele[2][y] == 3) && (lentele[3][y]== 1 || lentele[3][y] == 3)){
                baigta = true;
                laimetojas = 'X';
            }else if((lentele[0][y]== 2 || lentele[0][y] == 3) && (lentele[1][y]== 2 || lentele[1][y] == 3) && (lentele[2][y]== 2 || lentele[2][y] == 3) && (lentele[3][y]== 2 || lentele[3][y] == 3)){
                baigta = true;
                laimetojas = 'O';
            }
        }
        
        //tikrinam istrizaines
        if((lentele[0][0] == 1 || lentele[0][0] == 3) && (lentele[1][1] == 1 || lentele[1][1] == 3) && (lentele[2][2] == 1 || lentele[2][2] == 3) && (lentele[3][3] == 1 || lentele[3][3] == 3)){
            baigta = true;
            laimetojas = 'X';
        }

        if((lentele[0][3] == 1 || lentele[0][3] == 3) && (lentele[1][2] == 1 || lentele[1][2] == 3) && (lentele[2][1] == 1 || lentele[2][1] == 3) && (lentele[3][0] == 1 || lentele[3][0] == 3)){
            baigta = true;
            laimetojas = 'X';
        }
        
        if((lentele[0][0] == 2 || lentele[0][0] == 3) && (lentele[1][1] == 2 || lentele[1][1] == 3) && (lentele[2][2] == 2 || lentele[2][2] == 3) && (lentele[3][3] == 2 || lentele[3][3] == 3)){
            baigta = true;
            laimetojas = 'O';
        }
        
        if((lentele[0][3] == 2 || lentele[0][3] == 3) && (lentele[1][2] == 2 || lentele[1][2] == 3) && (lentele[2][1] == 2 || lentele[2][1] == 3) && (lentele[3][0] == 2 || lentele[3][0] == 3)){
            baigta = true;
            laimetojas = 'O';
        }

        fout << "Case #" << i+1 << ": ";
        if(baigta){
                   fout << laimetojas << " won";           
        }else{
              if(simboliai == 16){
                           fout << "Draw";
              }else{
                    fout << "Game has not completed"  ;    
              }      
        }
        fout << endl;
        
    }


    return 0;
}