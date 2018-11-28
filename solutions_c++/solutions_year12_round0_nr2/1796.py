#include<iostream>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int cas=1;cas<=T;++cas){
    int N,S,p;
    int res=0;
    cin >> N >> S >> p;
    for(int i=0;i<N;++i){
      int tmp;
      cin >> tmp;
      if(tmp>=p+2*(max(p-1,0)))
	res++;
      else if(S>0 && tmp>=p+2*max(p-2,0)){
	res++;
	S--;
      }

    }
    
    cout << "Case #" << cas << ": " << res << endl;
    
  }
}
