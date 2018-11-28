#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <bitset>
#include <set>


#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < n; i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define inp(x) rep(i, sz(x)) cin >> (x)[i];
#define out(x) rep(i, sz(x)) cout << (x)[i];
#define sqr(x) ((x) * (x))

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

int main(int argc, char **argv)
{

	//Small
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w+", stdout);

	/*
	//Large
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w+", stdout);
	*/
	int tt;
	cin >> tt;
	for(int t=1; t<=tt; t++)
	{
		int n;
		scanf("%d\n", &n);
		int* g=new int[n];
		int* w=new int[n];
		double* wp=new double[n];
		double* owp=new double[n];
		double* oowp=new double[n];
		vector<vector<int> > c(n, vector<int>(n, 0));

		char* s=new char[255];

		int wins, games;
		for(int i=0; i<n; i++)
		{
			scanf("%s", s);
			wins=games=0;
			for(int j=0; j<n; j++)
			{
				if(s[j]=='0')
				{
					games++;
					c[i][j]=1;
				}
				else if(s[j]=='1')
				{
					c[i][j]=2;
					wins++;
					games++;
				}
			}
			wp[i]=1.0*wins/games;
			g[i]=games;
			w[i]=wins;
			//cout << wp[i] << endl;
		}

		double maxwp;
		for(int i=0; i<n; i++)
		{
			maxwp=0;
			int count=0;
			double wpa;
			int wins, games;
			for(int j=0; j<n; j++)
			{
				if(c[i][j])
				{
					if(c[i][j]==2) wins=w[j];
					else wins=w[j]-1;
					games=g[j]-1;
					wpa=1.0*wins/games;
					maxwp+=wpa;
					count++;
				}
			}
			if(count) owp[i]=maxwp/count;
			else owp[i]=0;
		//	cout << owp[i] << endl;
		}
		
		double maxowp;
				for(int i=0; i<n; i++)
				{
					int count=0;
					maxowp=0;
					for(int j=0; j<n; j++)
					{
						if(c[i][j])
						{
							maxowp+=owp[j];
							count++;
						}
					}
					if(count) oowp[i]=maxowp/count;
					else oowp[i]=0;
					//cout << oowp[i] << endl;
				}

		printf("Case #%d:\n", t);
		for(int i=0; i<n; i++)
		{
			printf("%.15lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
	return 0;
}
