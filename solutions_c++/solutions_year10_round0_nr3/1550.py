#include<cstdio>
#include<vector>

using namespace std;

int main(void)
{
	int T;
	scanf("%d",&T);

	for(int t=1; t<=T; t++) {
		vector<int> v;
		vector<int> next;
		vector<int> m;

		int r, n, k;
		scanf("%d %d %d",&r, &k, &n);
		v.reserve(n);
		next.reserve(n);
		m.reserve(n);
		for(int i=0; i<n; i++) {
			int temp; scanf("%d",&temp);
			v.push_back(temp);
		}

		for(int i=0; i<n; i++) {
			int tmoney = 0;
			int s = i;
			int orgs = i;
			while(true) {
				if( tmoney + v[s] > k ) break;
				tmoney += v[s];
				s = (s + 1) % n;
				if ( s == orgs ) break;
			}
			m.push_back( tmoney );
			next.push_back( s );
		}

		long long money = 0;
		int s = 0;
		for(int i=0; i<r; i++) {
			money += m[s];
			s = next[s];
		}

		printf("Case #%d: %I64d\n", t, money);

	}
	return 0;

}

