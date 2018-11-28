/* 
 * File:   main.cpp
 * Author: dgleeman
 *
 * Created on April 14, 2012, 1:28 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>

/*
 * 
 */

using namespace std;

int main() {

    int numlines = 3;
    char trans[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

    string ctext;
    string ptext;

    cin >> numlines;
    getline(cin, ctext);

    char cchar;
    char pchar;

    cout << "numlines is "<< numlines << endl;

    for(int i=0; i<numlines; i++){
        cout << "Case #"<<i+1<<": ";
        getline(cin, ctext);
        for(int j=0; j<ctext.length(); j++){
            cchar = ctext[j];
            if(cchar == ' '){
                pchar = ' ';
            }else{
                pchar = trans[cchar - 'a'];
            }
            cout << pchar;
        }
        cout << '\n';
    }


}

