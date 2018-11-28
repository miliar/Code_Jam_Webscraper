#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


void split(const string& dir0, vector<string>& v) {
    for (int i=1; i<int(dir0.length()); i++)
        if (dir0[i]=='/')
            v.push_back(dir0.substr(0, i));
    v.push_back(dir0);
}

int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        int N, M; cin>>N>>M;
    
        vector<string> ready;
        for (int i=0; i<N; i++) {
            string dir; cin>>dir;
            split(dir, ready);
        }
        
        vector<string> wanted;
        for (int i=0; i<M; i++) {
            string dir; cin>>dir;
            split(dir, wanted);
        }
        
        sort(ready.begin(), ready.end());
        ready.erase(unique(ready.begin(), ready.end()), ready.end());
        sort(wanted.begin(), wanted.end());
        wanted.erase(unique(wanted.begin(), wanted.end()), wanted.end());
        
        vector<string> mkdir(wanted.size());
        vector<string>::iterator it = set_difference(wanted.begin(), wanted.end(), ready.begin(), ready.end(), mkdir.begin());
        int result = it - mkdir.begin();
        
/*        for (int i=0; i<result; i++)
            cout<<mkdir[i]<<endl;*/
        
        cout<<"Case #"<<t<<": "<<result<<endl;
    }
    
    return 0;
}
