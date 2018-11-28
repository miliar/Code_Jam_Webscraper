#include <iostream>
#include <cstdio>
using namespace std;
int main(){
    freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
    
    int t,n;
    string cad;
    cin>>t;
    getchar();
    for (int k=1; k<=t; k++){
        getline(cin,cad);
        n = cad.size();
        
        cout<<"Case #"<<k<<": ";        
        for (int i=0; i<n; i++){
            switch (cad[i]){
                   case 'y': cout<<"a";break;
                   case 'n': cout<<"b";break;
                   case 'f': cout<<"c";break;
                   case 'i': cout<<"d";break;
                   case 'c': cout<<"e";break;
                   case 'w': cout<<"f";break;
                   case 'l': cout<<"g";break;
                   case 'b': cout<<"h";break;
                   case 'k': cout<<"i";break;
                   case 'u': cout<<"j";break;
                   case 'o': cout<<"k";break;
                   case 'm': cout<<"l";break;
                   case 'x': cout<<"m";break;
                   case 's': cout<<"n";break;
                   case 'e': cout<<"o";break;
                   case 'v': cout<<"p";break;
                   case 'z': cout<<"q";break;
                   case 'p': cout<<"r";break;
                   case 'd': cout<<"s";break;
                   case 'r': cout<<"t";break;
                   case 'j': cout<<"u";break;
                   case 'g': cout<<"v";break;
                   case 't': cout<<"w";break;
                   case 'h': cout<<"x";break;
                   case 'a': cout<<"y";break;
                   case 'q': cout<<"z";break;
                   default : cout<<" ";
                   }
            
            }
        cout<<endl;
        }
    return 0;
}
