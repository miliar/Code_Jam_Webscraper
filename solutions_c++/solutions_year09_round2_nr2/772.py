#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main() {
    int nCase;
    char str[505];
    cin>>nCase;
    for(int a=1; a<=nCase; a++) {
        cin>>str;
        int slen = strlen(str);
        bool fold = next_permutation(str,str+slen);
        cout<<"Case #"<<a<<": ";
        if(fold) cout<<str<<endl;
        else {
            int idx = 0;
            while(str[idx]=='0') idx++;
            while(idx>0) {
                str[idx-1] = str[idx];
                str[idx] = '0';
                idx--;
            }
            cout<<str[0]<<"0"<<&str[1]<<endl;
        }
    }
    return 0;
}
