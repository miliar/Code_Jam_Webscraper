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

long long n;
long long re;

bool isugly(long long nm)
{
     if (nm==0) return 1;
     if (nm%2==0 || nm%3==0 || nm%5==0 || nm%7==0) return 1;
     return 0;
}

long long slv(string nms,long long ad,bool sign)
{
     long long re=0,tmp;
     for(int i=0;i<nms.length();i++)
     {
             tmp=0;
             rep(k,i+1)
             {
                tmp*=10;
                tmp+=nms[k]-'0';
             }
             if (i==nms.length()-1)
             {
                  if (!sign) tmp=-tmp;
                  tmp=ad+tmp;
                  if (isugly(tmp)) re++;
             }
             else
             {
                  if (!sign) tmp=-tmp;
                  re+=slv(nms.substr(i+1,nms.length()-i),ad+tmp,1);
                  re+=slv(nms.substr(i+1,nms.length()-i),ad+tmp,0);
             }
     }
     return re;
}

int main()
{
    fstream fin("B-small-attempt0.in",ifstream::in);
    fstream fout("B-small-attempt0.out",ofstream::out);
    fin >> n;
    string te;
    for(int j=1;j<=n;j++)
    {
        fin >> te;
        re=slv(te,0,1);
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
