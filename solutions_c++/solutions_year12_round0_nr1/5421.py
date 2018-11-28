#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cfloat>
#include<utility>
#include<set>
#include<memory>
#include<functional>
#include<sstream>
#include<complex>
#include<stack>
#include<queue>
#include<iostream>
#include<vector>
#include<list>
#include<string>
#include<cmath>
#include<map>
#include<algorithm>
#include<fstream>
using namespace std;

int main() {
    //ifstream ifs("A-test-in.txt");
    //ofstream ofs("A-test-out.txt");
    ifstream ifs("A-small-attempt0.in");
    ofstream ofs("A-small-out.txt");

    map<char,char> data;

    data['a']='y';
    data['b']='h';
    data['c']='e';
    data['d']='s';
    data['e']='o';
    data['f']='c';
    data['g']='v';
    data['h']='x';
    data['i']='d';
    data['j']='u';
    data['k']='i';
    data['l']='g';
    data['m']='l';
    data['n']='b';
    data['o']='k';
    data['p']='r';
    data['q']='z';
    data['r']='t';
    data['s']='n';
    data['t']='w';
    data['u']='j'; 
    data['v']='p';
    data['w']='f';
    data['x']='m';
    data['y']='a';
    data['z']='q';

    int num;
    ifs >> num;

    string hoge;
    getline(ifs,hoge);
    for(int i=0;i < num;i++) {
        stringstream ss;
        ss << (i+1);
        string s_num = ss.str();


        string s;
        string res="Case #" + s_num  + ": ";
        getline(ifs,s);
        cout << s << endl;
        
        for(int j=0;j < s.size();j++) {
            if(s[j] != ' ') res+=data[s[j]];
            else res+= ' ';
        }

        cout << res << endl;
        ofs << res << endl;

    }

}
