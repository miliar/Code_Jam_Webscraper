#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

int main() {

  ofstream file;
  file.open ("Output2.txt");

  int t;
  cin >> t;

  char arr[4][4];

  for(int k=1; k<=t; k++){

    bool faltan=false;

    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            cin >> arr[i][j];
            if(arr[i][j]=='.'){
                faltan=true;
            }
        }
    }

    string arrS[10];

    for(int i=0; i<4; i++){
        for(int j=0; j<4; j++){
            arrS[i].push_back(arr[i][j]);
        }
    }

    for(int j=0; j<4; j++){
        for(int i=0; i<4; i++){
            arrS[j+4].push_back(arr[i][j]);
        }
    }

    for(int i=0; i<4; i++){
        arrS[8].push_back(arr[i][i]);
    }

    for(int j=0; j<4; j++){
        arrS[9].push_back(arr[3-j][j]);
    }

    /*cout << endl;

    for(int i=0; i<10; i++){
        cout << arrS[i] << endl;
    }

    cout << endl;*/

    bool hayGanador=false;

    for(int i=0; i<10; i++){
        int contX=0, contO=0, contT=0;
        for(int j=0; j<4; j++){
            if(arrS[i].at(j)=='X'){
                contX++;
            } else if(arrS[i].at(j)=='O'){
                contO++;
            } else if(arrS[i].at(j)=='T'){
                contT++;
            }
        }

        if((contO+contT)==4){
            file << "Case #" << k << ": " << "O won" << endl;
            hayGanador=true;
            break;
        } else if((contX+contT)==4){
            file << "Case #" << k << ": " << "X won" << endl;
            hayGanador=true;
            break;
        }

    }

    if(hayGanador==false&&faltan==true){
        file << "Case #" << k << ": " << "Game has not completed" << endl;
    } else if(hayGanador==false&&faltan==false){
        file << "Case #" << k << ": " << "Draw" << endl;
    }


  }

  file.close();

  return 0;
}
