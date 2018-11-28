#include<cstdio>
#include<vector>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<sstream>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<fstream>
using namespace std;
char t[128][128];
char T[128][128];
char s[101];
int caso;

void opp(vector<char> &v){
    int n=v.size();
    for(int i=n-2;i>=0;--i){
        if(T[v[n-1]][v[i]]){
            v.clear();
            return;
        }
    }
}

void com(vector<char> &v){
    int n=v.size();
    if(n>=2&&t[v[n-2]][v[n-1]]){
        v.pop_back();
        v.pop_back();
        v.push_back(t[v[n-2]][v[n-1]]);
        com(v);
    }
    opp(v);
}

bool doit(){
    memset(t,0,sizeof(t));
    memset(T,0,sizeof(T));
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;++i){
        scanf("%s",s);
        t[s[0]][s[1]]=t[s[1]][s[0]]=s[2];
    }
    scanf("%d",&n);
    for(int i=0;i<n;++i){
        scanf("%s",s);
        T[s[0]][s[1]]=T[s[1]][s[0]]=1;
    }
    scanf("%d%s",&n,s);
    vector<char> v;
    for(int i=0;i<n;++i){
        v.push_back(s[i]);
        com(v);
    }
    printf("Case #%d: [",++caso);
    if(!v.empty())printf("%c",v[0]);
    for(int i=1;i<v.size();++i){
        printf(", %c",v[i]);
    }
    puts("]");
}
int main(){
    int n;
    scanf("%d",&n);
    while(n--)doit();
}
