/* 
 * File:   main.cpp
 * Author: NQH
 * Problem A. Speaking in Tongues
 * Created on April 14, 2012, 1:29 PM
 */

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

#define MAXLEN 100

using namespace std;

const char map[] = "yhesocvxduiglbkrztnwjpfmaq";


int main() {  

    FILE *fin = fopen("A-small-attempt0.in", "r"); 
    ofstream fout ("proba.out");
            
    int t,nt,k;
    char s[MAXLEN];
    fscanf(fin,"%d\n",&nt);

    for (t=1; t<=nt; t++) {
        fout << "Case #" << t << ": " ;
        while (fgets(s, sizeof(s), fin)!= NULL) {

            k=0;
            while (s[k]!='\0' && s[k]!='\n') {
                
                if ('a'<=s[k] && s[k]<='z') s[k] = map[s[k]-'a'];
                k++;
            } 
            fout << s;
            if (s[k]=='\n') break;
	}
    }
        
    fclose(fin);
    
    return 0;
}
