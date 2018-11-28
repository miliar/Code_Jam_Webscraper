#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    int t,i,j;
    string s,w;
    ofstream istr;
    istr.open("demo.txt");
    w="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d\n",&t);
    for(i=1;i<=t;i++){
        getline(cin,s);
        istr<<"Case #"<<i<<": ";
        for(j=0;j<s.length();j++){
             if(s[j]!=' ')
                        istr<<w[s[j]-'a'];
             else istr<<" ";                     
        }
        if(i!=t)
        istr<<"\n";
    }
    istr.close();
    return 0;
}
