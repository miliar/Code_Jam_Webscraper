#include <iostream>
#include <vector>
using namespace std;

void func() {
    int adds, opps;
    cin>>adds;
    vector<string> addv, oppv;
    for (int i=0;i<adds;i++) {
        string s;
        cin>>s;
        addv.push_back(s);
    }
    cin>>opps;
    for (int i=0;i<opps;i++) {
        string s;
        cin>>s;
        oppv.push_back(s);
    }
    int n;
    string ss;
    char ch[100];
    char op[100];
    int opl = 0;
    cin>>n;
    for (int i=0;i<n;i++) {
        cin>>ch[i];
        op[opl] = ch[i];
        opl++;
        while (opl > 1) {
            bool combined = false;
            for (int j=0;j<adds;j++) {
                if ((op[opl-1] == addv[j][0] && op[opl-2] == addv[j][1]) ||
                        (op[opl-1] == addv[j][1] && op[opl-2] == addv[j][0])) {
                    op[opl-2] = addv[j][2];
                    opl--;
                    combined = true;
                    break;
                }
            }
            if (!combined) break;
        }
        if (opl > 1) {
            for (int j=0;j<opps;j++) {
                for (int k=0;k<opl-1;k++)
                if ( (op[opl-1] == oppv[j][0] && op[k] == oppv[j][1]) || 
                        (op[opl-1] == oppv[j][1] && op[k] == oppv[j][0]) ) {
                    opl = 0;
                    break;
                }
            }
        }
    }
    if (opl > 0) cout<<op[0];
    if (opl > 1) for (int i=1;i<opl;i++) cout<<", "<<op[i];
}
int main() {
    int t;
    cin>>t;
    for (int i=0;i<t;i++) {
        cout<<"Case #"<<(i+1)<<": [";
        func();
        cout<<"]"<<endl;
    }
    return 0;
}
