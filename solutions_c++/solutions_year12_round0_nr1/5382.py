#include<vector>
#include<algorithm>
#include<cstdio>
#include<iostream>
#include<string>
#include<cstdlib>
#include<sstream>
using namespace std;

string convertInt(int number)
{
   std::stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main(void)
{
    int T,i,j;
    string inp;
    string ans="";
    char t;
    vector <char> con(26,'0');
    con['a'-'a']='y';
    con['b'-'a']='h';
    con['c'-'a']='e';
    con['d'-'a']='s';
    con['e'-'a']='o';
    con['f'-'a']='c';
    con['g'-'a']='v';
    con['h'-'a']='x';
    con['i'-'a']='d';
    con['j'-'a']='u';
    con['k'-'a']='i';
    con['l'-'a']='g';
    con['m'-'a']='l';
    con['n'-'a']='b';
    con['o'-'a']='k';
    con['p'-'a']='r';
    con['q'-'a']='z';
    con['r'-'a']='t';
    con['s'-'a']='n';
    con['t'-'a']='w';
    con['u'-'a']='j';
    con['v'-'a']='p';
    con['w'-'a']='f';
    con['x'-'a']='m';
    con['y'-'a']='a';
    con['z'-'a']='q';
    cin>>T;
    fflush(stdin);
    for(i=0;i<T;++i)
    {
        getline(cin,inp);
        for(j=0;j<inp.size();++j)
        {
            if(inp[j]!=' ')
            inp[j]=con[inp[j]-'a'];
        }
        ans+="Case #";
        ans+=convertInt(i+1);
        ans+=": ";
        ans+=inp;
        ans+="\n";
    }
    system("cls");
    cout<<ans;
    return 0;
}
