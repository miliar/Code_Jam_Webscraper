#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define x first
#define y second
#define c first

vector<int> M;

int rec(int a,int b){
    bool c = 0;
    for(int i=0;i<b;i++) if(M[i] != 0){
            c = 1;
            M[i]--;
    }
    if(c == 0) return 0;
    else return 1 + rec(a,(a+b)/2) + rec((a+b)/2, b);
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
            cout << "Case #" << t << ": ";
            int P;
            cin >> P;
            int p=1; for(int i=0;i<P;i++) p*=2;
            M = vector<int> (p);
            for(int i=0;i<p;i++){ int a; cin >> a; M[i] = P-a; }
            for(int i=0;i<p-1;i++){ int a; cin >> a; }
            
            
            cout << rec(0,p) << endl;
    }
}



