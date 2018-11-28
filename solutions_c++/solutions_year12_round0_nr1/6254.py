#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

string translate (string s1,char c[]){

    string s2;
    for (int i=0;i<s1.size();i++){
        if (s1[i]!=' ' && s1[i]!='\0'){
            s2+=c[s1[i]-'a'];
        }
        else if (s1[i]==' '){
            s2+=' ';
        }
        else if (s1[i]=='\0')
            s2[i]+='\0';

    }
    return s2;
}

int main()
{
    ifstream input("A-small-attempt0.in");
    string * ins;
    int size;
    string unused;
    input>>size;
    getline(input,unused);
    ins=new string[size];

    for (int i=0;i<size;i++){
        getline(input,ins[i]);
    }
    char c[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n'
    ,'w','j','p','f','m','a','q'};

    ofstream output("out.txt");

   for (int i=0;i<size;i++){
       output<<"Case #"<<i+1<<": "<<translate(ins[i],c)<<endl;
   }




    return 0;
}
