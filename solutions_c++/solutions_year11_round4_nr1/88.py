#include<algorithm>
#include<iomanip>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int n;
double Vwalk , Vrun , totL , Trun;

struct walk
{
    double L;
    double Vslow;
    double Vfast;
}W[1001];

bool cmp(walk A , walk B)
{
    if((A.Vfast / A.Vslow) > (B.Vfast / B.Vslow))
        return true;
    return false;
}

void solve()
{
    cin >> totL >> Vwalk >> Vrun >> Trun >> n;
    for(int i = 1 ; i <= n ; i++)
    {
        double lef , rig , dv;
        cin >> lef >> rig >> dv;
        W[i].L = rig - lef;
        totL -= W[i].L;
        W[i].Vslow = dv + Vwalk;
        W[i].Vfast = dv + Vrun;
    }
    n ++;
    W[n].L = totL;
    W[n].Vslow = Vwalk;
    W[n].Vfast = Vrun;
    sort(W + 1 , W + 1 + n , cmp);
    double ans = 0;
    for(int i = 1 ; i <= n ; i++)
    {
        double t = min(Trun , W[i].L / W[i].Vfast);
        ans += t;
        Trun -= t;
        ans += (W[i].L - W[i].Vfast * t) / W[i].Vslow;
    }
    cout << ans << endl;
}

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    cout << fixed << setprecision(10);
    int TestCase;
    cin >> TestCase;
    for(int CaseID = 1 ; CaseID <= TestCase ; CaseID ++)
    {
        cout << "Case #" << CaseID << ": ";
        solve();
    }
    return 0;
}
