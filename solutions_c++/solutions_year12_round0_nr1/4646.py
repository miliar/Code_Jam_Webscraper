using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define D(x) cout << #x " is " << x << endl

char d [] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
             'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'}; 
             
void decode(string &s){
    for (int i = 0; i < s.size(); i++){
        if (s[i] == ' ') continue;
        int c = int (s[i] - 'a');
        s[i] = d[c];
    }
}

int main(){
    //string a = "a b c d e f g h i j k l m n o p q r s t u v w x y z";
    int cases;
    scanf("%d ", &cases);
    int run = 1;
    while (cases--){
        string s;
        getline(cin, s);
        decode(s);
        printf("Case #%d: %s\n", run++, s.c_str());
    }
    return 0;
}













