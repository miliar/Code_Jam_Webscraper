#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps=1e-8
using namespace std;



int main(){
    ofstream fout ("A-small-attempt0.out");
    ifstream fin ("A-small-attempt0.in");

string one="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
string two="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
int map[26];
memset(map,26,sizeof(map));
for (int i=0;i<one.size();i++){
    cout<<one[i]<<" "<<two[i]<<endl;
    if (one[i]-'a'>=0 && one[i]-'a'<=25){
        
        map[one[i]-'a']=two[i]-'a';
        //map[two[i]-'a']=one[i]-'a';
    }
}

    
//'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'.
//map['a'-'a']='y'-'a';
map['y'-'a']=0;
//map['o'-'a']='e'-'a';
map['e'-'a']='o'-'a';
//map['z'-'a']='q'-'a';
map['q'-'a']='z'-'a';
map['z'-'a']='q'-'a';
 for (int i=0;i<=25;i++){
    cout<<(char)(i+'a')<<"->"<<(char)(map[i]+'a')<<endl;
} 
int testcases;
fin>>testcases;
string x;
std::getline(fin,x);
for (int tests=1;tests<=testcases;tests++){
string test;
std::getline(fin,test);
cout<<test<<endl;
string ans;
for (int i=0;i<test.size();i++){
    if (test[i]==' '){
        ans+=' ';
        continue;
    }
    ans+=char(map[test[i]-'a']+'a');
}
cout<<"Case #"<<tests<<": "<<ans<<endl;
fout<<"Case #"<<tests<<": "<<ans<<endl;
} 

//system("pause");
return 0;
}
