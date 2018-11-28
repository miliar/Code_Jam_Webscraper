#include<cstdio>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int t,n;
int c,d;
char pepe;
string com;
string op;
string lista;
int main(){
    ifstream entra("magicoin.txt");
    ofstream sale("magicoout.txt");
    entra>>t;
    for (int i=1;i<=t;i++){
        lista.clear();
        entra>>c;
        if (c==1) entra>>com;
        entra>>d;
        if (d==1) entra>>op;
        entra>>n;
        for (int j=0;j<n;j++){
            entra>>pepe;
            lista.push_back(pepe);
            int tam=lista.size();
            if(c==1&&(tam>1)){
                if((com[0]==lista[tam-2] && com[1]==lista[tam-1])||(com[0]==lista[tam-1] && com[1]==lista[tam-2])){
                    lista.resize(tam-2);
                    lista.push_back(com[2]);}}
            tam=lista.size();
            if(d==1&&(tam>1)){
                if(op[0]==lista[tam-1]){
                    for (int k=0;k<tam-1;k++){
                        if(lista[k]==op[1]){
                            lista.clear();
                            break;}}}
                if(op[1]==lista[tam-1]){
                    for (int k=0;k<tam-1;k++){
                        if(lista[k]==op[0]){
                            lista.clear();
                            break;}}}}}
        int tfin=lista.size();
        sale<<"Case #"<<i<<": [";
        for (int q=0;q<tfin;q++){
            sale<<lista[q];
            if (q!=(tfin-1)) sale<<", ";}
        sale<<"]"<<endl;}}
