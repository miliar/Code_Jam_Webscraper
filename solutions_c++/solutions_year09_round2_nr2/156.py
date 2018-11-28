#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

char s[33];

void test()
{
	int n;
	scanf(" %s", s);
	for(n=0;s[n];n++) ;
	for(int i = n-2; i >= 0; i--)
	{
		if(s[i] < s[i+1])
		{
			int best = i+1;
			for(int j = i+1; j < n; j++) if(s[j] > s[i] && s[j] < s[best]) best = j;
			swap(s[i], s[best]);
			sort(s+i+1, s+n);
			printf("%s\n", s);
			return;
		}
	}
	int best = 0;
	for(int i = 0; i < n; i++) if(s[i] > '0' && s[i] < s[best]) best = i;
	swap(s[0], s[best]);
	s[n] = s[1];
	n++;
	s[n] = 0;
	s[1] = '0';
	sort(s+1, s+n);
	printf("%s\n", s);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		test();
	}
}
