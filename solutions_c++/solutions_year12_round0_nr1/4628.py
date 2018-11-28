#include <iostream>
#include <sstream>
#include <map>

using namespace std;

int main(int argc, char** argv) {

    //freopen("input.txt", "rt", stdin);
    freopen("A-small-attempt0.in", "rt", stdin);
    //freopen("C-large-practice.in", "rt", stdin);
   
    
    freopen("output.txt", "wt", stdout);
    
    int N;
    string s;
    
    
    map<char,char> m;
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
    m['q']='z';//
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['y']='a';
    m['z']='q';//
    m[' ']=' ';
    
    scanf("%d\n", &N);
    
    for(int ii=0; ii<N; ii++){
        printf("Case #%d: ", ii+1);
        
        getline(cin,s);
        
        for (int i = 0; i < s.size(); ++i) {
             printf("%c",m[s[i]]);
        }   
        printf("\n");
    }
    return 0;
}

