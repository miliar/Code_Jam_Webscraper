#include <iostream>
#include <cstring>

using namespace std;

int valor[1000];
int maxbit;
int N;

void maxibit(){
  int c;
  for(int j=19; j>=0; j--)
    for(int i=0; i<N; i++)
      if(valor[i]>>j){ maxbit=j; return;}
}

int suma(){
  int a=valor[0];
  for(int i=1; i<N; i++)
    a^=valor[i];
  return a;
}

int main(int argc, char *argv[]){
  int T, min;
  unsigned long sum;

  cin >> T;
  for(int x=1; x<=T; x++){
    cin >> N;
    for(int i=0; i<N; i++) cin >> valor[i];

    cout << "Case #" << x << ": ";
    if(suma()) cout << "NO\n";
    else {
      sum=0;
      min=1000001;
      for(int i=0; i<N; i++){
	if(valor[i]<min)
	  min=valor[i];
	sum+=valor[i];
      }
      cout << (sum-min) << endl;
    }
  }

  return 0;
}
