#include <iostream>
#include <queue>
#include <cstdio>
#include <vector>

#define pb push_back
#define mp make_pair

using namespace std;

vector<pair<long long,long long> > V;

void process(int t)
{
    long long a,b,c,d,x0,y0,M,n;
    cin >> n >> a >> b >> c >> d >> x0 >> y0 >> M;
    long long x,y;

    long long dd[3][3] = {0};

    x= x0; y=y0;
    V.clear();

    dd[x % 3][y % 3] ++;

    for(int i=1;i<=n-1;i++)
    {
	x = (a*x + b) % M;
	y = (c * y + d) % M;

	dd[x % 3][y%3]++;
    }

    long long cnt=0;

    for(int i=0;i<3;i++)
    {
	for(int j=0;j<3;j++)
	{
	    cnt += dd[i][j] * (dd[i][j]-1) * (dd[i][j]-2) / 6;
	}
	cnt += dd[i][0] * dd[i][1] * dd[i][2];
	cnt += dd[0][i] * dd[1][i] * dd[2][i];
    }

    vector<int> perm1;
    perm1.pb(0);
    perm1.pb(1);
    perm1.pb(2);
    do
    {
	cnt += dd[0][perm1[0]] * dd[1][perm1[1]] * dd[2][perm1[2]];
    } while(next_permutation(perm1.begin(),perm1.end()));

    cout << "Case #" << t << ": " << cnt << endl;
}

int main(void)
{
    int T;
    cin >> T;
    for(int i=1;i<=T;i++)
	process(i);
}
