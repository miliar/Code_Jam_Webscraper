#include <string> 
#include <algorithm> 
#include <cfloat> 
#include <climits> 
#include <cmath> 
#include <complex> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <functional> 
#include <iostream> 
#include <map> 
#include <memory> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 

#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define ALL(x) (x).begin(),(x).end() 
using namespace std;
const double eps = 1e-10;

map<char, char> table;
set<char> used;
string f[] = {
                "yqee",
                "ejp mysljylc kd kxveddknmc re jsicpdrysi",
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                "de kr kd eoya kw aej tysr re ujdr lkgc jv"
             };
string t[] = {
                "azoo",
                "our language is impossible to understand",
                "there are twenty six factorial possibilities",
                "so it is okay if you want to just give up"
             };

//input data
string s;

void solve(int caseNum){
    //solve problem here
    for(int i = 0; i < s.size(); ++i){
        if('a' <= s[i] && s[i] <= 'z')
            s[i] = table[s[i]];
    }
    printf("Case #%d: %s\n", caseNum, s.c_str());
}

int main(){
    int T;

    //create table
    for(char i = 'a'; i <= 'z'; ++i){
        used.insert(i);
    }
    for(int i = 0; i < 4; ++i){
        for(int j = 0; j < f[i].size(); ++j){
            if('a' <= f[i][j] && f[i][j] <= 'z'){
                table[f[i][j]] = t[i][j];
                used.erase(t[i][j]);
            }
        }
    }
    for(int i = 'a'; i <= 'z'; ++i){
        if(table.find(i) == table.end()){
            table[i] = *used.begin();
        }
    }

    cin >> T;

    getline(cin, s);
    for(int i=1; i<=T; ++i){
        //input test case here
        getline(cin, s);

        solve(i);
    }
    return 0;
}
