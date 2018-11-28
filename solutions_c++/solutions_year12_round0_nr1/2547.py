#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
char p[32];
int main()
{
    int t,T=0;
    scanf("%d",&t);
    p[1]='y';
    p[2]='h';
    p[3]='e';
    p[4]='s';
    p[5]='o';
    p[6]='c';
    p[7]='v';
    p[8]='x';
    p[9]='d';
    p[10]='u';
    p[11]='i';
    p[12]='g';
    p[13]='l';
    p[14]='b';
    p[15]='k';
    p[16]='r';
    p[17]='z';
    p[18]='t';
    p[19]='n';
    p[20]='w';
    p[21]='j';
    p[22]='p';
    p[23]='f';
    p[24]='m';
    p[25]='a';
    p[26]='q';
    char c;
    cin.get(c);
    while(T++<t)
    {
        string s;
        getline(cin,s);
        int i,sz;
        sz=s.size();
        for(i=0;i<sz;i++)
        s[i]=p[s[i]-'a'+1];
        cout<<"Case #"<<T<<": "<<s<<endl;
    }
    return 0;
}
