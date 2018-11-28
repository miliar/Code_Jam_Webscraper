#include <iostream>
#include <vector>

using namespace std;

#include <fstream>


double productoEscalar(vector <int> x, vector <int> y){
    double re=0;
    for (int i=0; i<x.size(); i++){
        re+=x[i]*y[i];
    }
    return re;
}

double productoEscalarMinimo(vector <int> x, vector <int> y){
    if (x.size()==0) return 0;
    int x0=x[0];
    vector<int> yy;
//    int yi;

    x.erase(x.begin());
    long int re,rea;
    bool primeraVez=true;
    for( int i=0; i<y.size(); i++){
        yy.clear();
        for (int ii=0; ii<y.size(); ii++){
            if (ii!=i) yy.push_back(y[ii]);
        }
        if (primeraVez) {
            re=x0*y[i]+productoEscalarMinimo(x,yy);
            primeraVez=false;
        }else{
            rea=x0*y[i]+productoEscalarMinimo(x,yy);
            if (rea<re) re=rea;
        }
    }
    return re;
}

int main(){//int argc, char** argv){
//    ARGC=argc;
//    ARGV=argv;

//    INTERMEDIARIO grafico;
//    grafico.engraficoOpenGL(2,0,5);

  ifstream fin("A-small-attempt1.in");//entrada.in"); // "A-large.in" );
  ofstream fout( "A-small-salida1.out");//salida.out");
  int T;
  fin>>T;
  cout<<"Cantidad de casos: "<<T<<endl;
  long int minimo;
  vector <int> x;
  vector <int> y;
  int n;
  int aux;
  for (int t=0; t<T; t++){
      x.clear();
      y.clear();
      fin>>n;
      cout<<"Caso "<<t+1<<": cada vector tiene "<<n<<" elementos:"<<endl;
      for (int nn=0; nn<n; nn++){
          fin>>aux;
          x.push_back(aux);
      }

      for (int nn=0; nn<n; nn++){
          fin>>aux;
          y.push_back(aux);
      }

      minimo=productoEscalarMinimo(x,y);
      cout<<"Case #"<<t+1<<": "<<minimo<<endl;
      fout<<"Case #"<<t+1<<": "<<minimo<<endl;




  }

//  string en,en0,en1;
//  fin>>en0;
//  fin>>en1;

//    for (int ll=0; ll<14; ll++){
//        grafico.engraficoOpenGL(-4,ll, 0.01);
//    }











  cout<<"Presiona una tecla para continuar"<<endl;
  cin.get() ;
  cout<<endl;
  fout<<endl;


  fin.close();
  fout.close();


//    cout<<"CANTIDAD DE HILOS"<<vhilo.size()<<endl;

//    for (unsigned int i=0; i<vhilo.size(); i++){
//        pthread_join(vhilo[i], NULL);
//    }

    cout << "Hello world!" << endl;
    return 0;
}
