#include<fstream>
#include<iostream>
#include<set>
#include<utility>
#include<sstream>
#include<string>
using namespace std;

int f(int a, int b)
{
    stringstream ss;
    set<pair<int, int> > t;
    string s;
    for(int i=a; i <= b; ++i)
    {
        ss.str("");
        ss.seekg(ios_base::beg);
        ss<<i;
        s=ss.str();
        ss.str("");
        for(int j=0;j<s.length();)
        {
            ss.seekg(ios_base::beg);
            ss<<s;
            int n=-5;
            ss.seekg(ios_base::beg);
            ss>>n;
            ss.str("");
            if(n>i && n<=b)
                t.insert(make_pair(i,n));
            do s=s.substr(1) + s.substr(0, 1),++j; while(s[0]=='0'&&j<s.length());
        }
    }
    return t.size();
}

int main()
{
    ifstream inf("input.txt");
    ofstream outf("output.txt");
    int n, a ,b;
    inf>>n;
    for(int i=0;i<n;++i)
    {
        outf<<"Case #"<<i+1<<": ";
        inf>>a>>b;
        outf<<f(a,b)<<endl;
    }
    /*stringstream oss;
    string s;
    oss << 456;
    s = oss.str();
    cout<<s<<endl;*/
}
