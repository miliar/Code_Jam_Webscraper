#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

#define ON true
#define OFF false

class Snapper{
  
  Snapper *socket;
  static vector<Snapper > snappers;
  bool power;
  public:
    bool state;

    Snapper(){
      state = OFF;
      socket = NULL;
    }
    
    bool hasPower(){          
      return power;
    }
    
    void updatePower(){
      if(socket==NULL){
        power = true;
      }else{
        socket->updatePower();
        power = socket->state == ON && socket->power; 
      }       
    }
    
    void toogle(){
      if(hasPower()){
        state = !state;
      }      
     if(socket!=NULL){
        socket->toogle();
      }
    }
    
    Snapper connectTo(Snapper *_socket){
      socket = _socket;
    }
    
    string isPowerUp(){
      return this->state&&this->hasPower()?"ON":"OFF";
    }
    
  
};

int main(){    
  
  int C, N, K;  
  Snapper *last = NULL , *s;
  
  ifstream cin("A-small-attempt0.in");
  ofstream cout("A-small-attempt0.out");
  
  cin>> C;
  
  /*last = new Snapper();
  cout<<last->isPowerUp()<<endl;
  last->toogle();
  cout<<last->isPowerUp()<<endl;
  

  system("pause"); */
  for(int i=0;i<C;i++){
    cin>>N;
    cin>>K;
    last = NULL;
    for(int j=0;j<N;j++){
      s = new Snapper();
      if(last != NULL){
        s->connectTo(last);
      }
      last = s;
    }
    
    for(int j=0;j<K;j++){
      last->updatePower();
      last->toogle();
    }
    last->updatePower();
    cout<<"Case #"<<i+1<<": "<<last->isPowerUp()<<endl;
 
  }
  
  //system("pause");
}

