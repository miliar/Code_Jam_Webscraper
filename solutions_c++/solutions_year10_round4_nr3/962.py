#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = ((int)n)-1; i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

int bact[300][110][110];

int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int casos;
    cin >> casos;
    forn(casito,casos)
    {
        int n;
        cin >> n;
        forn(t,300)
        forn(i,110)
        forn(j,110)
        {
            bact[t][i][j] = 0;
        }
        forn(i,n)
        {
            int a,b,c,d;
            cin >> a >> b >> c >> d;
            for(int i=a-1;i<c;i++)
            for(int j=b-1;j<d;j++)
                bact[0][i][j] = 1;
        }
        bool b = true;
        int res = 1;
        while(b==true)
        {
            b = false;
            for(int i=1;i<100;i++)
            for(int j=1;j<100;j++)
            {
                if(bact[res-1][i-1][j]==1&&bact[res-1][i][j-1]==1)
                {
                    bact[res][i][j] = 1;
                    b = true;
                }
                if(bact[res-1][i][j]==1&&(bact[res-1][i-1][j]+bact[res-1][i][j-1]!=0))
                {
                    bact[res][i][j] = 1;
                    b = true;
                }
            }
            for(int i=1;i<100;i++)
                if(bact[res-1][i-1][0] == 1 && bact[res-1][i][0] == 1)
                {
                    bact[res][i][0] = 1;
                    b = true;
                }
            for(int i=1;i<100;i++)
                if(bact[res-1][0][i-1] == 1 && bact[res-1][0][i] == 1)
                {
                    bact[res][0][i] = 1;
                    b = true;
                }
            res++;
        }
        cout << "Case #" << casito+1 << ": " << res-1 << endl;
    }
}
