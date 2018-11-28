#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int cases;
    cin>>cases;
    char letras[100];
    int naranja[100], azul[100];
    for(int u = 0;u<cases;u++)
    {
            int tam;
            int blu = 1;
            int ora  =1;
            int az = 0;
            int nar = 0;
          cin>>tam;
          for(int i = 0;i < tam;i++)
          {
                  char caracter;
                  int puesto;
                cin>>caracter;
                if(caracter == 'O')
                            puesto = 1;
                if(caracter == 'B')
                            puesto = 2;
                letras[i] = caracter;

                int num;
                cin>>num;
                            if(puesto == 1)
                                      naranja[nar++] =num;
                            if(puesto == 2)
                                      azul[az++] = num;


          }
          long long int tiempo=0;
          int b= 0, o = 0;
          for( int i =0; i < tam; i++)
          {

              int pos;
              char actual = letras[i];
              if( actual == 'O')
              {
                  long long int diftiempo = ( abs((double)(naranja[o]-ora)) +1);

                 tiempo += diftiempo;
                 ora = naranja[o++];
                 if( abs((double)(blu-azul[b]))<= diftiempo)
                 {
                     blu = azul[b];

                 }
                 else
                 {
                     if(blu < azul[b])
                               blu += diftiempo;
                     else
                         blu-=diftiempo;
                 }

              }
              else
              {

                  long long int diftiempo = abs((double)(azul[b]-blu)) +1;
                 tiempo += diftiempo;
                 blu = azul[b++];
                 if( abs((double)(ora-naranja[o]))<= diftiempo)
                 {
                     ora = naranja[o];

                 }
                 else
                 {
                     if(ora < naranja[o])
                     ora += diftiempo;
                     else ora -=diftiempo;
                 }

              }

          }
          if(u != 0)
               cout<<endl;
          cout<<"Case #"<<u+1<<": "<<tiempo;





    }
}
