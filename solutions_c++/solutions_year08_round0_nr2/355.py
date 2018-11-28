#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;

int solve()
{
	int t;
	int na, nb;
	scanf("%d", &t);
	scanf("%d%d",&na,&nb);

	vector<pair<int, int> > v;

	REP(i, na) {
		int a, b, c, d;
		scanf("%d:%d", &a, &b);
		scanf("%d:%d", &c, &d);
		v.push_back(make_pair(a*60 + b, 2));		
		v.push_back(make_pair(c*60 + d+t, 0));		
	}
	REP(i, nb) {
		int a, b, c, d;
		scanf("%d:%d", &a, &b);
		scanf("%d:%d", &c, &d);
		v.push_back(make_pair(a*60 + b, 3));		
		v.push_back(make_pair(c*60 + d+t, 1));		
	}
	sort(v.begin(), v.end());

	int reta = 0, retb = 0;
	int cura = 0, curb = 0;
	EACH(i,v) {
		switch (v[i].second) {
		case 2:
			if (cura == 0) reta++;
			else cura--;
			break;
		case 3:
			if (curb == 0) retb++;
			else curb--;
			break;
		case 0:
			curb++;
			break;
		case 1:
			cura++;
			break;
		default:
			break;
		}
	}
	printf("%d %d\n", reta, retb);
}


int main(void)
{
	int test;
	int cnt = 0;
 	scanf("%d", &test);

	REP(i, test) {
		printf("Case #%d: ", ++cnt);
		solve();
	}

	return 0;
}

