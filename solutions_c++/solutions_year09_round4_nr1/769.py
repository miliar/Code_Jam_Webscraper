#include<iostream>
#define TAM 55
using namespace std;


int resol(int v[],int nivel,int N){
  if(N==1) return 0;
  for(int i=0;i<N;i++){
    if(v[i] <=nivel){
      int val=v[i];
      for(int j=i-1;j>=0;j--){
	v[j+1]=v[j];
      }
      v[0]=val;
      return i+resol(v+1,nivel+1,N-1);
    }
  }
  return 123123123;
}
int main(){
  int T;
  cin >> T;
  for(int caso=1;caso<=T;caso++){
    int N;
    char tab[TAM][TAM+1];
    cin >>N;
    for(int lin=0;lin<N;lin++){
      scanf(" %s ",tab[lin]);
    }
    int pode[TAM];
    for(int lin=0;lin<N;lin++){
      int max=0;
      for(int col=0;col<N;col++){
	if(tab[lin][col] == '1'){
	  max = col;
	}
      }
      pode[lin]=max;
    }
    int res = resol(pode,0,N);
    cout << "Case #"<< caso << ": " << res << endl;
  }
  
}
