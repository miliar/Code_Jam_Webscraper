#include<iostream>
#include<cstdio>
#include<string>
#include<map>
using namespace std;
map<char,char>m;
int main(){
    int T;
    m['y']='a';
    m['e']='o';
    m['q']='z';
    m['a']='y';
    m['b']='h';
    m['c']='e';
    m['d']='s';
    m['e']='o';
    m['f']='c';
    m['g']='v';
    m['h']='x';
    m['i']='d';
    m['j']='u';
    m['k']='i';
    m['l']='g';
    m['m']='l';
    m['n']='b';
    m['p']='r';
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['o']='k';
    m['z']='q';
    m['q']='z';
    scanf("%d",&T);
        string G;
        getline(cin,G);   
    for(int i=0;i<T;i++){
    
        getline(cin,G);
        printf("Case #%d: ",i+1);   
        for(int j=0;j<G.length();j++){
            if(G[j]==' ')cout<<" ";
            else cout<<m[G[j]];   
        }
        cout<<endl;
    }
}
