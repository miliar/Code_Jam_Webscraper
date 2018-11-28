#include<iostream>

using namespace std;

class Snapper{
public:
  bool state, sendPower, nextPower;
  Snapper(){
    state = false;
    sendPower = false;
    nextPower = false;
  }
  void toggle(bool flag, bool flag2){
    if(flag){
      state = !state;
      nextPower = (state && flag2);
    }
    else {
      nextPower = (state && flag2);
    }
    return;
  }
  void next(void){
    sendPower = nextPower;
  }
};

int main(){
  int T;

  cin >> T;
 
  for(int i=0; i<T; i++){
    
    int N, K;
    
    cin >> N >> K;
    
    Snapper s[N+1];
    
    s[0].state = true;
    s[0].sendPower = true;
    s[0].nextPower = true;
    
    for(int j=0; j<K; j++){
      for(int k=1; k<=N+1; k++){  

	if(k != N+1){
	  s[k].toggle(s[k-1].sendPower, s[k-1].nextPower); 
	}
	s[k-1].next();
	
      }    
    }
    
    cout << "Case #" << i+1 <<": ";
    if(s[N].nextPower){
      cout << "ON" << endl;
    }
    else {
      cout << "OFF" << endl;
    }    
  }
}
