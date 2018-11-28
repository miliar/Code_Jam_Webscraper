#include<stdio.h>
#include<stdlib.h>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
#include <string>
using namespace std;

class Solver {
  public:
    string solve (char trad[100],string in) {
        for(long long i=0;i<in.size();i++){
            if(in.at(i)!=' ')
                in.at(i)=trad[in.at(i)-'a'];
        }
        return in;
    }
};

int main(int argc,char *argv[]){
    char trad[26];
    for(int i=0;i<26;i++)
        trad[i]='9';
    string s1("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    string a1("our language is impossible to understand");
    string s2("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    string a2("there are twenty six factorial possibilities");
    string s3("de kr kd eoya kw aej tysr re ujdr lkgc jv");
    string a3("so it is okay if you want to just give up");
    for(int i=0;i<s1.size();i++){
        if(s1.at(i)==' ')continue;
        trad[s1.at(i)-'a']=a1.at(i);
    }
    for(int i=0;i<s2.size();i++){
        if(s2.at(i)==' ')continue;
        trad[s2.at(i)-'a']=a2.at(i);
    }
    for(int i=0;i<s3.size();i++){
        if(s3.at(i)==' ')continue;
        trad[s3.at(i)-'a']=a3.at(i);
    }
    trad['z'-'a']='q';
    trad['q'-'a']='z';
	FILE *in = fopen(argv[1],"r");
	stdin = in;
    long qnt;
    scanf("%ld",&qnt);
    for(long i=1;i<=qnt;i++){
        char in[102];
        scanf("\n");
        scanf("%[^\n]",in);
        string st(in);
        Solver solver;
        string res = solver.solve(trad,st);
        printf("Case #%ld: %s\n",i,res.c_str());
    }
    return 0;
}
