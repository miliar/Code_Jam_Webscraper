#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;
typedef vector<int> VI;
typedef vector<long long> VLL;
#define rep(i,N) for(i=0;i<N;i++)

int T,X,CA; double S,R,t; int N;
double ANS;

struct INV{
	int s,e; double v;
}I[1010];
bool cmp (const INV& a, const INV& b){return a.v < b.v;}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int i;

	scanf ("%d",&T); while (T--){
		scanf ("%d %lf %lf %lf %d",&X,&S,&R,&t,&N);
		for (i=0;i<N;i++){
			scanf ("%d %d %lf",&I[i].s,&I[i].e,&I[i].v);
			X -= I[i].e - I[i].s;
		}
		I[N].s = 0; I[N].e = X; I[N].v = 0; N++;
		sort (I,I+N,cmp); ANS = 0;
		for (i=0;i<N;i++){
			double vs = I[i].v + S, vr = I[i].v + R, l = I[i].e - I[i].s;
			if (l / vr < t){
				t -= l / vr;
				ANS += l / vr;
			}
			else{
				double x = vr * t;
				t = 0;
				ANS += x / vr + (l - x) / vs;
			}
		}

		printf ("Case #%d: %.10lf\n",++CA,ANS);
	}

	return 0;
}