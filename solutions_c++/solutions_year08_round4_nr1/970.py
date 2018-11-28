#include <iostream>
#include <fstream>
#define MAXN 10005
#define IMP 100000

using namespace std;

bool isAnd[MAXN], isChange[MAXN];
long long int value[MAXN][2];

int MIN(int a, int b){
  return a<b? a: b;
}
int MIN(int a, int b, int c){
  return MIN(MIN(a,b),c);
}

int main(int argc, char* argv[]){
  ifstream fin (argv[1]);
  ofstream fout (argv[2]);
 
  int testcase=0;
  fin>>testcase;
  //cout<<testcase<<endl;
  int V,M;
  int G,C,L;
  int AND[2],OR[2];
  for(int test=1;test<=testcase;test++){
    fin>>M>>V;
    for(int i=1;i<=(M-1)/2;i++){
      fin>>G>>C;
      isAnd[i]=(G==1);
      isChange[i]=(C==1);
    }
    for(int i=(M+1)/2;i<=M;i++){
      fin>>L;
      value[i][L]=0;
      value[i][1-L]=IMP;
    }
    for(int i=(M-1)/2;i>0;i--){
      OR[1]=MIN(value[2*i][1]+value[2*i+1][0],
		value[2*i][1]+value[2*i+1][1],
		value[2*i][0]+value[2*i+1][1]);
      OR[0]=value[2*i][0]+value[2*i+1][0];
      AND[0]=MIN(value[2*i][1]+value[2*i+1][0],
		 value[2*i][0]+value[2*i+1][1],
		 value[2*i][0]+value[2*i+1][0]);
      AND[1]=value[2*i][1]+value[2*i+1][1];
      if(isAnd[i]){
	value[i][0]=AND[0];
	value[i][1]=AND[1];
      }
      else{
	value[i][0]=OR[0];
	value[i][1]=OR[1];
      }
      if(isChange[i]){
	if(isAnd[i]){
	  value[i][0]=MIN(AND[0],OR[0]+1);
	  value[i][1]=MIN(AND[1],OR[1]+1);
	}
	else{
	  value[i][0]=MIN(AND[0]+1,OR[0]);
	  value[i][1]=MIN(AND[1]+1,OR[1]);
	}
      }

      
    }

    //  for(int i=1;i<=M;i++)
    //cout<<"Value "<<i<<" True:"<<value[i][1]<<" False: "<<value[i][0]<<endl;


    if(value[1][V]>=IMP)
      fout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<endl;
    else
      fout<<"Case #"<<test<<": "<<value[1][V]<<endl;

  }
  return 0;
}
