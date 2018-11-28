#include <iostream>
#include <vector>
using namespace std;

#include <fstream>

vector <string> vse;
vector <string> vqe;

/*
int minima_cantidad_elecciones(int i){ //i indica la consulta que se va haciendo
    int re; //re es la minima cantidad de cambios que se deben hacer en lo sucesivo.

    // resuelvo para el primer servidor que no sea igual a esta consulta
    int ise=0;
//    cout<<"vse.size()"<<vse.size()<<" vqe.size()"<<vqe.size()<<endl;
    if (vse[ise]==vqe[i]) {
//        cout<<"PRUEBA HOLA"<<endl;
    }
    for (ise=0; vse[ise]==vqe[i]; ise++){
//        cout<<vse[ise]<<" "<<vqe[i]<<endl;
    };

    // ahora ise es el indice del primer servidor que no es igual a esta consulta
    // SUPONGO QUE EXISTE UNO al menos
    // resuelvo para el primer servidor que no es igual a esta consulta como lo habia dicho

    // CORREGIR: LA ULTIMA VEZ PREGUNTO POR UNO QUE NO EXISTE
    int ii;
    for (ii=i; ii+1<vqe.size() && vqe[ii]!=vse[ise] ;ii++);
    if (ii+1==vqe.size() && vqe[ii]!=vse[ise]){ii++;}

    if (ii==vqe.size()){
        re=1; // pues hice solo una eleccion
    } else {
        re=minima_cantidad_elecciones(ii)+1;
    }

    // ahora ya tengo seteado re puedo hacer lo mismo y elegir el minimo re
    for (ise++; ise<vse.size() && re!=1; ise++){
        // resuelvo para cada servidor.
        for (; vse[ise]==vqe[i]; ise++);

        if (ise!=vse.size()){ //si hay alguno mas para corroborar
            // ahora ise es el indice del primer servidor que no es igual a esta consulta
            // resuelvo para el primer servidor que no es igual a esta consulta como lo habia dicho
            // CORREGIR: LA ULTIMA VEZ PREGUNTO POR UNO QUE NO EXISTE
            int ii;
            for (ii=i; ii+1<vqe.size() && vqe[ii]!=vse[ise] ;ii++);
            if (ii+1==vqe.size() && vqe[ii]!=vse[ise]){ii++;}

            if (ii==vqe.size()){
                re=1; // pues hice una eleccion
            } else {
                re=min(re,minima_cantidad_elecciones(ii)+1);
            }
        }
    }

    return re;
}
*/

