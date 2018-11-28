#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;
typedef vector<PI> VPI;

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ":";
    ll N, W, L;
    cin >> N >> W >> L;
    VPI r (N);
    fi (N) cin >> r[i].first;
    fi (N) r[i].second = i;
    sort(r.rbegin(),r.rend());
    VL x, y;
    x = y = VL (N);
    int xa = -r[0].first;
    int ya = 0;
    int mya = 0;
    fi (N)
    {
      if (xa + r[i].first > W)
      {
        x[i] = 0;
        y[i] = mya + r[i].first;
        xa = r[i].first;
        ya = y[i];
        mya = ya + r[i].first;
      }
      else
      {
        x[i] = xa+r[i].first;
        y[i] = ya;
        mya = max (mya, ya + r[i].first);
        xa = x[i] + r[i].first;
      }
    }
    VD xans, yans;
    xans = yans = VD (N);
    fi (N) xans [r[i].second] = x[i];
    fi (N) yans [r[i].second] = y[i];
    cout.setf(ios::fixed);
    cout.precision(1);
    fi (N) cout << " " << xans[i] << " " << yans[i];
    cout << endl;
    
  }
}