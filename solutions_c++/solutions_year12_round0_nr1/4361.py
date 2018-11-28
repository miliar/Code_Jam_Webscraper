#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<map>

using namespace std;

int main()
{
    int T,i,j;
    string line;
    char *newline;
    char dummy[10];
    map<char,char>tag;

    // mapping
    {
        tag['a']='y';
        tag['b']='h';
        tag['c']='e';
        tag['d']='s';
        tag['e']='o';
        tag['f']='c';
        tag['g']='v';
        tag['h']='x';
        tag['i']='d';
        tag['j']='u';
        tag['k']='i';
        tag['l']='g';
        tag['m']='l';
        tag['n']='b';
        tag['o']='k';
        tag['p']='r';
        tag['q']='z';
        tag['r']='t';
        tag['s']='n';
        tag['t']='w';
        tag['u']='j';
        tag['v']='p';
        tag['w']='f';
        tag['x']='m';
        tag['y']='a';
        tag['z']='q';
    }

    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("A-small-attempt0.out","w",stdout);

    cin >> T;
    gets(dummy);

    for(i=0;i<T;i++){
        getline(cin,line);
        //cout << line << endl;

        newline= new char [line.size()+1];
        strcpy(newline,line.c_str());
        //results
        cout << "Case #" << i+1 << ": ";
        for(j=0;j<strlen(newline);j++) {
            if (newline[j]==' ') cout << " ";
            else cout << tag[newline[j]];
        }
        cout << endl;
    }
    return 0;
}
