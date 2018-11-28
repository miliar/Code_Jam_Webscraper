#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))

using namespace std;

typedef long long ll;
typedef long double ld;

const double pi = acos(-1.0);

int a[200][200];

int main()
{
	int T;
	cin >> T;
	for (int I=0;I<T;I++){
		int n;
		cin >> n;
		memset(a,0,sizeof(a));
		vector <pair <int,int> > die;
		vector <pair <int,int> > born;
		for (int i=0;i<n;i++){
			int x1,y1,x2,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int x=x1;x<=x2;x++){
				for (int y=y1;y<=y2;y++)a[x][y]=1;
			}
			
		}
		int K=0;
		for (int i=1;i<=100;i++){
			for (int j=1;j<=100;j++){
				if (a[i][j]==1&&a[i-1][j]==0&&a[i][j-1]==0)die.push_back(make_pair(i,j));
				if (a[i][j]==0&&a[i-1][j]==1&&a[i][j-1]==1)born.push_back(make_pair(i,j));
				K+=a[i][j];
			}

		}
		int ans=0;
		while (1){
			//if (ans==1){
			/*for (int i=1;i<6;i++){
				for (int j=1;j<6;j++)cerr << a[i][j];
				cerr << endl;
			}
			cerr << endl;*/
			vector <pair <int,int> > ddie;
			vector <pair <int,int> > bborn;
			//for (int i=0;i<(int)die.size();i++)cerr << die[i].first << ' ' << die[i].second << endl;return 0;
			for (int i=0;i<(int)born.size();i++)if (abs(a[born[i].first-1][born[i].second])==1&&abs(a[born[i].first][born[i].second-1])==1&&a[born[i].first][born[i].second]==0){
				a[born[i].first][born[i].second]=2;
				bborn.push_back(make_pair(born[i].first+1,born[i].second));
				bborn.push_back(make_pair(born[i].first,born[i].second+1));
			}
			for (int i=0;i<(int)die.size();i++)if (a[die[i].first][die[i].second]==1&&a[die[i].first-1][die[i].second]%2==0&&a[die[i].first][die[i].second-1]%2==0){
				a[die[i].first][die[i].second]=-1;
				ddie.push_back(make_pair(die[i].first+1,die[i].second));
				ddie.push_back(make_pair(die[i].first,die[i].second+1));
			}
			for (int i=0;i<(int)born.size();i++)if (a[born[i].first][born[i].second]==2){
				a[born[i].first][born[i].second]=1;K++;
			}
			for (int i=0;i<(int)die.size();i++)if (a[die[i].first][die[i].second]==-1){
				a[die[i].first][die[i].second]=0;K--;
			}
			ans++;
			if (K==0)break;
			die=ddie;
			born=bborn;
		}
		cout << "Case #" << I+1 << ": " << ans << endl;
	}
	return 0;
}
