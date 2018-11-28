#include <iostream>
#include <string>
#include <map>

using namespace std;

typedef pair<string,int> dir;

map <dir, int> id;
//map <int, dir> di;
int tt,n,m,cant,cost;
string path;

#define forn(i,n) for(int (i)=0; (i) < (n); (i)++)

int parser(string str, int parent, int costo)
{
    if (str == "") return 0;
    string name;
    int subpar;
    int index = str.find_first_of("/");
    int res = 0;
    if (index != string::npos )
    {
        name=str.substr(0, index);
        str=str.substr(index+1);
    }else{
        name=str;
        str="";
    }

    dir x;
    x.first = name;
    x.second = parent;

    if (id.find(x) == id.end())
    {
        id[x] = cant;
        cant++;
        res = costo;
    }
    subpar = id[x];
    return res+parser(str, subpar, costo);
}


int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> tt;
    forn(t,tt)
    {
        id.clear();
        cin >> n >> m; getline(cin, path);
        cant = 1;
        forn(i,n)
        {
            getline(cin, path);
            path = path.substr(1);
            parser (path,0,0);
        }
        cost = 0;
        forn(i,m)
        {
            getline(cin, path);
            path = path.substr(1);
            cost += parser(path, 0, 1);
        }

        cout << "Case #" << t+1 << ": " << cost <<  endl;
    }
}
