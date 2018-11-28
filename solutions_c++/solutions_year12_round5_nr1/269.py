#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		int n, l[1000], p[1000];
		
		scanf("%d", &n);
		
		for(int i=0; i<n; i++) scanf("%d", &l[i]);		
		for(int i=0; i<n; i++) scanf("%d", &p[i]);		
		
		vector<pair<pair<int,int>, int> > t;

		for(int i=0; i<n; i++) t.push_back(make_pair(make_pair(-p[i],-l[i]),i));	

		sort(ALL(t));

		for(int i=0; i<n; i++) printf("%d ", t[i].second);
		printf("\n");
	}

	return 0;
}
