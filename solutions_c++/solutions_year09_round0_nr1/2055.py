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
#define VS vector<string>

int main() {
    int L,D,N;
    cin>>L>>D>>N;
    VS a;
    for (int i=0;i<D;i++) {string s; cin>>s; a.PB(s); }
    for (int j=0;j<N;j++) {
        string s;
        cin>>s;
        VS pom;
        int count=0;
        string tmp="";
        for (int i=0;i<s.size();i++) {
            if (s[i]=='(') { count++; tmp=""; continue;  }
            if (s[i]==')') { count--; pom.PB(tmp); continue;}
            if (count==0) { tmp=""; tmp+=s[i]; pom.PB(tmp); continue;}
            else { tmp+=s[i];}
        }
        
        int ret=0;
        for (int i=0;i<a.size();i++) {
            if (pom.size()!=a[i].size()) continue;
            bool ok=true;
            for (int k=0;k<L;k++) {
                bool dobre=false;
                for (int u=0;u<pom[k].size();u++) if (pom[k][u]==a[i][k]) dobre=true;
                if (!dobre) ok=false;
            }
            if (ok) ret++;
        }
        cout<<"Case #"<<j+1<<": "<<ret<<endl;
    }
}
