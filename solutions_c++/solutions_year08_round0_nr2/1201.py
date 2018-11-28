#include <iostream>
#include <map>
#include <string>
#include <cstdio>

using namespace std;

 int compare_ints( const void* a, const void* b ) {
   int* arg1 = (int*) a;
   int* arg2 = (int*) b;
   if( *arg1 < *arg2 ) return -1;
   else if( *arg1 == *arg2 ) return 0;
   else return 1;
 }              

int main()
{
  int N;
  int T;
  int NA;
  int NB;
  
  int tps;
  char tmp[2];
  
  char poub;
    
  string str;
  
  cin>>N;
  int tDA;
  int tDB;
  int tPA;
  int tPB;
  
  for(int i=0; i<N; i++)
  {
  
    tDA = 0;
    tDB = 0;
    tPA = 0;
    tPB = 0;
    
    cin>>T;
    cin>>NA;
    cin>>NB;
    
    int heureDA[NA];
    int heureDB[NB];
    int heureAA[NB];
    int heureAB[NA];
    
    int cptDA;
    int cptDB;
    int cptAA;
    int cptAB;
    
    getline(cin,str);
    for(int j=0; j<NA; j++)
    {
      cin.get(tmp,3,':');
      tps=60*atoi(tmp);
      cin.get();
      cin.get(tmp,3,':');
      tps+=atoi(tmp);
      heureDA[j]=tps;
      
      cin.get();
      cin.get(tmp,3,':');
      tps=60*atoi(tmp);
      cin.get();
      cin.get(tmp,3,':');
      tps+=atoi(tmp)+T;
      getline(cin,str);
      heureAB[j]=tps;
      
    }
    
    qsort(heureDA,NA,sizeof(int),compare_ints);
    qsort(heureAB,NA,sizeof(int),compare_ints);
    
    for(int j=0; j<NB; j++)
    {
      cin.get(tmp,3,':');
      tps=60*atoi(tmp);
      cin.get();
      cin.get(tmp,3,':');
      tps+=atoi(tmp);
      heureDB[j]=tps;
      
      cin.get();
      cin.get(tmp,3,':');
      tps=60*atoi(tmp);
      cin.get();
      cin.get(tmp,3,':');
      tps+=atoi(tmp)+T;
      heureAA[j]=tps;
      getline(cin,str);
    }
    
    qsort(heureDB,NB,sizeof(int),compare_ints);
    qsort(heureAA,NB,sizeof(int),compare_ints);
    
    cptDA=0;
    cptDB=0;
    cptAA=0;
    cptAB=0;
    for(int j=0; j<24*60; j++)
    {    
      while(cptAA<NB && heureAA[cptAA]==j)
      {
        tDA++;
        cptAA++;
      }
      while(cptAB<NA && heureAB[cptAB]==j)
      {
        tDB++;
        cptAB++;
      }
      while(cptDA<NA && heureDA[cptDA]==j)
      {
        cptDA++;
        if(tDA<1)
          tPA++;
        else
          tDA--;
      }
      while(cptDB<NB && heureDB[cptDB]==j)
      {
        cptDB++;
        if(tDB<1)
          tPB++;
        else
          tDB--;
      }
    }
    
    printf("Case #%d: %d %d\n",i+1,tPA,tPB);
  }

  return 0;
}
