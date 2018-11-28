#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <algorithm>
#include <string>

using namespace std;

string conv(int i)
{
    stringstream ss;
    ss << i;
    return ss.str();
}

int main()
{
    freopen ("Recbers.in", "r", stdin);
    freopen ("Recbers.out", "w", stdout);
    int n, i;
    cin >> n;
    for (i=0; i<n; i++)
    {
        int a, b;
        cin >> a >> b;
        int k=0;
        multiset <set <string> > s;
        int j;
        for (j=a; j<=b; j++)
        {
            set <string> ss;
            string x=conv(j);
            ss.insert(x);
            for (int l=0; l<x.size(); l++)
                ss.insert(x.substr(l) + x.substr(0,l));
            k+=s.count(ss);
            s.insert(ss);
        }
        cout << "Case #" << i+1 << ": " << k << endl;
    }
}
