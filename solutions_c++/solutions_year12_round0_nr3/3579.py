#include<fstream>
using namespace std;

bool pares(int k, int j);

int main(){
    int T, i, a, b, k, j, cont;
    
    fstream leer, escribir;
    
    leer.open("recycled.in", ios::in);
    escribir.open("recycled.out", ios::out);
    
    leer>>T;
    for(i=1;i<=T;i++){
        leer>>a>>b;
        cont=0;
        for(k=a;k<b;k++)
            for(j=k+1;j<=b;j++)
                if(pares(k, j))
                    cont++;
        escribir<<"Case #"<<i<<": "<<cont<<endl;
    }
    leer.close();
    escribir.close();
}

bool pares(int k, int j){
    int temp=k, dig=0, i, l, ld=k;
    while(temp>0){
        dig++;
        temp/=10;
    }
    
    for(i=0;i<dig;i++){
        temp = k%10;
        k/=10;
        for(l=1;l<dig;l++)
            temp*=10;
        k+=temp;
        if(k==j){
            return true;
        }
    }
    
    return false;
}
