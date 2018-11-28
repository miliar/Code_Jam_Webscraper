#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

ifstream fin("input.txt");
#define cin fin

ofstream fout("output.txt");
#define cout fout

string english;
string googlerese;

map<char, char> mp;

void init()
{
    english      = "abcdefghijklmnopqrstuvwxyz";
    googlerese   = "ynficwlbkuomxsevzpdrjgthaq";
    
    int i, j;
    for(i=0; i<googlerese.size(); i++)
    {
        mp[googlerese[i]] = english[i];
    }
    mp[' '] = ' ';
}

string translate(string en)
{
    string g = "";
    int i;
    for(i=0; i<en.size(); i++)
    {
        g += mp[en[i]];
    }
    return g;
}

int main()
{
    init();
    
    int i, n;
    cin>>n;
    
    char ch[120];
    cin.getline(ch, 120);
    
    for(i=0; i<n; i++)
    {
        cin.getline(ch, 120);
        string g = ch;
        cout<<"Case #"<<i + 1<<": "<<translate(g)<<endl;
    }
    return 0;
}
