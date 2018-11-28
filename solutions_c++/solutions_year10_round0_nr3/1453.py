#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define llong long long

llong r,k,n;
vector<llong> vals;
vector<llong> nextPos;
vector<llong> euros;

void getit(int pos) {
    llong sum=0;
    llong added=0;
    for(int i=0;i<n;i++) {
        int endpos = (pos+i)%n;
        if(sum+vals[endpos] > k) break;
        sum+=vals[endpos];
        added++;
    }
    nextPos.push_back((pos+added)%n);
    euros.push_back(sum);
}

llong solve() {
    vals=vector<llong>(n);
    nextPos.clear();
    euros.clear();
    for(int i=0;i<n;i++) cin>>vals[i];
    for(int i=0;i<n;i++) getit(i);
    llong ret=0;
    int pos=0;
    for(int i=0;i<r;i++) {
        ret+=euros[pos];
        pos=nextPos[pos];
    }
    return ret;
}

int main() {
    int t;
    cin>>t;
    for (int c=1;c<=t;c++) {
        cin>>r>>k>>n;
        cout<<"Case #"<<c<<": "<<solve()<<endl;
    }
}
