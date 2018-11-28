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
#define FOR(i,a,b) for(int i=a;i<b;i++)

using namespace std;

long long N,n,m,x,y,z;
long long re;
vector <long long> a,dp,el;

long long slv(long long no)
{
     long long ret=1;
     if (dp[no]!=-1) return dp[no];
     for(int k=no+1;k<el.size();k++)
     {
             if (el[k]>el[no]) ret=((ret+slv(k))%1000000007)%1000000007;
     }
     return dp[no]=ret;
}

int main()
{
    fstream fin("C-small-attempt2.in",ifstream::in);
    fstream fout("C-small-attempt2.out",ofstream::out);
    fin >> N;
    string te;
    for(int j=1;j<=N;j++)
    {
        re=0;
        fin >> n >> m >> x >> y >> z;
        a.resize(n);
        el.resize(n);
        dp.resize(n);
        rep(i,m) fin >> a[i];
        rep(i,n) el[i]=a[i%m],a[i%m]=(x*a[i%m]+y*(i+1))%z,dp[i]=-1;
        rep(i,n) re+=slv(i);
        re=re%1000000007;
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
