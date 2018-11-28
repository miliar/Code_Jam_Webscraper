#include <iostream>
#include <string>
#include "stdio.h"
using namespace std;

char code[28]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char ans[28]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int findchar(char c){
    for (int i=0;i<28;i++) if(code[i]==c) return i;

}

int main(){

    int inp=0;
    string res="";
    string txt="";
    scanf("%d\n",&inp);
    for (int i=0;i<inp;i++){
        res="";
        getline(cin,txt);

            for(int j=0;j<txt.length();j++){
                if (txt[j]==' ') res+=" ";
                else res+=ans[findchar(txt[j])];
            }

        cout << "Case #" << i+1 << ": "<< res;
        if (i<inp-1) cout << endl;
    }


    return 0;
}
