#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int count=0;
    string s;
    char c[256];
    c[0]='y';
    c[1]='h';
    c[2]='e';
    c[3]='s';
    c[4]='o';
    c[5]='c';
    c[6]='v';
    c[7]='x';
    c[8]='d';
    c[9]='u';
    c[10]='i';
    c[11]='g';
    c[12]='l';
    c[13]='b';
    c[14]='k';
    c[15]='r';
    c[16]='z';
    c[17]='t';
    c[18]='n';
    c[19]='w';
    c[20]='j';
    c[21]='p';
    c[22]='f';
    c[23]='m';
    c[24]='a';
    c[25]='q';
    getline(cin,s);
    while(t!=count)
    {
        count++;
        getline(cin,s);
        for(int i=0;i<s.length();i++)
        {
            if(s[i]==' ')continue;
            s[i]=c[s[i]-'a'];
        }
        cout<<"Case #"<<count<<":"<<" ";
        cout<<s<<endl;
    }
    return 0;
} 
