#include<iostream>
#include<fstream>

using namespace std;
char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    ifstream fin("1.in");
    ofstream fout("1a.out");
    int t;
    string s;
    fin>>t;
    fin.ignore();
    for(int i=1;i<=t;i++)
    {
        getline(fin,s);
        fout<<"Case #"<<i<<": ";
        for(int j=0;j<s.length();j++)
          if(s[j]!=' ')
            fout<<map[s[j]-'a'];
          else
            fout<<" ";
        fout<<endl;
    }
    return 0;
}

