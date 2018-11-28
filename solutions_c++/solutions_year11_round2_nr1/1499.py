#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <iomanip>

using namespace std;

#define pb push_back
#define INF 101111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define ford(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

const int maxN = 100;

char B[maxN][maxN];
double rpi[maxN], wp[maxN], owp[maxN], oowp[maxN];
int N;

void solve();

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
        //freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    FOR(cs,1,T+1)
    {
        cin >> N;

        rep(i,N) rep(j,N) cin >> B[i][j];

        solve();

        cout << "Case #" << cs <<":" << endl;


        rep(i,N) cout << setprecision (8)<< rpi[i] << endl;
    }

	return 0;
}

void solve()
{
    int cnt[maxN];
    CL(cnt,0);

    rep(i,N)
    {
        cnt[i] = 0;
        wp[i] = 0;
        rep(j,N) if(B[i][j] != '.')
        {
            cnt[i] ++;
            if(B[i][j] == '1' ) wp[i] += 1.0;
        }
    }

    //rep(i,N) cout << wp[i]/cnt[i] << ' '; cout << endl;

    int cnt2[maxN];
    CL(cnt2,0);

    rep(i,N)
    {
        owp[i] = 0;
        cnt2[i] = 0;

        rep(j,N) if(i!=j)
        {
            if(B[j][i]=='.') continue;

            cnt2[i]++;

            double a = B[j][i]=='1' ? 1 : 0;

            owp[i] += (wp[j]-a)/(cnt[j]-1);
        }
    }

    //rep(i,N) cout << owp[i]/cnt2[i] << ' '; cout << endl;

    rep(i,N)
    {
        oowp[i] = 0;

        rep(j,N) if(i!=j)
        {
            if(B[j][i]=='.') continue;

            double a = B[j][i]=='1' ? 1 : 0;
            double aa = B[j][i]=='1' ? (wp[j]-a)/(cnt[j]-1) : 0;

            //oowp[i] += (owp[j]-aa)/(cnt2[j]-1);
            oowp[i] += owp[j]/cnt2[j];
        }

        oowp[i] /= cnt2[i];
    }

    //rep(i,N) cout << oowp[i] << ' '; cout << endl;

    rep(i,N) wp[i] /= cnt[i], owp[i] /= cnt2[i];

    rep(i,N) rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
}
