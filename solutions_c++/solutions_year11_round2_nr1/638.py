#include <cstdio>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <map>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <bitset>
#include <cstdlib>
using namespace std;

#define rep(i,a,b) for(int i=(a); i<(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin();it!=(v).end(); ++it)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef double fl;

int ma[100+10][100+10];
int n;

int n_match[100+10];

fl wp[100+10];
fl owp[100+10];
fl oowp[100+10];

void solve(int tc)
{
	cout << "Case #" << tc << ":"<<endl;
	char c;
	cin >> n;
	rep(i,0,n)
		rep(j,0,n)
		{
			cin >> c;
			ma[i][j] = c=='1'?1:(c=='0'?-1:0);
		}

	rep(i,0,n)
	{
		n_match[i]=0;
		rep(j,0,n)
			if(ma[i][j])
				++n_match[i];
	}

	rep(i,0,n)
	{
		wp[i] = 0;
		rep(j,0,n)
		{
			if(ma[i][j]==1)
				wp[i] += 1.0;
		}
		wp[i] /= fl(n_match[i]);
	}


	rep(i,0,n)
	{
		owp[i] = 0;
		rep(j,0,n)
		{
			if(ma[i][j]!=0)
			{
				fl tmp = (wp[j]*n_match[j]-int(ma[j][i]==1))/(n_match[j]-1);
				owp[i] += tmp;
			}
		}
		owp[i] /= fl(n_match[i]);
	}


	rep(i,0,n)
	{
		oowp[i] = 0;
		rep(j,0,n)
		{
			if(ma[i][j]!=0)
			{
				oowp[i] += owp[j];
			}
		}
		oowp[i] /= fl(n_match[i]);
	}
	rep(i,0,n)
		cout << (0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]) << endl;
}

int main()
{
	int T;
	cin >> T;
	rep(i,1,T+1)
		solve(i);
  return 0;
}
