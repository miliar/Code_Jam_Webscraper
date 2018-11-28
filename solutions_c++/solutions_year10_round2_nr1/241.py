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

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
            cout << "Case #" << t << ": ";
            int N,M;
            cin >> N >> M;
            map<string,bool> dir;
            dir["/"] = 1;
            for(int i=0;i<N;i++){
                    string s;
                    cin >> s;
                    s+='/';
                    dir[s] = 1;
            }
            
            int sol = 0;
            for(int i=0;i<M;i++){
                    string s;
                    cin >> s;
                    s+='/';
                    for(int i=0;i<s.size();i++) if(s[i] == '/' && !dir.count(s.substr(0,i+1)) ){
                            for(int k=i;k<s.size();k++){
                                    if(s[k] == '/'){
                                            sol++;
                                            dir[s.substr(0,k+1)] = 1;
                                    }
                            }
                            break;
                    }
            }
            cout << sol << endl;
    }
}





