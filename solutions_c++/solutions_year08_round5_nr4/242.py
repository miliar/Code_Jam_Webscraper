#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

void writeCaseNumber(int num) { printf("Case #%d: ",num); }


const int mod=10007;
int X,Y;
bool bad[1000][1000];
int ans[1000][1000];

int solve(int x, int y) {
	if (x==X && y==Y) return 1;
	if (x>X) return 0;
	if (y>Y) return 0;
	int &res=ans[x][y];
	if (res!=-1)
		return res;
	res=(!bad[x+1][y+2])*solve(x+1,y+2)+(!bad[x+2][y+1])*solve(x+2,y+1);
	res%=mod;
	return res;
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=0; tst<tn; tst++) {
		cin>>X>>Y;
		int cnt;
		cin>>cnt;
		memset(bad,false,sizeof(bad));
		for (int i=0; i<cnt; i++) {
			int x,y;
			cin>>x>>y;
			bad[x][y]=true;
		}
		memset(ans,-1,sizeof(ans));
		writeCaseNumber(tst+1);
		cout<<solve(1,1)<<endl;
	}
	
	return 0;
}
