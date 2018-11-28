#include <cstdio>
#include <string>
#include <map>
#include <vector>
using namespace std;

int main(){
    string a1 = "our language is impossible to understand";
    string a2 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";

    string b1 = "there are twenty six factorial possibilities";
    string b2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";

    string c1 = "so it is okay if you want to just give upzq";
    string c2 = "de kr kd eoya kw aej tysr re ujdr lkgc jvqz";


    vector<string> Arr;
    map<char,char> dicc;

    Arr.push_back(a1);
    Arr.push_back(a2);
    Arr.push_back(b1);
    Arr.push_back(b2);
    Arr.push_back(c1);
    Arr.push_back(c2);

    for(int i = 0 ; i < 3*2; i+=2){
        for(int pos = 0; pos < Arr[i].size(); pos++)
            dicc[Arr[i+1][pos]] = Arr[i][pos];
    }

    //for(int c = 'a'; c <= 'z'; c++)
       //printf("%c - > %c\n",c,dicc[c]);

    int cases;
    char buffer[128];

    gets(buffer);
    sscanf(buffer,"%d",&cases);

    for(int i = 1; i <= cases; i++){
        printf("Case #%d: ",i);

        gets(buffer);
        for(int pos = 0; buffer[pos]!='\0';pos++)
            printf("%c", dicc[buffer[pos]]);

        printf("\n");
    }

    return 0;
}
