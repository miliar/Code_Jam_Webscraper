#include <iostream>
#include <vector>
#include <memory>
#include <queue>
#include <stack>

using namespace std;
    
struct Folder {
    string name;
    vector <Folder*> child;
};

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    
    cin >> T;
    
    for(int p=0; p<T; ++p) {
        int n, m;
        string temp, cpy;
        Folder* Root = new Folder();
        Root -> name = "/";
        cin >> n >> m;
        for(int i=0; i<n; ++i) {
            cin >> temp;
            int first = 1, last = 1;
            Folder* qwe = Root;
            while(last<temp.length()) {
                cpy = "";
                bool check = false;
                int adress;
                while(temp[last]!='/' && last<temp.length()) last++;
                for(int k=first; k<last; ++k) cpy += temp[k];
                for(int k=0; k<qwe -> child.size(); ++k)
                    if(qwe -> child[k] -> name == cpy) {
                        check = true;
                        adress = k;
                    }
                if(!check) {
                    Folder* qfold = new Folder();
                    qfold -> name = cpy;
                    qwe -> child.push_back(qfold);
                    qwe = qfold;
                }
                else qwe = qwe -> child[adress];
                first = last++;
            }
        }    
        int res = 0;
        
        for(int i=0; i<m; ++i) {
            cin >> temp;
            int first = 1, last = 1;
            Folder* qwe = Root;
            while(last<temp.length()) {
                cpy = "";
                bool check = false;
                int adress;
                while(temp[last]!='/' && last<temp.length()) last++;
                for(int k=first; k<last; ++k) cpy += temp[k];
                for(int k=0; k<qwe -> child.size(); ++k)
                    if(qwe -> child[k] -> name == cpy) {
                        check = true;
                        adress = k;
                    }
                if(!check) {
                    Folder* qfold = new Folder();
                    qfold -> name = cpy;
                    qwe -> child.push_back(qfold);
                    qwe = qfold;
                    res++;
                }
                else qwe = qwe -> child[adress];
                first = last++;
            }
        }
        printf("Case #%d: %d\n", p+1, res);
    }
    return 0;
}
