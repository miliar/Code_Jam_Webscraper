#include <iostream>
#include <vector>
#include <set>
#include <string>

#define inf 1000

using namespace std;

int N;
vector<string> col;
vector <int> ini,fin;
int resp;
int act;
vector <bool> us;

void back (int a)
{
    if (act>=resp)
        return;
    if (a==N)
    {
        set <string> lc;
        for (int i=0;i<N;i++)
        {
            if (us[i])
                lc.insert(col[i]);
        }
        if (lc.size()>3)
            return;
        vector <int> par (10001,0);
        for (int i=0;i<N;i++)
        {
            if (us[i])
            for (int j=ini[i];j<=fin[i];j++)
            {
                par[j]=1;
            }
        }
        for (int i=1;i<10001;i++)
            if (par[i]==0)
                return;
        resp=act;
        return;
    }
    us[a]=true;
    act++;
    back(a+1);
    us[a]=false;
    act--;
    back(a+1);
}

int main()
{
    int T;
    cin >> T;
    for (int caso=1;caso<=T;caso++)
    {
        cin >> N;
        col=vector <string> (N);
        ini=vector <int> (N);
        fin=vector <int> (N);
        us=vector <bool> (N,false);
        for (int i=0;i<N;i++)
        {
            cin >> col[i];
            cin >> ini[i] >> fin[i];
        }
        resp=inf;
        act=0;
        back(0);
        cout << "Case #" << caso << ": ";
        if (resp==inf)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << resp << endl;
    }
}
