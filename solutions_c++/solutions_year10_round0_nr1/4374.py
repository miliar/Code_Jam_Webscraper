#include <iostream>

using namespace std;
enum state{off,on};

bool testON(int N, long int K){
  state snapper[30];

  int i;
  for(i=0;i<N;++i)
    snapper[i] = off;


  long int li;
  bool alimentado;

  for(li=0;li<K;++li){

    alimentado = true;
    i=0;

    while(alimentado&&i<N){
      if(snapper[i] == off){
        alimentado = false;
        snapper[i] = on;
      }
      else{
        snapper[i] = off;
        ++i;
      }
    }
  }

  i=0;
  while(i<N)
    if(snapper[i++] == off)
      return false;

  return true;
}

int main(int argc,char **argv)
{
  FILE *file    = fopen(argv[1],"rt");
  FILE *fileOut = fopen("teste.out","wt");

  if(!file){
    cout<<"file missing";
    return 0;
  }

  int nCases,i;
  int N;
  long int K;
  fscanf(file,"%d",&nCases);

  for(i=0;i<nCases;++i){
    cout<<"case "<<i+1<<endl;
    fprintf(fileOut,"Case #%d:",i+1);

    fscanf(file,"%d %ld",&N, &K);
    if(testON(N,K))
      fprintf(fileOut," ON");
    else
      fprintf(fileOut," OFF");


    if(i+1!=nCases)
      fprintf(fileOut,"\n");
  }
  fclose(fileOut);
  fclose(file);

  return 0;
}
