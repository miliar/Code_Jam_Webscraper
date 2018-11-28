#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>

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

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ":";
    int N;
    cin >> N;
    VI v(N);
    fi (N-1) cin >> v[i];
    fi (N-1) v[i]--;
    v[N-1] = N;
    //test if possible
    bool ok = true;
    fi (N-1)
    {
      fjj (i+1, v[i])
        if (v[j] > v[i]) ok = false;
    }
    if (not ok)
    {
      cout << " Impossible" << endl;
      continue;
    }
    
    VI ord (N);
    ord[0] = N-1;
    int ii = 1;
    fi (N)
    {
      fj (N-1)
      {
        if (v[j] == ord[i])
          ord[ii++] = j;
      }
    }
//     fi (N) cout <<" " << ord[i];
//     cout << endl;
    
    VL alt (N+1);
    alt [N] = 99999999;
    alt[N-1] = 99999999;
    ll ult = 99999999;
    fii (1,N)
    {
      int a = ord[i];
      int b = v[a];
      int c = v[b];
      double hb = alt[b];
      double hc = alt[c];
      double pen = (hc-hb) / double(c-b);
      double nh = hb - pen * double(b-a);
      ll nalt = min(nh, double(ult));
      nalt--;
      alt[a] = nalt;
      ult = nalt;
    }
    fi (N) cout << " " << alt[i];
    cout << endl;
  }
}