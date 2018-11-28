#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

//double PI =  3.14159265358979323846;
#define dd long double
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

string sp(int x) {
    string ret="";
    for (int k=0;k<4;k++) {
        ret+=(x%10)+'0';
        x/=10;
    }

    reverse(ret.begin(),ret.end());
    return ret;
}

int main() {
int n;
string ss;
getline(cin,ss);
stringstream sss;sss<<ss;sss>>n;
string p="welcome to code jam";
for (int t=0;t<n;t++) {
    string s;
    getline(cin,s);
    VVI a = VVI(s.size()+1,VI(p.size(),0));
    for (int i=0;i<s.size();i++) {
        for (int j=0;j<p.size();j++) {
            a[i+1][j]+=a[i][j];
            if (s[i]==p[j]) {
                if (j>0) a[i+1][j]+=a[i][j-1];
                else if (j==0) { a[i+1][j]+=1; }
            }
            a[i+1][j]%=10000;        
        }
    }
    int ret=a[s.size()][p.size()-1];
    cout<<"Case #"<<t+1<<": "<<sp(ret)<<endl;
}

}
