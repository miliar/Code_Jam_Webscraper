#include<string>
#include<iostream>
using namespace std;

int T,N,temp,wrong;

int main(){
  cin >> T;
  for(int t=1;t<=T;t++){
    cin >> N;
    wrong = 0;
    for(int n=1;n<=N;n++){
      cin >> temp;
      if( temp != n ){
	wrong++;
      }
    }
    cout << "Case #" << t << ": " << wrong << ".000000" << endl;
  }
}
