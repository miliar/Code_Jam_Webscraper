#include<fstream>
#include<queue>
using namespace std;
int main(){
    ifstream in("C-small.in");
    ofstream out("C-small.out");
    int t;
    in>>t;
    for(int z=0;z<t;z++){
            int r,k,n;
            long long aux,total,plata=0;
            in>>r;
            in>>k;
            in>>n;
            queue<long long> fila;
            queue<long long> subidos;
            for(int x=0;x<n;x++){
                    in>>aux;
                    fila.push(aux);
            }
            for(int y=0;y<r;y++){
                    total=0;
                    while(!(fila.empty())){
                                                    aux=fila.front();
                                                    if(aux<=k-total){
                                                                     fila.pop();
                                                                     total+=aux;
                                                                     subidos.push(aux);
                                                                     plata+=aux;
                                                    }else{
                                                          break;
                                                    }
                                                    
                    }
                    while(!subidos.empty()){
                                            fila.push(subidos.front());
                                            subidos.pop();
                    }
            }
            out<<"Case #"<<z+1<<": "<<plata<<endl;
    }
}
