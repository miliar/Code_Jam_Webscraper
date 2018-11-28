#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define ll long long

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

bool judge(vector<vector<int> > f){
    bool ret = false;
    int tmp = 0;
    for(int i=0;i<4;i++){
        tmp = 0;
        for(int j=0;j<4;j++){
            tmp += f[i][j];
        }
        if(tmp == 4) ret = true;
    }
    for(int i=0;i<4;i++){
        tmp = 0;
        for(int j=0;j<4;j++){
            tmp += f[j][i];
        }
        if(tmp == 4) ret = true;
    }
    tmp = 0;
    for(int i=0;i<4;i++){
        tmp += f[i][i];
    }
    if(tmp == 4) ret = true;
    tmp = 0;
    for(int i=0;i<4;i++){
        tmp += f[3-i][i];
    }
    if(tmp == 4) ret = true;

    return ret;
}

int main(){
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        vector<vector<int> > x(4, vector<int>(4, 0));
        vector<vector<int> > o(4, vector<int>(4, 0));
        char c;
        bool isEmpty = false;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin >> c;
                if(c == 'X' || c == 'T') x[j][k] = 1;
                if(c == 'O' || c == 'T') o[j][k] = 1;
                if(c == '.') isEmpty = true;
            }
        }
        bool isX = judge(x);
        bool isO = judge(o);
        if(isX){
            cout << "Case #" << i+1 << ": X won" << endl;
        }else if(isO){
            cout << "Case #" << i+1 << ": O won" << endl;
        }else if(isEmpty){
            cout << "Case #" << i+1 << ": Game has not completed" << endl;
        }else{
            cout << "Case #" << i+1 << ": Draw" << endl;
        }
    }
}
