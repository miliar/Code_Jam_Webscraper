#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#define  f(x,y,i) for(int i=x;i<y;i++)
#define in(n,up) find(up,up+sizeof(up)/4,(n))-&up[0]!=sizeof(up)/4 
using namespace std;

int cuantos(string frase,string line){
    int a=0;
    if(frase.size()==0) return 1;
    if(frase.size()>line.size() ) return 0;
    if(frase.size()==1){
        f(0,line.size(),i)if(line[i]==frase[0]) a++;
        return a;
    }
    int corte=frase.size()/2;
    string aux=""; aux+=frase[corte];
    f(0,line.size(),i){
        if(line[i]==frase[corte]){
            string f1(frase,0,corte);
            string f2(frase,corte+1);
            string l1(line,0,i);
            string l2(line,i+1);
            a=(a+cuantos(f1,l1)*cuantos(f2,l2))%10000;
        }
    }
    return a;
}
        
int main()
{
    freopen("C.small.in.txt","r",stdin);
    freopen("C.small.out.txt","w",stdout);
    char cad[501];
    string line;
    int N; cin>>N;
    cin.get();
    f(0,N,i){
        cin.getline(cad,501);
        line=cad;
        printf("Case #%d: %04d\n",i+1,cuantos("welcome to code jam",line));
    }
}
