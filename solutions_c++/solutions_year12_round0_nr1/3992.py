#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <cstring>

using namespace std;

int main(){
    
    int n=1;
    char mapping[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int T;
    cin>>T;
    cin.ignore();
    
    while(T--){
        char s[101];
        memset(s,'\0',sizeof s);        
        cin.getline(s,101);
        string str(s);
        
        
        int sz=str.size();
        for(int i=0;i<sz;i++){
            if(str[i]==' ') str[i]=' ';    
            else str[i] = mapping[ str[i]-'a'];
        }        
        cout<<"Case #"<<n<<": "<<str<<endl;
        n++;
    }
    
    return 0;
}
