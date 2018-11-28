#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>


using namespace std;
char b[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k'
		,'r','z','t','n','w','j','p','f','m','a','q'};
	
int main(){
    
    
    ifstream in("a.in");
    ofstream out("a.out");
    int N;
    
    in >> N;
    char s[256];
    in.getline(s,256);
    for(int i =0;i<N;i++){
            in.getline(s,256);
            for(int j = 0;s[j]!='\0';j++){
               if ( s[j] >= 'a' && s[j]<='z' )     
                s[j] = b[s[j]-'a'];
            }
            out <<"Case #"<<(i+1)<<": "<<s<<endl;
    }
}
