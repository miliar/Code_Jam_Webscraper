/*

brute force??
- invoke: first try to combine backward until no combination happen
- detect opposition: last element with previous elements

*/

#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

vector<string> opposes, combines;
string elems;
int c, d, n;

int main(){

    int ntest;
    cin>>ntest;

    for(int test=1;test<=ntest;test++){
        string str;
        combines.clear();
        opposes.clear();

        cin >> c;
        for(int i=0;i<c;i++){
            cin>>str;
            combines.push_back(str);
        }

        cin>>d;
        for(int i=0;i<d;i++){
            cin>>str;
            opposes.push_back(str);
        }

        cin>>n;
        cin>>elems;
        vector<char> res;
        res.clear();
        for(int i=0;i<n;i++){
            // check evoke
            char elem = elems[i];
            res.push_back(elem);
            bool found = true;
            while (found){
                int m = res.size()-1;
                if (m<1) break;
                found = false;
                for(int j=0;j<c;j++){
                    if ((combines[j][0] == res[m] && combines[j][1] == res[m-1]) ||
                        (combines[j][0] == res[m-1] && combines[j][1] == res[m]) ){
                        res.pop_back();
                        res[m-1] = combines[j][2];
                        found = true;
                        break;
                    }
                }
            }

            // check opposition
            int m = res.size()-1;
            if (m<1) continue;
            for(int j=0;j<d;j++){
                for(int k=0;k<m;k++){
                    if ((opposes[j][0] == res[m] && opposes[j][1] == res[k]) ||
                        (opposes[j][0] == res[k] && opposes[j][1] == res[m]) ){
                        res.clear();
                        break;
                    }
                }
            }
        }
        // print result
        cout<<"Case #"<<test<<": [";
        for(int i=0;i<res.size();i++){
            cout<<res[i];
            if (i<res.size()-1) {
                cout<<", ";
            }
        }
        cout<<"]"<<endl;
    }
    
    return 0;
}
