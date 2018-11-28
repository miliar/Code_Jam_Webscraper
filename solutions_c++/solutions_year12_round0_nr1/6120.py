#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<stdlib.h>
#include<list>
#include<algorithm>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<sstream>

using namespace std;
#define READ(f) freopen(f, "r", stdin)
int main()
{
    //READ("A-small-attempt1.in");
    //freopen("output.txt","w",stdout);
    int t,i,cas=0;
    map<char,char>m;
    char s[105];
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
    m['o']='k';
    m['p']='r';
    m['q']='z';
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['y']='a';
    m['z']='q';
    cin>>t;
    getchar();
    while(t--){
        gets(s);
        cout<<"Case #"<<++cas<<": ";
        for(i=0;s[i]!=NULL;i++){
            if(s[i]==' '){
                cout<<" ";
                continue;
            }
            cout<<m[s[i]];
        }
        cout<<endl;
    }
    return 0;
}
