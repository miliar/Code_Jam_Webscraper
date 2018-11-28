#include <iostream>
#include <fstream>

using namespace std;

int abs(int a){
    return (a>0)?(a):(a*(-1));
}

int main(){
    
    ifstream sisf("A-large.in");
    ofstream valf("A-large.out");
    
    int T;
    sisf >> T;
    
    for(int t = 1; t<=T; t++){
       int N;
       char temp;
       int a;
       int V=0;
       int ot=0, bt=0;
       int op=1, bp=1;
       sisf >> N;
       for(int i = 1; i<=N; i++){
          sisf.get(temp);
          sisf.get(temp);
          if(temp=='O'){
             sisf >> a;
             if(ot>=abs(a-op)+1){
                //ot=ot-abs(a-op)-1;
                ot=0;
                V++;
                bt++;
                op=a;
             }
             else if(ot<abs(a-op)+1){
                V+=abs(a-op)+1-ot;
                bt+=abs(a-op)+1-ot;
                ot=0;
                op=a;
             } 
          }
          else if(temp=='B'){
             sisf >> a;
             if(bt>=abs(a-bp)+1){
                //bt=bt-abs(a-bp)-1;
                bt=0;
                V++;
                ot++;
                bp=a;
             }
             else if(bt<abs(a-bp)+1){
                V+=abs(a-bp)+1-bt;
                ot+=abs(a-bp)+1-bt;
                bt=0;
                bp=a;
             }
          }
       }
    valf << "Case #" << t << ": "<< V << endl;
    }
    
    
    return 0;
}
