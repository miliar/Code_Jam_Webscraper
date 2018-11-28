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

const int inf=1000*1000;

int maxx[10000], maxy[10000], minx[10000], miny[10000];

int solve(string com) {
	for (int i=0; i<10000; i++) {
		minx[i]=inf;
		miny[i]=inf;
		maxx[i]=-inf;
		maxy[i]=-inf;
	}
	int x=5000, y=5000;
	int dx=0, dy=1;
	int area=0;
	for (int i=0; i<sz(com); i++) {
		if (com[i]=='L') {
			swap(dx,dy);
			dx*=-1;
		} else if (com[i]=='R') {
			swap(dx,dy);
			dy*=-1;
		} else {
			int x1=x, y1=y, x2=x+dx, y2=y+dy;
			area+=x1*y2-x2*y1;
			x+=dx, y+=dy;
			if (y1==y2) {
				if (x1>x2) swap(x1,x2);
				miny[x1]=min(miny[x1],y1);
				maxy[x1]=max(maxy[x1],y1);
			} else {
				if (y1>y2) swap(y1,y2);
				minx[y1]=min(minx[y1],x1);
				maxx[y1]=max(maxx[y1],x1);
			}
		}
	}
	int totalArea=0;
	for (int x=0; x<10000; x++)
		for (int y=0; y<10000; y++)
			if ((minx[y]<=x && x<maxx[y]) || (miny[x]<=y && y<maxy[x]))
				totalArea++;
	return totalArea-abs(area)/2;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;
	
	for (int tst=0; tst<tn; tst++) {
		cerr<<tst<<endl;
		int L;
		cin>>L;
		string com="";
		for (int i=0; i<L; i++) {
			string s;
			int cnt;
			cin>>s>>cnt;
			for (int j=0; j<cnt; j++)
				com+=s;
		}
		writeCaseNumber(tst+1);
		cout<<solve(com)<<endl;
	}

	return 0;
}
