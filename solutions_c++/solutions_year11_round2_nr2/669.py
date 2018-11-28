#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

struct Inv
{
    int p,v;
    void Rd()
    {
        cin >> p >> v;
    }
} d[2009];

int n,D;

bool check(double time)
{
    double pos = 1e10;
    for (int i = n-1;i >= 0;--i)
    {
            double cango = (pos-D) > d[i].p+time ? d[i].p+time : pos - D;
            double goleft = cango - (D*(d[i].v-1));
        //    cout << "cango" << cango << " goleft" << goleft<< endl;
            if (!(cango-d[i].p - time < eps && d[i].p - goleft - time < eps)) return false;
            double newx = goleft;
            pos = newx;
        //    printf("%f\n",pos);
    }
    return true;
}

int main()
{
    int T;
    cin >> T;
    for (int cs = 0;cs < T;++cs)
    {
        cin >> n >> D;
        for (int i = 0;i < n;++i)
            d[i].Rd();
        int l = 0,r = 0x7ffffff;
      //  cout << check(2.4) << endl;
    //    cout << check(2.5) << endl;
        while (l < r)
        {
            int mid = ((l+r)>>1);
            if (check((double)mid/2))
                r = mid;
            else
                l = mid +1;

        }
        cout << "Case #" << cs+1 << ": " ;
        printf("%.1f",(l/2.0));
        cout  << endl;
    }

}
