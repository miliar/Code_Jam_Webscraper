#include <iostream>
#include <set>
#include <string>

using namespace std;

int solve()
{
    int i,j;
    int n,m,res=0;
    set<string> exits;    
    string dir,creat;
    exits.insert("");
    cin >> n >> m;
    for(i=0; i<n; ++i) 
    {
        cin >> dir;
        exits.insert(dir);
    }
    
    for(i=0; i<m; ++i)
    {
        cin >> dir;
        while(true)
        {
            if(exits.find(dir)!=exits.end()) break;
            ++res;
            exits.insert(dir);
            int l=dir.length()-1;
            while(dir[l]!='/') --l;
            dir=dir.substr(0, l);
        }
    }
    return res;    
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cnum;
    cin >> cnum;
    for(int cid=1; cid<=cnum; ++cid)
    {
        cout << "Case #"<< cid << ": " << solve() << endl;        
    }
    return 0;    
}
