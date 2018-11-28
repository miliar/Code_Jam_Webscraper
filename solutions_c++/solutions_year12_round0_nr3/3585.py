#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

ifstream fin("input.txt");
#define cin fin

ofstream fout("output.txt");
#define cout fout

string toString(int a)
{
    string s = "";
    
    if(a == 0)
        return "0";
    
    while(a)
    {
        s = (char)(a % 10 + '0') + s;
        a /= 10;
    }
    
    return s;
}

int toInt(string s)
{
    int a = 0;
    int i;
    for(i=0; i<s.size(); i++)
    {
        a *= 10;
        a += (int)(s[i] - '0');
    }
    
    return a;
}

int engez(int a, int b)
{
    int ret = 0;
    
    int i, k;
    for(i=a; i<=b; i++)
    {
        string s = toString(i);
        string t = s;
        do
        {
            s = s[s.size() - 1] + s.substr(0, s.size() - 1);
            int j = toInt(s);
            if(j >= a && j <= b && j > i)
                ret++;
        }
        while(s != t);
    }
    
    return ret;
}

int main()
{
    int i, j, c;
    cin>>c;
    for(i=0; i<c; i++)
    {
        int a, b;
        cin>>a>>b;
        int ret = engez(a, b);
        cout<<"Case #"<<i + 1<<": "<<ret<<endl;
    }
    return 0;
}
