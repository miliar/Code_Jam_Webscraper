#include<cstdio>
#include<fstream>
#include<vector>
#include<string>
#include<bitset>
#include<iostream>
using namespace std;
int t,n,j;
vector<int> lista;
bool sepuede(vector<int>x){
    int tamanio=x.size();
    if (tamanio<2) return 0;
    long long respuesta=x[0];
    for (int y=1;y<tamanio;y++) {
        respuesta ^= x[y];}
    if (respuesta==0) return 1;
    return 0;}
int main(){
    ifstream entra("carin.txt");
    ofstream sale("carout.txt");
    entra>>t;
    for (int k=1;k<=t;k++){
        entra>>n;
        lista.clear();
        for (int i=0;i<n;i++){
            entra>>j;
            lista.push_back(j);}
        if (sepuede(lista)==0) sale<<"Case #"<<k<<": NO"<<endl;
        else{
            sort (lista.begin(),lista.end());
        long long contador=0;
        for (int i=1;i<n;i++) contador+=lista[i];
        sale<<"Case #"<<k<<": "<<contador<<endl;}}}
