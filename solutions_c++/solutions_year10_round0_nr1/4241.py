#include<fstream>
#include<math.h>
#include<iostream>
using namespace std;
struct snapper{
       bool prendido;
       bool energia;
       bool energiaf;
};
int main(){
    int t,n,k;
    ifstream in("A-small.in");
    ofstream out("A-small.out");
    in>>t;
    for(int z=0;z<t;z++){
            in>>n;
            in>>k;
            //cout<<n<<" "<<k<<endl;
            /*if((k-1)%(int)(pow(2,n)-1)==0||k==(int)(pow(2,n)-1)){
                              out<<"Case #"<<z+1<<": ON"<<endl;
            }else{
                  out<<"Case #"<<z+1<<": OFF"<<endl;
            }*/
            snapper cable[n+1];
            for(int x=0;x<=n;x++){
                    cable[x].prendido=false;
                    cable[x].energia=false;
            }
            cable[0].energia=true;
            cable[0].prendido=false;
            /*for(int x=1;x<=n;x++){
                    cout<<"pepe"<<endl;
                    cout<<cable[x].energia<<" "<<cable[x].prendido<<endl;
            }
            system("pause");*/
            for(int y=0;y<k;y++){
                    for(int x=1;x<=n;x++){
                            if(cable[x-1].energia*!(cable[x-1].prendido)){
                                                 cable[x].energia=true;
                                                 cable[x].prendido=!(cable[x].prendido);
                            }else{
                                  break;
                            }
                    }
                    //cout<<y<<endl;
            /*for(int x=1;x<=n;x++){
                    cout<<"pepe2"<<endl;
                    cout<<x<<" "<<cable[x].energia<<" "<<cable[x].prendido<<endl;
            }
            system("pause");*/
            }
            /*for(int x=1;x<=n;x++){
                    cout<<"pepe2"<<endl;
                    cout<<x<<" "<<cable[x].energia<<" "<<cable[x].prendido<<endl;
            }
            system("pause");*/
            int pepe=0;
            for(int x=1;x<=n;x++){
                    if(cable[x].energia&&cable[x].prendido){
                                                            pepe++;
                    }
            }
            if(pepe==n){
                        out<<"Case #"<<z+1<<": ON"<<endl;                        
            }else{
                  out<<"Case #"<<z+1<<": OFF"<<endl;
            }
    }
    //system("pause");
}
