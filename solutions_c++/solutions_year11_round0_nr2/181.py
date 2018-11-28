#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

char a[256][256];
char b[256][256];

int main(){
    int T; cin >> T;
    string s; 
    string res;
    for (int _ = 0; _ < T; _++){
        int c; cin >> c;
        memset(a,-1,sizeof(a));
        memset(b,-1,sizeof(b));
        for (int i = 0; i < c; i++){
            cin >> s;
        //    Eo(s[0]);Eo(s[1]);Eo(s[2]);
            a[s[0]][s[1]] = s[2];
            a[s[1]][s[0]] = s[2];
        }
        int d; cin >> d;
        for (int i = 0; i < d; i++){
            cin >> s;
            b[s[0]][s[1]] = 0;
            b[s[1]][s[0]] = 0;
        }
        int n; cin >> n;
        cin >> s;
        res.clear();
        for (int i = 0; i < n; i++){
            res += s[i];
            for (;res.size()>1;){
                char x = res[res.size()-1];
                char y = res[res.size()-2];
                if (isupper(a[x][y])){
                    res.resize(res.size()-1);
                    res[res.size()-1] = a[x][y];
                    continue;
                }
                for (int j = 0; j < int(res.size()-1); j++){
                    y = res[j];
                    if (b[x][y] == 0){
                        res.clear();
                        break;
                    }
                }
                break;
            }
        }
        printf("Case #%d: ",_+1);
        printf("[");
        for (int i = 0; i < res.size(); i++){
            if (i) printf(", ");
            printf("%c",res[i]);
        }
        printf("]\n");
    }
	return 0;
}

