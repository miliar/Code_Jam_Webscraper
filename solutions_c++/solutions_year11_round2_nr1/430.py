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
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;

char s[110][110];
double WP[110];
double WON[110];
int GAMES[110];
double OWP[110];
double OOWP[110];
double RPI[110];

int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)	scanf("%s",s[i]);
		
		for(int i=0;i<n;i++){
			int games=0,won=0;
			for(int j=0;j<n;j++){
				if(s[i][j]=='1')	won++;
				if(s[i][j]!='.')	games++;
			}
			WON[i]=won;
			GAMES[i]=games;
			WP[i] = (double)won/games;
		}
		
		for(int i=0;i<n;i++){
			int games=0;
			double wps=0;
			for(int j=0;j<n;j++){
				if(s[i][j]!='.'){
					games++;
					if(s[i][j]=='1'){
						wps += (WON[j])/(GAMES[j]-1);
					}
					else{
						wps += (WON[j]-1)/(GAMES[j]-1);
					}
				}
			}
			OWP[i] = wps/games;
		}
		
		for(int i=0;i<n;i++){
			int games=0;
			double owps=0;
			for(int j=0;j<n;j++){
				if(s[i][j]!='.'){
					games++;
					owps += OWP[j];
				}
			}
			OOWP[i] = owps/games;
			RPI[i] = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
		}

		printf("Case #%d:\n",caseno++);
		for(int i=0;i<n;i++){
			printf("%.9lf\n",RPI[i]);
		}
	}
	return 0;
}