#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;
int main(){
        
        int t;
        int cont=1;
        string cad;
        string alpha="yhesocvxduiglbkrztnwjpfmaq";
        scanf("%d\n", &t);
        while(t--){
                string sal="";
                getline(cin, cad);
                for( int i=0;i<cad.length();i++ ){
                        if( cad[i]>='a' && cad[i]<='z')
                                sal+=alpha[ cad[i]-'a' ];
                        else sal+=cad[i];
                }
                cout<<"Case #"<<cont++<<": "<<sal<<endl;
        }
 
        return 0;
}