#include<iostream>
using namespace std;
int main()
{
    char a[29];
    a['o'-'a']='k';
    a['e'-'a']='o';
    a['j'-'a']='u';
    a['p'-'a']='r';
    a['m'-'a']='l';
    a['y'-'a']='a';
    a['s'-'a']='n';
    a['l'-'a']='g';
    a['c'-'a']='e';
    a['k'-'a']='i';
    a['d'-'a']='s';
    a['x'-'a']='m';
    a['v'-'a']='p';
    a['n'-'a']='b';
    a['r'-'a']='t';
    a['i'-'a']='d';
    a['y'-'a']='a';
    a['b'-'a']='h';
    a['t'-'a']='w';
    a['a'-'a']='y';
    a['h'-'a']='x';
    a['w'-'a']='f';
    a['f'-'a']='c';
    a['p'-'a']='r';
    a['u'-'a']='j';
    a['g'-'a']='v';
    a['z'-'a']='q';
    a['q'-'a']='z';
    int n,i,j,sz;
    string s;
    cin>>n;
    getline(cin,s);
    for(i=0;i<n;i++)
    {
        getline(cin,s);
        sz=s.size();
        cout<<"Case #"<<i+1<<": ";
        for(j=0;j<sz;j++)
        {
            if(s[j]==' ')cout<<s[j];
            else cout<<a[s[j]-'a'];
        }
        cout<<endl;
    }
}
