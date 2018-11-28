#include<fstream>
#include<queue>
#include<iostream>
using namespace std;
int main(){
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in>>t;
    for(int i=0;i<t;i++){
            int n;
            int cant=0;
            in>>n;
            int orpos=1;
            int blpos=1;
            queue<int> ormo;
            queue<int> blmo;
            queue<bool> moves;
            char aux;
            int auxb;
            for(int x=0;x<n;x++){
                    in>>aux;
                    in>>auxb;
                    if(aux=='O'){
                                 ormo.push(auxb);
                                 moves.push(true);
                    }else{
                          blmo.push(auxb);
                          moves.push(false);
                    }
            }
            while(!moves.empty()){
                                  bool banco=false;
                                                if(blmo.front()==blpos){
                                                                        if(!moves.front()){
                                                                                           blmo.pop();
                                                                                           moves.pop();
                                                                                           cout<<"apreto azul"<<endl;
                                                                                           banco=true;
                                                                        }
                                                }else{
                                                      if(blpos>blmo.front()){
                                                                             blpos--;
                                                                             cout<<"atras azul"<<endl;
                                                      }else{
                                                            blpos++;
                                                            cout<<"adelante azul"<<endl;
                                                      }
                                                }
                                                if(ormo.front()==orpos){
                                                                        if(moves.front()&&!banco){
                                                                                           ormo.pop();
                                                                                           moves.pop();
                                                                                           cout<<"apreto naranja"<<endl;
                                                                                           
                                                                        }
                                                }else{
                                                      if(orpos>ormo.front()){
                                                                             orpos--;
                                                                             cout<<"atras naranja"<<endl;
                                                      }else{
                                                            orpos++;
                                                            cout<<"adelante naranja"<<endl;
                                                      }
                                                }
                                                cant++;
            }
            out<<"Case #"<<(i+1)<<": "<<cant<<endl;
            //system("pause");
    }
}
