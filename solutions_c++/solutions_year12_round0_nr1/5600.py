/*
Autor : Arojas - rfreak

*/
#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
#include<string.h>
#include<bitset>
#include<set>

#define f(i, a,b) for(int i=int(a);i<int(b);i++)
#define foreach(it, l) for(typeof(l.begin()) it = l.begin();it!=l.end();it++)

using namespace std;
typedef long long LL;
typedef vector<int> v;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii > VQ;
int t;

char c[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w',
'j','p','f','m','a','q'};

void resolve(){
    string line;
    getline(cin,line);
    f(i,0,line.size())
    if(line[i]!=' ')
    cout<<c[line[i]-'a'];
    else cout<<line[i];
    cout<<endl;
}
int main(){
    string line;
    getline(cin,line);
    sscanf(line.c_str(),"%d",&t);
    f(i,0,t){
        cout<<"Case #"<<(i+1)<<": ";
        resolve();
    }
}
