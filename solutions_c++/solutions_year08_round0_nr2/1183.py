#include <iostream>
#include <vector>
using namespace std;
#include <fstream>

 bool first( pair<int,int> a, pair<int,int> b ) {
   return a.first < b.first;
 };

int main(){//int argc, char** argv){
//    ARGC=argc;
//    ARGV=argv;

//    INTERMEDIARIO grafico;
//    grafico.engraficoOpenGL(2,0,5);


  ifstream fin("B-large.in");//B-small-attempt0.in");//ejemplo_00.in");//B-small02.in"); // "A-large.in" );
  ofstream fout( "B-large-salida.out");//salida02.out");
  int N;
  fin>>N;
  cout<<"Cantidad de casos de prueba: "<<N<<endl;

  for (int n=0; n<N; n++){
      int salenA=0;
      int salenB=0;

      int T;
      fin>>T;
      cout<<"Caso "<<n+1<<" turnaround "<<T<<endl;
      int nA;
      fin>>nA;
      int nB;
      fin>>nB;
      cout<<nA<<" "<<nB<<endl;

      vector< pair<int,int> > A;
      pair<int,int> a;
      vector< pair<int,int> > B;
      pair<int,int> b;
      string s;
      getline( fin, s );
      for (int iA=0; iA<nA; iA++){
          getline( fin, s );
          a.first=(s[0]-'0')*600+(s[1]-'0')*60+(s[3]-'0')*10+(s[4]-'0');
          a.second=(s[6]-'0')*600+(s[7]-'0')*60+(s[9]-'0')*10+(s[10]-'0');
          cout << "You entered " << s <<" "<<a.first<<" - " <<a.second<< endl;
          A.push_back(a);

      }

      for (int iB=0; iB<nB; iB++){
          getline( fin, s );
          b.first=(s[0]-'0')*600+(s[1]-'0')*60+(s[3]-'0')*10+(s[4]-'0');
          b.second=(s[6]-'0')*600+(s[7]-'0')*60+(s[9]-'0')*10+(s[10]-'0');
          cout << "You entered " << s <<" "<<b.first<<" - " <<b.second<< endl;
          B.push_back(b);
      }

      sort(A.begin(),A.end(), first);
      sort(B.begin(),B.end(), first);


//      vector<pair<int,int> >::iterator itAaux=itA;
//      vector<pair<int,int> >::iterator itBaux=itB;

      //Buscando el inicial
      bool Bsigue=false;

      bool hayMas=true;




      while(hayMas){

      vector<pair<int,int> >::iterator itA=A.begin();
      vector<pair<int,int> >::iterator itB=B.begin();
      bool seguir=true;

      if (itA!=A.end() && itB!=B.end()){
          Bsigue=(*itA).first<=(*itB).first;
          if (Bsigue){
              salenA++;
          }else{
              salenB++;
          }
      }else if(itA!=A.end()){
          Bsigue=true;
          salenA++;
      }else if(itB!=B.end()){
          Bsigue=false;
          salenB++;
      }else{
          hayMas=false;
          seguir=false;
      }


      if(itA!=A.end()) {
          cout<<"*itA=="<<(*itA).first<<endl;
      } else {
          cout<<"*itA==NULL"<<endl;
      }

      if(itB!=B.end()){
          cout<<"*itB=="<<(*itB).first<<endl;
      } else {
          cout<<"*itB==NULL"<<endl;
      }

        // Borro un recorrido
      while (seguir){

          if (Bsigue){
              int instante=(*itA).second+T;
              A.erase(itA);// si segui es por que habia uno antes asi que tiene sentido borrarlo
              itB=B.begin();

              while (itB!=B.end()){
                  if((*itB).first>=instante) break;
                  itB++;
              }
              if (itB==B.end()) { seguir=false;
              } else { Bsigue=false;}
//              } else {
//                  salenB++;
//              }

          }else{
              int instante=(*itB).second+T;
              B.erase(itB);
              itA=A.begin();
              while (itA!=A.end()){
                  if((*itA).first>=instante) break;
                  itA++;
              }
              if (itA==A.end()) { seguir=false;
              }else { Bsigue=true;}
//              } else {
//                  salenA++;
//              }
          }
      }

      }

      cout<<"Case #"<<n+1<<": "<<salenA<<" "<<salenB<<endl;
      fout<<"Case #"<<n+1<<": "<<salenA<<" "<<salenB<<endl;



  }

  cout<<"Presiona una tecla para continuar"<<endl;
  cin.get() ;
//  cout<<endl;
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
