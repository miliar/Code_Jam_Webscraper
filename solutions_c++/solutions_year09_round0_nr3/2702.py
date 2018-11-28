#include<iostream>
#include<string>
using namespace std;
int res;
string base="welcome to code jam", palabra;

int backtrack(int b, int p)
{
    if(b==base.size()) return 1;
    if(p==palabra.size()) return 0;
    if(base[b]==palabra[p]) return backtrack(b+1,p+1)+backtrack(b,p+1);
    else return backtrack(b,p+1);
}

string responder()
{
    getline(cin,palabra);
    res=backtrack(0,0);
    string mostrar="";
    while(res)
    {
        char a=res%10+'0';
        mostrar=a+mostrar;
        res/=10;
    }
    while(mostrar.size()<4)
        mostrar="0"+mostrar;
    return mostrar;
}

int main()
{
    int n;
    cin>>n;
    getline(cin,palabra);
    for(int i=0;i<n;i++)
    {
        cout<<"Case #"<<i+1<<": "<<responder()<<endl;
    }
}
