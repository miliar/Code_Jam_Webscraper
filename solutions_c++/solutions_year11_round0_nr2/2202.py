#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<set>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<sstream>

using namespace std;

string result;
string list;

struct e{
    string base;
    char res;
    
    e(string b, char r){
        base = b;
        res = r;
    }
    
    bool operator<(const e& x) const{
        return base < x.base;
    }
};

int test;
int n,c,d;

set<e> combine;
set<e> oppose;

void solve(){
    int l;
    string sub;
    set<e>::iterator it;
    result = "";
    for(int i = 0;i<n;i++){
        sub = "aa";
        l = result.size();
        if (l > 0){
            sub[0] = result[l-1];
            sub[1] = list[i];
            it = combine.find(e(sub,' '));
            if (it!=combine.end()){
                result[l-1] = (*it).res;
            } else{
                for(int j = 0;j<l;j++){
                    sub[0] = result[j];
                    sub[1] = list[i];
                    it = oppose.find(e(sub,' '));
                    if (it!=oppose.end()){
                        result = "";
                        break;
                    }
                }
                if (result.size() ==0){
                    continue;
                } else{
                    result += list[i];
                }
            }
        } else{
            result += list[i];
        }
    }
}

void reverseS(string& s){
    int i = 0;
    int j = s.size()-1;
    while(i<j){
        char t = s[i];
        s[i] = s[j];
        s[j] = t;
        i++; j--;
    }
}


int main(){
    string temp;
    string sub;
    
    ifstream fin("Blarge.in");
    
    fin>>test;
    for(int i = 1;i<=test;i++){
        combine.clear();
        oppose.clear();
        fin>>c;
        for(int j = 0;j<c;j++){
            fin>>temp;
            sub = temp.substr(0,2);
            combine.insert(e(sub,temp[2]));
            reverseS(sub);
            combine.insert(e(sub,temp[2]));
        }
        fin>>d;
        for(int j = 0;j<d;j++){
            fin>>temp;
            oppose.insert(e(temp,' '));
            reverseS(temp);
            oppose.insert(e(temp,' '));
        }
        
        fin>>n;
        fin>>list;
        
        set<e>::iterator it;
        
        solve();
        
        cout<<"Case #"<<i<<": [";
        for(int j = 0;j<result.size();j++){
            if (j==0) cout<<result[j]; else cout<<", "<<result[j];
        }
        cout<<"]"<<endl;
    }
    return 0;
}
