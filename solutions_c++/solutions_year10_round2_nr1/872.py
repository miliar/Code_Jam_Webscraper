#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

struct d {
    map<string, int> sub;
    string name;
};

d file[100000];
int len;

int rst;

void gao(int index, string name) {
    if (name.size() == 0)
        return ;
    size_t s = name.find('/');
    string n = name.substr(0, s);
    if (file[index].sub.find(n) == file[index].sub.end()) {
        file[len].sub.clear();
        file[len].name = s;
        file[index].sub[n] = len;
        rst++;
        len++;
    }
    //cout<<index<<' '<<name<<' '<<rst<<endl;
    if (s != string::npos) {
        gao(file[index].sub[n], name.substr(s + 1));
    }
}

void process() {
    string s;
    cin>>s;
    gao(0, s.substr(1));
}

int main()
{
    int ca;
    cin>>ca;
    for (int index = 1; index <= ca; index++)
    {
        string s;
        file[0].sub.clear();
        file[0].name = "root";
        len = 1;
        rst = 0;
        int M, N;
        cin>>M>>N;
        REP(i, M)
            process();
        rst = 0;
        REP(i, N)
            process();
        printf("Case #%d: %d\n", index, rst);
    }
    return 0;
}
