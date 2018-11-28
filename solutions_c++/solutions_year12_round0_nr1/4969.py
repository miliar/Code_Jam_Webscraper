#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

char ch[26];

string t1="zaeqejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
string t2="qyozourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

int T;

int main(){
    scanf("%d",&T);
    for (int i=0;i<26;i++) ch[i]='?';
    for (int i=0;i<t2.size();i++){
        ch[t1[i]-'a']=t2[i];
        }   
    char dum; scanf("%c",&dum);
    for (int t=0;t<T;t++){
        string res="";
        
        while (true){
              char c;
              scanf("%c",&c);
              if (c=='\n') break;
              if (c==' ') res.push_back(c); else res.push_back(ch[c-'a']);
              }

        printf("Case #%d: %s\n",t+1,res.c_str());
        }
    return 0;
    }
