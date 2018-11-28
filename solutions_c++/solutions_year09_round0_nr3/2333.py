#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

#define sz(a) (int)a.size()
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp(a, b) insert(make_pair(a,b))
typedef long long ll;
using namespace std;

char tgt[19] = {'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ',
                't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm'};
vector<int> cnt;
string str;

ll q;


void rec(int now, int a){
    if(now == 18){
        ++q;
        return;
    }
    
    for(int i=a+1; i<sz(str); ++i){
        if(str[i] == tgt[now+1]) rec(now+1, i);
    }
//     for(int i=a; i<sz(str); ++i){
//         if(str[i] == tgt[now+1] && cnt[now]){
//             ++now;
//             ++cnt[now];
//         }else if(str[i] == tgt[now]){
//             ++cnt[now];
//         }
//     }
}

int main(){
    int n;  cin >> n;
    string tmp; getline(cin, tmp);
    for(int fase=0; fase<n; ++fase){
        cnt.clear();
        cnt.resize(19, 0);
        int now=0;
        str="";
        getline(cin, str);
        q=0;
        for(int i=0; i<sz(str); ++i)
            if(str[i] == 'w') rec(0, i);
        
        //for(int i=0; i<19; ++i){cout << cnt[i]  << endl; ans *= cnt[i];}
        stringstream ss;  ss << q;
        string s_ans=ss.str();
        for(; sz(s_ans)<4; s_ans.insert(s_ans.begin(),'0'));
        cout << "Case #"<< fase+1<<": ";
        for(int i=0; i<4; ++i) cout << s_ans[sz(s_ans)+i-4];
        cout <<  endl;
    }
    return 0;
}
