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

char t[44][44];
int x[44];
multiset<int> S;
int res,n;

inline void sw(int a, int b)
{
	res++;
	swap(x[a], x[b]);
}

void test()
{
	res = 0;
	scanf("%d", &n);
	fore(i,n) scanf("%s", t[i]);
	S.clear();
	fore(i,n)
	{
		for(x[i] = n-1; x[i] >= 0 && t[i][x[i]] == '0'; x[i]--) ;
		//printf("%d,", x[i]);
		S.insert(x[i]);
	}
	//printf("\n");
	for(int i = n-1; i >= 0; i--)
	{
		int pos = -1;
		fore(j,i+1) if(x[j] == i)
		{
			pos = j;
			break;
		}
		if(pos == -1)
		{
			for(int j = i; j >= 0; j--)
			{
				S.erase(S.find(x[j]));
				int cnt = 0, bad = 0;
				fort(q,S)
				{
					if(*q > cnt)
					{
						//printf("%d %d zle\n", *q, cnt);
						bad = 1;
						break;
					}
					cnt++;
				}
				S.insert(x[j]);
				if(!bad)
				{
					pos = j;
					break;
				}
			}
		}
		//printf("p=%d\n",pos);
		for(int j = pos; j < i; j++)
			sw(j,j+1);
		S.erase(S.find(x[i]));
		//printf("r=%d\n",res);
	}
	printf("%d\n", res);
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
