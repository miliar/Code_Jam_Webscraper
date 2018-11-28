#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <string>
#include <cmath>
#include <iostream>
#include <stack>
#include <queue>
#include <ctime>
#include <utility>
#include <bitset>
#include <memory.h>
#include <deque>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define forn(i, a, b) for (int (i) = a; (i) < (b); (i)++)
#define ford(i,a,b) for (int i(a);i>=(b);--i)
#define sqr(n) (n)*(n)
#define all(v) (v).begin(), (v).end()
#define mem0(a) memset(a,0,sizeof(a))
#define mem1(a) memset(a,-1,sizeof(a))

#define INF 2000000000

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<pll> vll;

typedef pair<int, int> pii;
typedef vector<pii> vii;

typedef vector<int> vi;
typedef vector<vi> vvi;

struct path{
	int a,b,speed;
}temp;

vector<path> P;

bool f(path &a, path &b){
	return a.speed < b.speed;
}

int main()
{
	//freopen("A-small.in","r",stdin);
	//freopen("A-small.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	scanf("%d",&T);
	for(int z = 0; z < T; z++){
		printf("Case #%d: ",z+1);
		P.clear();
		int X, S, R, N;
		double t;
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
		int last = 0;
		for(int i = 0; i <= N; i++){
			int A, B, W;
			if(i!=N)
				scanf("%d%d%d",&A,&B,&W);
			else
			{
				A = last;
				B = X;
				W = 0;
			}
			if(A!=last){
				temp.a = last;
				temp.b = A;
				temp.speed = 0;
				P.push_back(temp);
			}
			temp.a = A;
			temp.b = B;
			temp.speed = W;
			last = B;
			P.push_back(temp);
		}
		
		sort(P.begin(), P.end(), f);

		double time = 0;

		for(int i = 0; i < P.size(); i++){
			double position = P[i].a;
			if(t>1e-9){
				double dist = P[i].b - P[i].a;
				double canMove = min(t, (double)dist / ((double)P[i].speed + R));
				t -= canMove;
				position += canMove * ((double)P[i].speed + R);
				time += canMove;
			}
			double dist = P[i].b - position;
			time += dist / ((double)P[i].speed + (double)S);
		}
		printf("%0.10lf",time);
		printf("\n");
	}

	return 0;
}