//#include <string>
//#include <cstdio>
//#include <cstdlib>
//#include <cstring>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
//#include <sstream>


using namespace std;

//CONVERT STRING TO INT: atoi(STRING.c_str())
//    getline(input,temp,'\n');
//    casos=atoi(temp.c_str());

void mostrarStr(string a[],int b, string nombre);
int aclarar(string dicc[],int palDicc,string patt, int longitud);
bool pertenece(string x[],int n, string s);
void setearStr(string a[],int b);
bool pertenece2(string x, char c);

int main(){
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("A-large.out");
    int palDicc=0;
    int longitud=0;
    int casos=0;
    string temp;
    int pos=0;

    getline(input,temp,' ');
    longitud=atoi(temp.c_str());
    cout << longitud << endl;

    getline(input,temp,' ');
    palDicc=atoi(temp.c_str());
    cout << palDicc << endl;

    getline(input,temp);
    casos=atoi(temp.c_str());
    cout << casos << endl;

    string dicc[palDicc];

    for(int i=0;i<palDicc;i++){
        getline(input,dicc[i]);
    }

mostrarStr(dicc,palDicc,"dic");
    string patterns[casos];

    for(int i=0;i<casos;i++){
        getline(input,patterns[i]);
    }



mostrarStr(patterns,casos,"patterns");

    for(int i=0;i<casos;i++){
        pos=aclarar(dicc,palDicc,patterns[i],longitud);
        cout << "Case #" << (i+1) << ": " << pos << endl;
        output << "Case #" << (i+1) << ": " << pos << endl;
    }

    input.close();
    output.close();
	return 0;
}

int aclarar(string dicc[],int palDicc,string patt, int longitud){
    int res=0;
    int i=0;
    int j=0;
    bool ext=false;

    string palabra[longitud];

    while(i<patt.length()){
        if(patt[i]=='(') ext=true;
        else if(patt[i]==')'){
            ext=false;
            j++;
        }

        if(ext){
            if(patt[i]!='(') palabra[j].append(patt,i,1);
        }
        else{
            if(patt[i]!=')'){
                palabra[j].append(patt,i,1);
                j++;
            }
        }

        i++;
    }
    mostrarStr(palabra,longitud,"Posibilidades");

    i=0;
    j=0;
    bool esposible=true;
    while(i<palDicc){
        while(j<longitud && esposible){
            if(!(pertenece2(palabra[j],dicc[i][j]))) esposible=false;
            j++;
        }
        if(esposible) res++;
        j=0;
        esposible=true;
        i++;
    }

    return res;
}


bool pertenece(string x[],int n, string s){
    int i=0;
    bool res=false;
    while(i<n){
        if(x[i]==s) res=true;
        i++;
    }
    return res;
}

bool pertenece2(string x, char c){
    int i=0;
    bool res=false;
    while(i<x.length()){
        if(x[i]==c) res=true;
        i++;
    }
    return res;
}

void setearStr(string a[],int b){
    int i=0;
    while(i<b){
        a[i]="";
        i++;
    }
}



void mostrarStr(string a[],int b, string nombre){
    int i=0;
    cout << endl << endl << "Array " << nombre << ":" << endl;
    while(i<b){
        if(a[i]!="")
        cout << "Elemento " << i << ": " << a[i] << endl;
        i++;
    }
    cout << endl << endl;
}
