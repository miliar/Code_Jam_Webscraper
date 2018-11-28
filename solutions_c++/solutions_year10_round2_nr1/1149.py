#include <iostream>
#include <string.h>
#include <vector>
#include <sstream>

using namespace std;

class directorio
{
    string nombre;
    vector <directorio> ls;
public:
    directorio(string n){
        nombre = n;
    }
    string getNombre(){
        return nombre;
    }
    void agregar(directorio *d){
        ls.push_back(*d);
    }
    directorio* esta(string n){
        for (int i=0; i<ls.size(); i++){
            if (n.compare(ls[i].getNombre())==0){
                return &ls[i];
            }
        }
        return NULL;
    }
};

int main(){
    int nc;
    cin>>nc;
    for (int i=1; i<=nc; i++){
        int resp,N,M;
        string line;
        //Codigo del problema
        cin>>N>>M;
           getline( cin, line );
        directorio d("root");
        for (int j=0; j<N; j++){
            string s;
            char c;

            getline(cin,line);
            istringstream iss(line);
            iss>>c;
            directorio *diract = &d;
            while (!iss.eof()){
                iss>>c;
                if (c=='\n' || c=='\0') break;                                
                if (iss.eof()) break;
                if (c=='/'){
                    if (diract->esta(s)!=NULL){
                        diract = diract->esta(s);
                        
                    }
                    else {
                        diract->agregar(new directorio(s));
                        diract = diract->esta(s);
                        resp++;
                    }
                }

                if (c=='/') {
                    s="";
                    continue;
                }
                s = s+c;
                
            }
            
            if (diract->esta(s) != NULL){
                diract = diract->esta(s);
            }
            else {
                diract->agregar(new directorio(s));
                resp++;
            }
            //cout<<resp<<endl;
        }
        
        int r = 0;
        for (int j=0; j<M; j++){
            string s;
            char c;

            getline(cin,line);
            istringstream iss(line);
            iss>>c;
            directorio *diract = &d;
            while (!iss.eof()){
                iss>>c;
                if (c=='\n' || c=='\0') break;                                
                if (iss.eof()) break;
                if (c=='/'){
                    if (diract->esta(s)!=NULL){
                        diract = diract->esta(s);
                    }
                    else {
                        diract->agregar(new directorio(s));
                        diract = diract->esta(s);
                        //cout<<"agregado "<<s<<endl;
                        r++;
                    }
                }
                if (c=='/') {
                    s="";
                    continue;
                }

                s = s+c;
            }
            if (diract->esta(s) != NULL){
                diract = diract->esta(s);
            }
            else {
                diract->agregar(new directorio(s));
                //cout<<"agregado "<<s<<endl;
                r++;
            }
            //cout<<r<<endl;
        }
        
        cout<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}
