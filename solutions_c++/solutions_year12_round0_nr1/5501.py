#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <iostream>

using namespace std;
char equiv [2][200];

void PreencherDicionario (){
    string texLingNat = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up q z" ;
    string texLingNotNat = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv z q" ;
             
    for (int coluna = 0; coluna < texLingNat.size(); coluna++){
        
        equiv[0][coluna] = texLingNat[coluna];
        equiv[1][coluna] = texLingNotNat[coluna];
    }
    
}
   
char LetraEquivalente(char c){
    for (int coluna = 0; coluna < 200; coluna ++){
        if (c ==equiv[1][coluna] ){
          return equiv[0][coluna];
        }
    } 
}


int main (){
    PreencherDicionario ();

    string palavraASerConvertida;
    string palavraConvertida;
    
    int nCases;
    
    cin >> nCases;
    getline (cin,palavraASerConvertida);
    for(int n = 1; n<= nCases; n++){
        cout<< "Case #"<< n <<": " ;
        getline (cin,palavraASerConvertida);
        for (int i = 0; i < palavraASerConvertida.size(); i++){
            cout<< LetraEquivalente(palavraASerConvertida[i]);
        }   
        cout << endl;
    }
    
    return 0;   
}
