#include<algorithm>
#include<cmath>
#include<iomanip>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<sstream>
#include<vector>
#include<iostream>
#include<fstream>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

bool anda(int n, int b)
{
    int res=0;
    set<int> nums;
    while(nums.find(res)==nums.end())
    {
        nums.insert(res);
        res = 0;
        while(n>0)
        {
            res += (n%b)*(n%b);
            n /= b;
        }
        n = res;
    }
    if(n == 1)
        return true;
    return false;
}

int main()
{
    ifstream fin("A-small.in");
    ofstream fout("A-small.out");
    int caso;
    fin >> caso;
    string st;
    getline(fin,st);
    forn(casito,caso)
    {
        int res = 1;
        getline(fin,st);
        vector<int> bases;
        istringstream iss;
        iss.str(st);
        iss.clear();
        int n;
        while(iss >> n)
            bases.pb(n);
        bool p = false;
        while(p==false)
        {
            res++;
            p = true;
            forn(i,bases.size())
            {
                if(anda(res,bases[i])==false)
                    p = false;
            }
        }
        fout << "Case #" << casito+1 << ": " << res << endl;
    }
    return 0;
}
