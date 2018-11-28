#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cassert>

using namespace std;

char s[10];
int a;

typedef pair<int,int> pii;

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int gi=1; gi<=cases; ++gi){
		int b = 1;
		int o = 1;
		unsigned wo = 0, wb = 0;
		int n;
		scanf("%d", &n);
		assert(n <= 100);
		vector<pii> B, O;
		for(int i=0; i<n; ++i){
			scanf(" %s %d", s, &a);
			if(s[0] == 'O') O.push_back(pii(a,i));
			else B.push_back(pii(a,i));
		}
		int t;
		int kt = 0;
		for(t=1; ; ++t)
		{
			bool change = false;
			if(wo < O.size()){
				if(o == O[wo].first){ if(kt == O[wo].second){ wo++; kt++; change = true; } }
				else if(o < O[wo].first) o++;
				else o--;
			}
			if(wb < B.size()){
				if(b == B[wb].first){ if(kt == B[wb].second && !change){ wb++; kt++; } }
				else if(b < B[wb].first) b++;
				else b--;
			}
			
			if(wo == O.size() && wb == B.size()) break;
		}
		
		printf("Case #%d: %d\n", gi, t);
	}
	return 0;
}
