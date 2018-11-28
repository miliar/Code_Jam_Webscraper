#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void myreplace(string &a, string &b, string &c){
    int pos = a.find(b);
    string tmp = a.substr(0,pos) + c + a.substr(pos+b.length());
    a = tmp;
}

int main(){
    int T, N;
    int c = 1;
    cin >> T;
    while(T--){
        map<string,string> combines;
        map<string,string> opposites;
    
        string tmp, ans, line;
        cin >> N;
        for(int i = 0; i < N; ++i){
            cin >> tmp;
            combines[tmp.substr(0,2)] = tmp.substr(2);
            combines[string(1,tmp[1]) + string(1,tmp[0])] = tmp.substr(2);
        }
        cin >> N;
        for(int i = 0; i < N; ++i){
            cin >> tmp;
            opposites[tmp.substr(0,1)] = tmp.substr(1);
            opposites[tmp.substr(1,1)] = tmp.substr(0,1);
        }
        cin >> N;
        cin >> line;
        string last = line.substr(0,1);
        ans = last;
        //cout << ans << endl;
        for(int i = 1; i < N; ++i){
            tmp = last + line.substr(i,1);
            last = line.substr(i,1);
            if(combines[tmp] != ""){
                ans = ans.substr(0,ans.length()-1) + combines[tmp];
                last = "";
            }
            else{
                if(opposites[last] != ""){
                    int pos = ans.find(opposites[last]);
                    if(pos!=string::npos){
                        ans = "";
                        last = "";
                    }
                    else
                        ans += last;
                }
                else{
                    ans += last;
                }
            }
            //cout << ans << endl;
        }
        cout << "Case #" << c++ << ": [";
        for(int i = 0; i < ans.length(); ++i){
            cout << ans[i];
            if(i < ans.length()-1)
                cout << ", ";
        }
        cout << "]" << endl;
    }
    return 0;
}
