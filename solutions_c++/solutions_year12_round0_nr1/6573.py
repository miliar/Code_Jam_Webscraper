#include <iostream>
#include <fstream>
using namespace std;

int main(){

    char strings[30][100];
    char translate[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i',
                          'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p',
                          'f', 'm', 'a', 'q'};
    char x(0);
    int i, j, k(0);
    ifstream input;
    ofstream output;

    for (i=0; i<30; i++)
        for (j=0; j<100; j++)
            strings[i][j] = 0;

    input.open ("in.txt", ios::in);
    if ( input.fail() ){
        cout << "File Error opening input." << endl;
        cin >> i;
        return 1;
    }

    output.open ("out.txt",ios::out);
    if ( output.fail() ){
        cout << "Error opening output" << endl;
        cin >> i;
        return 1;
    }

    x = input.get();
    while (x!='\n'){
        k = (k*10) + (x-48);
        x = input.get();
    }

    i=j=0;

    x = input.get();
    while (!input.eof()){

        if (x == '\n'){
            i++;j=0;
        }else{
            if (j<100){
                strings[i][j] = x;
            }
            j++;
        }
        x = input.get();
    }

    for (i=0; i<k; i++){
        for (j=0; j<100; j++){
            if (strings[i][j] == 0){
                break;
            }else if (strings[i][j] != ' '){
                strings[i][j] = translate[strings[i][j]-97];
            }
        }
    }

    for (i=0; i<k; i++){
        j=0;
        if (i>0)
            output << endl;
        output << "Case #" << i+1 << ": ";
        while ((strings[i][j] != 0) && (j<100)){
            output << strings[i][j];
            j++;
        }
    }

    return 0;

}

