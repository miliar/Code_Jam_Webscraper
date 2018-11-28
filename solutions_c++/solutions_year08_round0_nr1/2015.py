//---------------------------------------------------------------------------

#include <vcl.h>
#include <stdio.h>
#include <iostream.h>
#include <fstream>
#include <string>
#include <cassert>
#include <iomanip>
#pragma hdrstop

//---------------------------------------------------------------------------

struct reg
{
  AnsiString motor;
  int cuenta;
  int deep;
  float wgt;
};

void incMotor(AnsiString Name, struct reg motores[], int e)
{
  for(int i=0; i<e; i++)
  {
     if(motores[i].motor==Name)
     {
       motores[i].cuenta++;
       return;
     }
  }
}

void SetDeep(AnsiString Name, struct reg motores[], int e, int index)
{
  for(int i=0; i<e; i++)
  {
     if(motores[i].motor==Name)
     {
        if(motores[i].deep == 9999)
          motores[i].deep=index;
        return;
     }
  }//end for
  return;
}

void SortMotor(struct reg motores[], int e)
{
  int auxc,auxd;
  float auxw;
  AnsiString auxm;
  for(int i=0; i<e-1; i++)
  {
    for(int j=i+1; j<e; j++)
    {
       if(motores[i].deep < motores[j].deep)
       {
          auxc=motores[i].cuenta;
          auxm=motores[i].motor;
          auxd=motores[i].deep;
          auxw=motores[i].wgt;
          motores[i].cuenta=motores[j].cuenta;
          motores[i].motor=motores[j].motor;
          motores[i].deep=motores[j].deep;
          motores[i].wgt=motores[j].wgt;
          motores[j].cuenta=auxc;
          motores[j].motor=auxm;
          motores[j].deep=auxd;
          motores[j].wgt=auxw;
       }//endif
     }//end j
  }//end i
  return;
}

/*void writeToFile(const std::string& fileName, const double& value)
{
  std::ofstream myFile(fileName.c_str());
  assert(myFile.is_open()==true);
  myFile << value << "\n";
  myFile.close();
}*/

#pragma argsused
int main(int argc, char* argv[])
{
  struct reg *motores=NULL;
  AnsiString *queries=NULL;
  AnsiString sengine,query;
  int n,e,q,y;
  AnsiString fileName;

  if(argc==1)
  {
     cout<<"Usage: "<<argv[0]<<"  <Case filename>"<<endl;
     return 0;
     fileName = "A-small-attempt1.txt";
  }
  else
     fileName = argv[1];

  //cout<<fileName.c_str()<<endl;
  //getchar();

  std::ifstream indata(fileName.c_str());
  char buf[101];
  AnsiString Cadena;

  //Obtener numero de casos
  indata.getline(buf,101);
  Cadena=buf;
  n=Cadena.ToInt();

  //cout<<"Numero de casos: "<<n<<endl;

  //Considerar cada caso
  for(int i=0; i<n; i++)
  {
     //Numero de intercambios
     y=0;
     //Obtener numero de motores de busqueda
     indata.getline(buf,101);
     Cadena=buf;
     e=Cadena.ToInt();
     if(motores!=NULL)
       delete []motores;
     motores=new reg[e];
     //Cargarlos en el arreglo
     for(int j=0; j<e; j++)
     {
        indata.getline(buf,101);
        Cadena=buf;
        motores[j].motor=Cadena;
        motores[j].cuenta=0;
        motores[j].deep=9999;
        motores[j].wgt=99999;
     }
     //Obtener numero de cadenas de busqueda para el caso
     indata.getline(buf,101);
     Cadena=buf;
     q=Cadena.ToInt();
     if(queries!=NULL)
       delete []queries;
     queries = new AnsiString[q];
     //Cargarlas en el arreglo
     for(int j=0; j<q; j++)
     {
        indata.getline(buf,101);
        Cadena=buf;
        queries[j]=Cadena;
        incMotor(Cadena,motores,e);
        SetDeep(Cadena,motores,e,j);
     }

      //Ahora calcular la distribución de búsquedas
     //Ordenar segun la frecuencia de queries
     SortMotor(motores,e);
     /*
     for(int j=0; j<e; j++)
     {
        cout<<"Motor: "<<motores[j].motor.c_str()<<" - "<<motores[j].wgt<<endl;
     }
     */

     //Empezar a procesar los queries
     int m=0;
     for(int j=0; j<q; j++)
     {
        //verificar si el motor es inusable
        if(queries[j]==motores[m].motor)
        {
          //Probar el proximo motor
          if(j!=0)
            y++;
          //Buscar el motor mas lejano en la lista
          for(int k=0; k<e; k++)
          {
             for(int l=j; l<q; l++)
             {
               motores[k].deep=9999;
               if(motores[k].motor==queries[l])
               {
                  motores[k].deep=l;
                  break;
               }
             }//end l
          }//end k
          SortMotor(motores,e);
        }//end if
     }//end forj
     cout<<"Case #"<<i+1<<": "<<y<<endl;
     //cout<<"---------------------"<<endl;
  }//end i
  //Pausa antes de salir
  //getchar();
  return 0;
}
//---------------------------------------------------------------------------
