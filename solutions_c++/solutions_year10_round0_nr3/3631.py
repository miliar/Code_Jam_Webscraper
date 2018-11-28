#include <iostream>

using namespace std;

class Queue{
  int ini,size;
  long int v[1000];

  public:
    Queue():
      ini(0),
      size(0)
    {}
    void put(long int n){
      v[size++] = n;
    }
    long int getNext(){
      if(ini==size)
        ini=0;
      return v[ini++];
    }
    long int examineNext(){
      if(ini==size)
        ini=0;
      return v[ini];
    }
    void reset(){
        ini = size = 0;
    }
    int getIni(){
      if(ini==size)
        ini=0;
      return ini;
    }

};

long int solveCase(FILE *file){
  long int k,R,aux,money=0,run=0;
  int N,i,startGroup;
  Queue q;

  fscanf(file, "%ld %ld %d",&R,&k,&N);
  for(i=0;i<N;++i){
    fscanf(file,"%ld", &aux);
    q.put(aux);
  }

  for(;R;--R){
    startGroup = q.getIni();
    run=0;
    while(run+q.examineNext()<=k){
      run += q.getNext();
      if(startGroup == q.getIni())
        break;
    }

    money+=run;
  }
  return money;
}

int main(int argc,char **argv)
{
  FILE *file    = fopen(argv[1],"rt");
  FILE *fileOut = fopen("test.out","wt");

  if(!file){
    cout<<"file missing";
    return 0;
  }

  int nCases,i;
  fscanf(file,"%d",&nCases);

  for(i=0;i<nCases;++i){
    fprintf(fileOut,"Case #%d:",i+1);
    fprintf(fileOut," %ld",solveCase(file));

    if(i+1!=nCases)
      fprintf(fileOut,"\n");
  }
  fclose(fileOut);
  fclose(file);

  return 0;
}
