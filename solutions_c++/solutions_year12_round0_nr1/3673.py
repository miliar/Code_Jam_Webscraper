#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

string remap(const string source)
{
    int i;
    string target;
    for(i=0;i<source.size();i++)
    {
        switch(source[i])
        {
            case ' ' :
                target.push_back(' ');
                break;
            case 'a' :
                target.push_back('y');
                break;
            case 'b' :
                target.push_back('h');
                break;
            case 'c' :
                target.push_back('e');
                break;
            case 'd' :
                target.push_back('s');
                break;
            case 'e' :
                target.push_back('o');
                break;
            case 'f' :
                target.push_back('c');
                break;
            case 'g' :
                target.push_back('v');
                break;
            case 'h' :
                target.push_back('x');
                break;
            case 'i' :
                target.push_back('d');
                break;
            case 'j' :
                target.push_back('u');
                break;
            case 'k' :
                target.push_back('i');
                break;
            case 'l' :
                target.push_back('g');
                break;
            case 'm' :
                target.push_back('l');
                break;
            case 'n' :
                target.push_back('b');
                break;
            case 'o' :
                target.push_back('k');
                break;
            case 'p' :
                target.push_back('r');
                break;
            case 'q' :
                target.push_back('z');
                break;
            case 'r' :
                target.push_back('t');
                break;
            case 's' :
                target.push_back('n');
                break;
            case 't' :
                target.push_back('w');
                break;
            case 'u' :
                target.push_back('j');
                break;
            case 'v' :
                target.push_back('p');
                break;
            case 'w' :
                target.push_back('f');
                break;
            case 'x' :
                target.push_back('m');
                break;
            case 'y' :
                target.push_back('a');
                break;
            case 'z' :
                target.push_back('q');
                break;
        }
    }
    //cout<<"in remap : "<<target<<endl;
    return target;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    string str;
    string res;
    int test,i=1;
    cin>>test;
    getline(cin,str);
    while(test--)
    {
        getline(cin,str);
        //cin>>str;
        res=remap(str);
        cout<<"Case #"<<i<<": "<<res<<endl;
        i++;
    }
    return 0;
}
