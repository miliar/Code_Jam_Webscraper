#include <iostream>
#include <map>
#include <string>
using namespace std;
map<string,int> haveDir;
map<string,int> allDir;
map<string,int>::iterator itr;
void newdir(map<string,int>& dir, string line)
{
    //cout << "l:" << line << endl;
    int start = 1, np;
    while( (np=line.find('/', start))!=string::npos)
    {
        start = np;
        //cout << start << endl;
        //cout << line.substr(0, start) << endl;
        dir[line.substr(0, start)] = 1;
        ++start;
    }
    dir[line] = 1;
}
void makedir(map<string,int>& dir, string line)
{
    int start = 1,np;
    while( (np=line.find('/', start))!=string::npos)
    {
        start = np;
        itr = haveDir.find(line.substr(0, start));
        //cout << start << endl;
        //cout << line.substr(0, start) << endl;
        if(itr==haveDir.end())
        {
            dir[line.substr(0, start)];
        }
        ++start;
    }
    if(haveDir[line]==0)dir[line] = 1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t,n,m;
    cin >> t;
    for(int ca = 1; ca <= t; ++ca)
    {
        cin>>n>>m;
        string line;
        allDir.clear();
        haveDir.clear();
        for(int i=0;i<n;++i)
        {
            cin>>line;
            newdir(haveDir, line);
        }
        for(int i=0;i<m;++i)
        {
            cin>>line;
            makedir(allDir, line);
        }
        int c=0;
        for(itr=allDir.begin();itr!=allDir.end();++itr)
            ++c;
        cout << "Case #" << ca << ": " << c << endl;
    }
   return 0;
}
