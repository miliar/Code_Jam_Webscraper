#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>
#include<cmath>

#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)

#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>
#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000
#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL long long
#define LD long double

using namespace std;

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0-2.out", "w", stdout);
  //freopen("C-small-attempt1.in", "r", stdin); //freopen("C-small-attempt1.out", "w", stdout);
  freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
  //freopen("C-small-attempt2.in", stdin, "r"); freopen("C-small-attempt2.out", stdout, "w");

  //freopen("C-large.in", stdin, "r"); freopen("C-large.out", stdout, "w");
  int T;
	cin >> T;
	int count = 1;
	while( count <= T )
	{
		int N, L, H;
		cin >> N >> L >> H;
		int i;
		LL notes[N];
		//LL ans = H;
		LL ans = -1;
		bool no = true;

		REP(i, N)
			cin >> notes[i];

//		REP( i, N )
//		{
//			for( LL freq = L; freq <= ans; freq++ )
//			{
//				if( notes[i] == freq )
//					continue;
//				if( freq < notes[i] && notes[i]%freq == 0 && freq <= ans )
//				{
//					ans = freq;
//					no = false;
//				}
//				else if( freq%notes[i] == 0 && freq <= ans )
//				{
//					ans = freq;
//					no = false;
//				}
//
//			}
//		}

		for( LL freq = L; freq <= H; freq++ )
		{
			bool inHarmony = true;
			REP(i, N)
			{
				if( freq < notes[i] && notes[i]%freq == 0 )
					continue;
				else if( freq >= notes[i] && freq%notes[i] == 0 )
					continue;
				else
				{
					inHarmony = false;
					break;
				}
			}
			if( inHarmony == true )
			{
				ans = freq;
				break;
			}

		}

		cout << "Case #" << count << ": ";
		if( ans == -1 )
			cout << "NO" << endl;
		else
			cout << ans << endl;
		count++;
	}
}

