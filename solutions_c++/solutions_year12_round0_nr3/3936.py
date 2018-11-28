#include<cstdio>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<fstream>

using namespace std;


typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;

const long double Pi = acos(-1.0);
const double Eps=1e-8;

template<class T> 
inline T sq(T a) { return a*a;}

const int MAXN = 2e6;

bool used[MAXN+1];
char t[101];
void shift(char* s, int len)
{
	char p = s[0], t;
	s[0] = s[len-1];
	for(int i = 1; i<len; i++)
		t = s[i], s[i] = p, p = t;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, a, b, r, ans;
	scanf("%d", &T);
	for(int tt = 0; tt<T; ++tt)
	{
		scanf("%d%d", &a, &b);
		ans = 0;
		memset(used, 0, sizeof(used));
		for(int i = a; i<=b; i++)
			if(!used[i])
			{
				itoa(i, t, 10);
				int len = strlen(t);
				int c = 1;
				for(int j = 0; j<len; j++)
					{
						shift(t, len);
						r = atoi(t);
						if(t[0] != '0' && a<=r && r<=b && i!=r && !used[r])
						{
							used[r] = true, c++;
						}
					}
				ans += c*(c-1)/2;
			}
		printf("Case #%d: %d\n", tt+1, ans);
	}
	return 0;
}