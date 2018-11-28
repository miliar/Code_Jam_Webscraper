#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
#include<vector>

using namespace std;


int Min4 (int A, int B, int C, int D)
{
    int Fin=A;
    if(Fin>B)
        Fin=B;
    if(Fin>C)
        Fin=C;
    if(Fin>D)
        Fin=D;
    return(Fin);
}

void AlgoTrain(string* line1,string* line2, int Temps,  int N1, int N2, int numSol)
{
    /*
    for(int i=0; i<N1; i++)
        cout<<line1[i]<<endl;
    cout<<endl;
    for(int i=0;i<N2;i++)
        cout<<line2[i]<<endl;
    cout<<endl<<endl<<endl;
    */
    
    //On trie le temps: conversion int puis triage croissant
    int * PointA =new int[N1+1];
    int * PointB =new int[N2+1];
    int * PointAS =new int[N1+1];
    int * PointBS =new int[N2+1];
    
   for(int i=0; i<N1; i++)
   {
       int a=line1[i].find(":",0);
       int b=line1[i].find(" ",a);
       int c=line1[i].find(":",b);
       PointA[i]=atoi(line1[i].substr(0,2).c_str())*60 + atoi(line1[i].substr(a+1,2).c_str());
       PointAS[i]=atoi(line1[i].substr(b+1,2).c_str())*60 + atoi(line1[i].substr(c+1,2).c_str());
   }
   for(int i=0; i<N2; i++)
   {
       int a=line2[i].find(":",0);
       int b=line2[i].find(" ",a);
       int c=line2[i].find(":",b);
       PointB[i]=atoi(line2[i].substr(0,2).c_str())*60 + atoi(line2[i].substr(a+1,2).c_str());
       PointBS[i]=atoi(line2[i].substr(b+1,2).c_str())*60 + atoi(line2[i].substr(c+1,2).c_str());
   }
    /*
   if(numSol==1) 
   {
         for(int i=0; i<N2; i++)
            cout<<PointBS[i]<<" ";
             cout<<endl;cout<<endl;
   }*/
    
  int Min;
  int IdMin;
  int* PointASort= new int[N1+1];
  int* PointASortS= new int[N1+1];
  int* PointBSort= new int[N2+1];
  int* PointBSortS= new int[N2+1];
  for(int i=0; i<N1; i++)
  {
      Min=1450;
         for(int j=0;j<N1;j++)
         {
             if(PointA[j]<Min)
             {
                 Min=PointA[j];
                 IdMin=j;
             }
         }
      PointASort[i]=Min;
      PointA[IdMin]=1450;
  }
  for(int i=0; i<N1; i++)
  {
      Min=1450;
         for(int j=0;j<N1;j++)
         {
             if(PointAS[j]<Min)
             {
                 Min=PointAS[j];
                 IdMin=j;
             }
         }
      PointASortS[i]=Min+(int)Temps;
      PointAS[IdMin]=1450;
  }
  
  for(int i=0; i<N2; i++)
  {
      Min=1450;
         for(int j=0;j<N2;j++)
         {
             if(PointB[j]<Min)
             {
                 Min=PointB[j];
                 IdMin=j;
             }
         }
      PointBSort[i]=Min;
      PointB[IdMin]=1450;  
  }
  for(int i=0; i<N2; i++)
  {
      Min=1450;
         for(int j=0;j<N2;j++)
         {
             if(PointBS[j]<Min)
             {
                 Min=PointBS[j];
                 IdMin=j;
             }
         }
      PointBSortS[i]=Min+(int)Temps;
      PointBS[IdMin]=1450;
  }
  /*
  if(numSol==1)
  {
   for(int i=0; i<N1; i++)
      cout<<PointASort[i]<<" ";
  cout<<endl;
  for(int i=0; i<N2; i++)
      cout<<PointBSort[i]<<" ";
    cout<<endl;cout<<endl;
    
    for(int i=0; i<N1; i++)
      cout<<PointASortS[i]<<" ";
    cout<<endl;cout<<endl;
    for(int i=0; i<N2; i++)
      cout<<PointBSortS[i]<<" ";
    cout<<endl;cout<<endl;
    
    }*/
  
  cout<<"Begin to check the trains"<<endl;
  int Ida=0, Idb=0, IdaS=0, IdbS=0;
  int TrA=0, TrB=0;
  int SolA=0, SolB=0;
  bool Stop1=0, Stop2=0;
  if(N2==0)
      Stop2=true;
  if(N1==0)
      Stop1=true;
  PointASort[N1]=1450;PointBSort[N2]=1450;PointASortS[N1]=1450;PointBSortS[N2]=1450;
  
  do
  {
      //Trouver l'action prioritaire: arrivée puis départ
      int Mini=Min4(PointASort[Ida],PointBSort[Idb],PointASortS[IdaS],PointBSortS[IdbS]);
     
      //Si les trains ont fini d'attendre
      if(PointASortS[IdaS]==Mini && IdaS<N1)
      {
          TrB++;
          IdaS++;
      }
       if(PointBSortS[IdbS]==Mini && IdbS<N2)
       {
          TrA++;
          IdbS++;
       }
      
      //Si les trains demarre
       if(PointASort[Ida]==Mini )
       {
           if(Ida==N1-1)
               Stop1=true;
           
           if(Ida<N1)
           {
               Ida++;
               if(TrA>0)
                    TrA--;
               else
                   SolA++;
           }
       }
       if(PointBSort[Idb]==Mini )
       {
           if(Idb==N2-1)
               Stop2=true;
           
           if(Idb<N2)
           {
               Idb++;
               if(TrB>0)
                    TrB--;
               else
                   SolB++; 
           }
       }
  }
  while(!Stop1 || !Stop2);
  
  cout<<SolA<<" "<<SolB<<endl;
  ofstream outfile;
  outfile.open ("Output0.txt", ios::out | ios::app);
  outfile<<"Case #"<<numSol<<": "<<SolA<<" "<<SolB<<endl;
    
}
