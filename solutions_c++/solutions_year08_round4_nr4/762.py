#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int n,k,re;
string s;
vector<int> cp;
set<int> cs;

int csize(string s)
{
    char t=s[0];
    int re=1;
    for(int i=1;i<s.length();i++)
    {
            if (s[i]!=t) re++,t=s[i];
    }
    return re;
}

int tr()
{
    string s1=s;
    rep(i,s.length()/k)
    {
        rep(m,k)
        {
           s1[i*k+m]=s[i*k+cp[m]];
        }
    }
    return csize(s1);
}

void appe(int no)
{
     rep(i,k)
     {
        if (!cs.count(i+1))
        {
           cs.insert(i+1);
           cp[no]=i;
           if (no<k-1) appe(no+1);
           else re=min(re,tr());
           cs.erase(i+1);
        }
     }
}

int main()
{
    fstream fin("D-small-attempt0.in",ifstream::in);
    fstream fout("D-small-attempt0.out",ofstream::out);
    fin >> n;
    for(int j=1;j<=n;j++)
    {
        fin >> k;
        fin >> s;
        cp.resize(k);
        re=50001;
        cs.clear();
        appe(0);
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
