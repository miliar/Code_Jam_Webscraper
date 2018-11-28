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
  AnsiString departure;
  AnsiString arrival;
  float depart;
  float arriv;
};

float TimeToFloat(AnsiString hora)
{
   float h,m;
   h=hora.SubString(0,2).ToDouble();
   m=hora.SubString(4,2).ToDouble();
   return(h+m/60);
}

void sort(float v[],int n)
{
  float aux;
  for(int i=0; i<n-1;i++)
  {
    for(int j=i; j<n;j++)
    {
       if(v[i]<v[j])
       {
         aux=v[i];
         v[i]=v[j];
         v[j]=aux;
       }
    }//end j
  }//end i
}

#pragma argsused
int main(int argc, char* argv[])
{
  struct reg *timetableA=NULL;
  struct reg *timetableB=NULL;
  float *salidasA=NULL;
  float *salidasB=NULL;

  int n,nta,ntb,rt,ha,hb;
  AnsiString fileName;

  if(argc==1)
  {
     //cout<<"Usage: "<<argv[0]<<"  <Case filename>"<<endl;
     //return 0;
     fileName = "B-small-attempt0.in";
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
     nta=0;
     ntb=0;
     //Obtener round trip
     indata.getline(buf,101);
     Cadena=buf;
     rt=Cadena.ToInt();
     //cout<<"Round trip time: "<<rt<<endl;

     //Tamaño tablas de tiempo
     indata.getline(buf,101);
     Cadena=buf;
     Cadena=Cadena.Trim();
     int pos=Cadena.Pos(" ");
     ha=Cadena.SubString(0,pos-1).ToInt();
     hb=Cadena.SubString(pos+1,10).ToInt();


     //cout<<"A to B: "<<ha<<"  B to A: "<<hb<<endl;
     if(timetableA!=NULL)
       delete [] timetableA;
     timetableA=new reg[ha];
     if(timetableB!=NULL)
       delete [] timetableB;
     timetableB=new reg[hb];
     if(salidasA!=NULL)
       delete [] salidasA;
     salidasA=new float[hb];
     if(salidasB!=NULL)
       delete [] salidasB;
     salidasB=new float[ha];

     for(int j=0; j<ha; j++)
     {
        indata.getline(buf,101);
        Cadena=buf;
        Cadena=Cadena.Trim();
        int pos=Cadena.Pos(" ");
        timetableA[j].departure=Cadena.SubString(0,Cadena.Length()-pos);
        timetableA[j].depart=TimeToFloat(timetableA[j].departure);
        timetableA[j].arrival=Cadena.SubString(pos+1,10);
        timetableA[j].arriv=TimeToFloat(timetableA[j].arrival);
        salidasB[j]=timetableA[j].arriv+((float)rt/60.0);
        //cout<<timetableA[j].departure.c_str()<<" "<<timetableA[j].arrival.c_str()<<endl;
     }
     for(int j=0; j<hb; j++)
     {
        indata.getline(buf,101);
        Cadena=buf;
        Cadena=Cadena.Trim();
        int pos=Cadena.Pos(" ");
        timetableB[j].departure=Cadena.SubString(0,Cadena.Length()-pos);
        timetableB[j].depart=TimeToFloat(timetableB[j].departure);
        timetableB[j].arrival=Cadena.SubString(pos+1,10);
        timetableB[j].arriv=TimeToFloat(timetableB[j].arrival);
        salidasA[j]=timetableB[j].arriv+((float)rt/60.0);
        //cout<<timetableB[j].departure.c_str()<<" "<<timetableB[j].arrival.c_str()<<endl;
     }
     //Se ordenan las posibles horas de salida de mayor a menor
     sort(salidasA,hb);
     sort(salidasB,ha);

     //Buscar cuantos trenes se necesitan desde A hasta B
     for(int j=0; j<ha; j++)
     {
        bool found=false;
        for(int k=0; k<hb; k++)
        {
          if(timetableA[j].depart>=salidasA[k])
          {
            found=true;
            salidasA[k]=999999.99;
            break;
          }
        }//end k
        if(!found)
          nta++;
     }

     //Buscar cuantos trenes se necesitan desde B hasta A
     for(int j=0; j<hb; j++)
     {
        bool found=false;
        for(int k=0; k<ha; k++)
        {
          if(timetableB[j].depart>=salidasB[k])
          {
            found=true;
            salidasB[k]=999999.99;
            break;
          }
        }//end k
        if(!found)
          ntb++;
     }
     cout<<"Case #"<<i+1<<": "<<nta<<" "<<ntb<<endl;
  }//end i casos

  //Pausa antes de salir
  //getchar();
  return 0;
}
//---------------------------------------------------------------------------
