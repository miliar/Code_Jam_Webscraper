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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,x,y) for(int i=x; i<=y; i++)
#define FORN(i,n) FOR(i,0,n-1)
#define db(x) cerr << (#x) << " = " << x << endl;
#define clr(x) memset(x,0,sizeof(x));
#define ab(x) (max(x,-x))
#define all(x) x.begin(),x.end()
#define sz size()
#define mp make_pair
#define pb push_back
#define re return

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;


int main()
{
	int T;
	cin >> T;
	
	FOR(t,1,T)
	{
		int N;
		cin >> N;
		
		char S[N][N];
		int won[N], played[N];
		double WP[N], OWP[N], OOWP[N];
		
		clr(won);
		clr(played);
		clr(WP);
		clr(OWP);
		clr(OOWP);
		
		FORN(i,N)
		{
			FORN(j,N)
			{
				scanf("\n");
				cin >> S[i][j];
				if(S[i][j] == '1')
					won[i]++;
				if(S[i][j] != '.')
					played[i]++;		
			}
			
			WP[i] = (double)won[i] / (double)played[i];
		}
		
		
		
		FORN(i,N)
		{
			double sum = 0;
			
			FORN(j,N)
			{
				
				if(S[i][j] != '.' && played[j] == 1)
				{
					
				}
				else if(S[i][j] == '1')
				{
					double wpTemp = (double)(won[j]) / (double)(played[j] - 1);
					sum += wpTemp;
				}
				else if(S[i][j] == '0')
				{
					double wpTemp = (double)(won[j] - 1) / (double)(played[j] - 1);
					sum += wpTemp;
				}
			}
			
			if(played[i] == 0.0)
				OWP[i] = 0;
			else
				OWP[i] = (double)sum / (double)played[i];
		}
		
		
		FORN(i,N)
		{
			double sum = 0;
			FORN(j,N)
			{
				if(S[i][j] != '.')
					sum += OWP[j];
			}
			OOWP[i] = (double)sum / (double)played[i];
		}
		
		cout << "Case #" << t << ":\n";
		FORN(i,N)
		{
			//cout << (0.25 * WP[i]) + (0.5 * OWP[i]) + (0.25 * OOWP[i]) << endl;
			printf("%0.12f\n",(0.25 * WP[i]) + (0.5 * OWP[i]) + (0.25 * OOWP[i]) );
		}
		/*
		FORN(i,N)
			cout << WP[i] << "\n";
		cout << "\n\n";
		FORN(i,N)
			cout << OWP[i] << "\n";
		cout << "\n\n";
		FORN(i,N)
			cout << OOWP[i] << "\n";
			*/
	}

    //system("PAUSE");
    re 0;
}
