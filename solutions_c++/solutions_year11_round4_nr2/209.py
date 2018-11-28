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
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

int main()
{
	freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int casos;
    cin >> casos;
    forn(casito,casos)
    {
        int r,c,d;
        cin >> r >> c >> d;
        vector<vector<int> > blade(r);
        forn(i,r)
        {
            blade[i].resize(c);
            string st;
            cin >> st;
            forn(j,c)
            {
                blade[i][j] = d+ st[j]-'0';
            }
        }
        int res = 0;
        forn(i,r)
        forn(j,c)
        for(int k=3;k<16;k++)
        {
            if(i+k>r||j+k>c)
                continue;
            int a=0,b=0;
            for(int ii=i;ii<i+k;ii++)
            for(int jj=j;jj<j+k;jj++)
            {
                if(ii==i&&jj==j)
                    continue;
                if(ii==i&&jj==j+k-1)
                    continue;
                if(ii==i+k-1&&jj==j)
                    continue;
                if(ii==i+k-1&&jj==j+k-1)
                    continue;
                if(k%2==1)
                {
                    a += blade[ii][jj]*(ii-i-k/2);
                    b += blade[ii][jj]*(jj-j-k/2);
                }
                else
                {
                    a += blade[ii][jj]*(2*ii+1-2*i-k);
                    b += blade[ii][jj]*(2*jj+1-2*j-k);
                }
            }
            if(a==0&&b==0)
                res = max(res,k);
        }
        cout << "Case #" << casito+1 << ": ";
        if(res==0)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << res << endl;
    }
}
