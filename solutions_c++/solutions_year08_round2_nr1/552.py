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

using namespace std;

long long n,N,a,b,c,d,xo,yo,m;
long long re;

int main()
{
    fstream fin("A-small-attempt1.in",ifstream::in);
    fstream fout("A-small-attempt1.out",ofstream::out);
    fin >> N;
    for(int j=1;j<=N;j++)
    {
        re=0;
        fin >> n >> a >> b >> c >> d >> xo >> yo >> m;
        int trs[n][2];
        long long x=xo,y=yo;
        trs[0][0]=xo; trs[0][1]=yo;
        for(int i=1;i<n;i++)
        {
                x=(a*x+b)%m;
                y=(c*y+d)%m;
                trs[i][0]=x;
                trs[i][1]=y;
        }
        rep(i,n-2)
        for(int l=i+1;l<n-1;l++)
        for(int s=l+1;s<n;s++) if ((trs[i][0]+trs[l][0]+trs[s][0])%3==0 && (trs[i][1]+trs[l][1]+trs[s][1])%3==0) re++;
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
