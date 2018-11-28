#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<string>
using namespace std;


int main(int argc, char *argv[]){
    map<char, char> dictionary;

    string o1("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
    string d1("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");

    for(size_t i=0;i<o1.size();++i){
        dictionary[o1[i]] = d1[i];
    }
    dictionary['q'] = 'z';
    dictionary['z'] = 'q';
        
    int N = 0;

    cin>>N;
    string text;
    getline(cin,text);
    for(int k=1;k<=N;++k){
        string res;
        getline(cin, text);
        for(size_t i =0;i<text.size();++i){
            res+= dictionary[ text.at(i) ];
        }
        cout<<"Case #"<<k<<": "<<res<<endl;
    }
    return EXIT_SUCCESS;    
}


