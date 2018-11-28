#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

typedef long long ll; 
#define SQR(x) ((x)*(x))
const double EPS = 1e-8;
const double PI  = acos(-1.0);

bool v[2000000 + 1];

char buf[512];
int T, A, B;
int main()	{
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)	{
		memset(v, 0, sizeof(v));
		scanf("%d %d", &A, &B);
		ll ans = 0;
		for(int i = A; i <= B; i++)	{
			if(v[i])	{
				//printf("%d already in.. passing\n", i);
				continue;
			}
			v[i] = true;
			int cnt = 1;
			sprintf(buf, "%d", i);
			string s(buf);
			//printf("## Testing %d\n", i);
			for(int j = 1; j < s.size(); j++)	{
				rotate(s.begin(), s.begin()+1, s.end());
				//printf("%s ", s.c_str());
				if(s[0] == '0')	;
				else	{
					int t = atoi(s.c_str());
					if(t >= A && t <= B && !v[t])	{
						v[t] = true;
						cnt++;
					}
				}
			}
			//printf("\ncnt: %d\n", cnt);
			if(cnt > 1)		ans += (ll)cnt * (cnt - 1) / 2;
		}
		printf("Case #%d: %lld\n", tt, ans);
	}
	return 0;
}