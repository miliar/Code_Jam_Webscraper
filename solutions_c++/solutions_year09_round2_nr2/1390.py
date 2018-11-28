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

using namespace std;

int main(){
    int n;
    cin >> n;
    for(int cc=0; cc<n; ++cc){
        string s;
        cin >> s;
        string tmp = s;
        sort(all(s));
        string mm ="zzzzzzzzzzzzzzzzzzzz";
        bool flag = false;
        string mmm = "zzzzzzzzzzzzzzzzzzzz";
        do{
            if(s > tmp && s < mm && s[0] != '0'){
                mm = s;
                flag = true;
            }
            if(s[0] != '0' && s < mmm){
                mmm = s;
            }
        }while(next_permutation(all(s)));

        if(!flag){
            mmm.insert(1,1, '0');
            mm = mmm;
        }
        
        cout << "Case #"<<cc+1<<": "<<mm  << endl;
    }
    return 0;
}
