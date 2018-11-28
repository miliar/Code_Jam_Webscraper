#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <iostream>

using namespace std;

int main(){
    string infoCompetidores;
    int nCases;
    cin >> nCases;
//    getline (cin,infoCompetidores);
    int integrantes = 0;
    int qtdNotasExt = 0;
    double notaMinima = 0;
    double partNotasSomadas[3];
    int notas[3];
    double notaMax = 0.0;
    int qtdAcimaNotaMinima = 0;
      
    for(int n = 1; n<= nCases; n++){
            getline (cin,infoCompetidores);
            cin >> integrantes >> qtdNotasExt >> notaMinima;
      //      cout<<"nota minima: "<< notaMinima<< " qtd de notas extraordinarias :" << qtdNotasExt <<endl;
            for (int integ = 1; integ <= integrantes; integ++){
                 cin >> partNotasSomadas[integ];
        //         cout<<"notas somadas #"<<integ<<": "<< partNotasSomadas[integ]<< endl;
          //       cout<<"nota#"<<integ<<": "<< partNotasSomadas[integ]/3 << endl;
                 notaMax = ceil(partNotasSomadas[integ]/3);
                 
    //             cout<<"nota max #"<<integ<<": "<< notaMax<< endl;
                 if (notaMax >= notaMinima){
                    qtdAcimaNotaMinima++;
                 } else{
                        if(qtdNotasExt > 0 && notaMax > 0){
  //                          cout <<"Verificando Extraordinarias "<< trunc(partNotasSomadas[integ]/3)+trunc(partNotasSomadas[integ]/3)+(trunc(partNotasSomadas[integ]/3)+2) << endl;
  //                          cout <<"Verificando Extraordinarias "<< trunc(partNotasSomadas[integ]/3)+(trunc(partNotasSomadas[integ]/3)+2)+(trunc(partNotasSomadas[integ]/3)+2) << endl;
                            if(
                            ((trunc(partNotasSomadas[integ]/3)+trunc(partNotasSomadas[integ]/3)+(trunc(partNotasSomadas[integ]/3)+2) ==partNotasSomadas[integ] ) 
                            || (trunc(partNotasSomadas[integ]/3)+(trunc(partNotasSomadas[integ]/3)+2)+(trunc(partNotasSomadas[integ]/3)+2) ==partNotasSomadas[integ])) 
                            && ((trunc(partNotasSomadas[integ]/3)+2) >= notaMinima )
                            ){
                                qtdAcimaNotaMinima++;           
                                qtdNotasExt--;
                            }else{
//                                  cout <<"Continuando "<< (trunc(partNotasSomadas[integ]/3)-1)<< (trunc(partNotasSomadas[integ]/3))<< (trunc(partNotasSomadas[integ]/3)+1) << endl;
                                  if(((trunc(partNotasSomadas[integ]/3)-1)+(trunc(partNotasSomadas[integ]/3))+(trunc(partNotasSomadas[integ]/3)+1) == partNotasSomadas[integ] )
                                  &&(trunc(partNotasSomadas[integ]/3)+2) >= notaMinima ){
                                      qtdAcimaNotaMinima++;   
                                      qtdNotasExt--;                                                                                                         
                                  }
                              }
                         }
                 }
                 notaMax = 0.0;
                  
            }
            cout<<"Case #"<<n<<": "<<qtdAcimaNotaMinima << endl;
            qtdNotasExt = 0;
            qtdAcimaNotaMinima = 0;            
    }

    return 0;
}