int minima_cantidad_elecciones(int i){
    int re; //re es la minima cantidad de cambios que se deben hacer en lo sucesivo.

    // resuelvo para el primer servidor que no sea igual a esta consulta
    int ise=0;
//    cout<<"vse.size()"<<vse.size()<<" vqe.size()"<<vqe.size()<<endl;
//    if (vse[ise]==vqe[i]) {
//        cout<<"PRUEBA HOLA"<<endl;
//    }

    // simple pues supongo que siempre hay un servidor de entre TODOS al menos factible
    for (ise=0; vse[ise]==vqe[i]; ise++){
//        cout<<vse[ise]<<" "<<vqe[i]<<endl;
    };
//    cout<<"consulta ";
//    for (int k=0; k<i; k++) {cout<<" ";}
//    cout<<i<<" en adelante, servidor provisional ELEGIDO: "<<vse[ise]<<endl;

    // ahora ise es el indice del primer servidor que no es igual a esta consulta
    // SUPONGO QUE EXISTE UNO al menos
    // resuelvo para el primer servidor que no es igual a esta consulta como lo habia dicho

    // calculo el indice ii para este servidor, luego elegire el servidor con menor indice ii;
    int isee; //indice del servidor elegido
    int iimax; //iimaximo para el servidor elegido
    int ii;
    for (ii=i; ii+1<vqe.size() && vse[ise]!=vqe[ii]; ii++){
    }
    //for (ii=i; ii+1<vqe.size() && vqe[ii]!=vse[ise] ;ii++);
    if (ii+1==vqe.size() && vqe[ii]!=vse[ise]){ii++;} //
    iimax=ii;
    isee=ise;

    if (ii==vqe.size()){
        re=1; // pues hice solo una eleccion
        // Aqui termina por que encontre un servidor optimo hasta el final
    } else{
        re=0; // una bandera para seguir
    }// else {

    for (ise++; ise<vse.size() && re!=1; ise++){
        //isee=ise;
        //iimax=ii;
        for (; ise+1<vse.size() && vse[ise]==vqe[i]; ise++);
        if (ise+1==vse.size() && vse[ise]==vqe[i]) {ise++;}
      if (ise!=vse.size()){ // encontre un servidor mas
        for (ii=i; ii+1<vqe.size() && vse[ise]!=vqe[ii]; ii++);
        if (ii+1==vqe.size() && vqe[ii]!=vse[ise]){ii++;}

        if (ii>iimax) {
            iimax=ii;
            isee=ise;
        }

        if (ii==vqe.size()){
            re=1; // pues hice solo una eleccion
        // Aqui termina por que encontre un servidor optimo hasta el final
        } else{
            re=0; // una bandera para seguir
        }
      }

    }

    cout<<"consulta ";
    for (int k=0; k<i; k++) {cout<<" ";}
    cout<<i<<"a"<<iimax-1<<", servidor ELEGIDO: "<<vse[isee]<<endl;


    if (re!=1){
        re=minima_cantidad_elecciones(iimax)+1;
    }

    return re;
}

int main(){//int argc, char** argv){
//    ARGC=argc;
//    ARGV=argv;

//    INTERMEDIARIO grafico;
//    grafico.engraficoOpenGL(2,0,5);

  ifstream fin("A-large.in");//A-small-attempt1.in"); // "A-large.in" );
  ofstream fout( "A-large-salida.out");//-attempt1-salida.out");
  int N;
  fin>>N;
  cout<<N;

  for (int n=0; n<N; n++){
      vse.clear();
      vqe.clear();

      int S;
      fin>>S;
      cout<<"S: "<<S<<endl;

      char  enter[10];
      fin.getline(enter,255);


      for (int s=0; s<S; s++){//
          string se;
          char cadena[101];
          fin.getline(cadena,255);
          se=cadena;
          //fin>>se;
          vse.push_back(se);
          cout<<"s:"<<s<<" "<<vse[s]<<endl;
      }

      int Q;
      fin>>Q;
      cout<<"Q"<<Q<<endl;
      fin.getline(enter,255);

      for (int q=0; q<Q; q++){
          string qe;
          char cadena[101];
          fin.getline(cadena,255);
          qe=cadena;
          //fin>>qe;
          vqe.push_back(qe);
          cout<<vqe[q]<<endl;
      }
      if (Q==0) {
          cout<<"Case #"<<n+1<<": "<<0<<endl; //descuento la primera eleccion
    fout<<"Case #"<<n+1<<": "<<0<<endl;
      cout<<endl;
      }else{
      cout<<"Case #"<<n+1<<": "<<minima_cantidad_elecciones(0)-1<<endl; //descuento la primera eleccion
      fout<<"Case #"<<n+1<<": "<<minima_cantidad_elecciones(0)-1<<endl;
      cout<<endl;
      }
  }

  cout<<"Presiona una tecla para continuar"<<endl;
  cin.get() ;
  cout<<endl;
//  fout<<endl;

  fin.close();
  fout.close();

//    cout<<"CANTIDAD DE HILOS"<<vhilo.size()<<endl;

//    for (unsigned int i=0; i<vhilo.size(); i++){
//        pthread_join(vhilo[i], NULL);
//    }

    cout << "Hello world!" << endl;
    return 0;
}
