//
//
//

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main() {

    ifstream input("data.txt");
    int iL,iD,iN;
    string* words;

    input >> iL >> iD >> iN;

    words = new string[iD];

    for ( int i = 0; i < iD ; i++ ) {
        input >> words[i];
    }

    for ( int i = 0; i < iN; i++ ) {
        string check;
        int num = 0;

        input >> check;

        for ( int l = 0; l < iD; l++){
            int checkflag = true;
            int index = 0;
            int inflag = false;
            for ( int j = 0; j < check.size(); j++ ) {
                if ( !inflag && check.at(j) == '(' ) {
                    inflag = true;
                    j++;
                }

//cout << l << "word " << words[l].at(index) <<index<< " " << j << endl;
                if ( !inflag && words[l].at(index) != check.at(j) ){
                    checkflag = false;
                    break;
                }
                if (inflag) {
                    checkflag = false;
                    while ( check.at(j) != ')' ) {
                        if (words[l].at(index) == check.at(j)){
                             checkflag = true;
                        }
                        j++;
                    } 
                    inflag = false;
                    if (!checkflag)
                        break;
                }
                if ( !inflag )
                        index++;
            }
            if (checkflag)
                num++;
        }

        cout << "Case #" << i+1 << ": " << num << endl;
    }

    delete []words;
    
    return 1;
}
