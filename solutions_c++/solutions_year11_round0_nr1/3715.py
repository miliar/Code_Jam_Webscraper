#include <iostream>
#include <cstdlib>

using namespace std;
int main(){
  int T;
  cin >> T;
  for(int cases=1;cases<=T;++cases){
    int res=0;
    int N;
    cin >> N;
    char R[N];
    int P[N];
    for(int i=0;i<N;++i){
      cin >> R[i] >> P[i];
    }
    char C = R[0];
    int delay=0;
    int time=0;
    int timeo=0;
    int timeb=0;
    int o=1;
    int b=1;
    for(int i=0;i<N;++i){
      
      if(R[i]==C){
        if(C=='O'){
          time = abs(o-P[i]);
          time += 1;
          timeo += time;
          delay += time;
          o=P[i];
        }
        else{
          time = abs(b-P[i]);
          time += 1;
          timeb += time;
          delay += time;
          b=P[i];
        }
      }
      else {
        C = R[i];
        if(C=='O'){
          time = max(delay,abs(o-P[i]));
          time +=1;
          timeo += time;
          delay = timeo-timeb;
          o=P[i];
        }
        else{
          time = max(delay,abs(b-P[i]));
          time +=1;
          timeb += time;
          delay = timeb-timeo;
          b=P[i];
        }
      }
    }
      res= max (timeo,timeb);
    
    cout << "Case #"<<cases<<": "<<res << endl;
  }
  
  return 0;
}