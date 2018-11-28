#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;
int T,N;
char in[40];

int main() {
    cin>>T;
    cin.getline(in+1,39);
    for(int i=0;i<T;i++) {
        in[0]='0';
        cin.getline(in+1,39);
        next_permutation(in,in+strlen(in));
        cout<<"Case #"<<(i+1)<<": ";
        if(in[0]!='0') cout<<in[0];
        cout<<(in+1)<<"\n";
    }
    return 0;
}
