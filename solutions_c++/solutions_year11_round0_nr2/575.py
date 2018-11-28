#include <iostream>
#include <map>
#include <vector>
#include <stdio.h>
#include <string>
#include <stack>

using namespace std;

int tc, c, d, n;
map<char, map<char, bool> > opposed;
map<char, map<char, char> > combine;
map<char, int> cnt;
string s;
vector<char> res;

void emulate(char c)
{
    while(res.size() && combine[res[res.size() - 1]][c] != 0)
    {
        c = combine[res[res.size() -1]][c];
        res.resize(res.size() - 1);
    }
    for(int i = 0; i < res.size(); i++)
        if(opposed[c][res[i]])
        {
            res.clear();
            return;
        }
    res.push_back(c);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>tc;
    for(int test = 1; test <= tc; test++)
    {
        opposed.clear();
        combine.clear();
        cnt.clear();
        res.clear();
        cin>>c;
        for(int i = 0; i < c; i++)
        {
            cin>>s;
            combine[s[0]][s[1]] = s[2];
            combine[s[1]][s[0]] = s[2];
        }
        cin>>d;
        for(int i = 0; i < d; i++)
        {
            cin>>s;
            opposed[s[0]][s[1]] = true;
            opposed[s[1]][s[0]] = true;
        }
        cin>>n>>s;
        for(int i = 0; i < s.size(); i++)
        {
            char cc = s[i];
            emulate(cc);
        }
        cout<<"Case #"<<test<<": ";
        cout<<"[";
        for(int i = 0; i < res.size(); i++)
        {
            cout<<res[i];
            if(i != res.size() - 1)
                cout<<", ";
        }
        cout<<"]"<<endl;
    }
    return 0;
}